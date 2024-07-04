import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status, Request
from starlette.responses import JSONResponse
from sqlalchemy import exc, func, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List

from app.database.database import get_conn
from app.middleware.exception import exception_message
from app.models.model import Patients
from app.schemas.v1.patients import (
    PatientsBase, 
    PatientsCreate
)


# router = APIRouter(
#     dependencies=[Depends(authenticate_basic)],
#     responses={404: {"detail": "data not found"}})

router = APIRouter()


# Declare Logger
uvicorn_logger = logging.getLogger('uvicorn.error')
system_logger = logging.getLogger('custom.error')


# @router.get("/")
# async def test():
#     return JSONResponse(status_code=200, content="Here goes the apis")


### [GET]: Get all patients
@router.get("", response_model=List[PatientsBase], name="Get all patients", description="Get all patients", include_in_schema=True)
async def get_all_patients(
    db: Session=Depends(get_conn)
    ):
    '''
    Get all patients

    Parameters:
        db (Session): Database Session Dependency

    Return:
        data (Pydantic Model): List[PatientsBase]
    '''
    try: 
        data = db.query(Patients).order_by(Patients.create_time.desc()).all()

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500)
    
    if not data:
        raise HTTPException(status_code=404, detail=f"No patient found")
    
    return data


### [POST]: Create patient
@router.post("", name="Create patient", description="Create patient", include_in_schema=True)
async def create_patient(
    data: PatientsCreate,
    db: Session=Depends(get_conn)
    ):
    '''
    Create patient

    Parameters:
        data (Pydantic Model): PatientsCreate 
        db (Session): Database Session Dependency
    
    Return:
        JSONResponse: Create patient successfully
    '''
    try:
        existing_patient = db.query(Patients)\
            .filter(
                Patients.name==data.name,
                Patients.phone_number==data.phone_number)\
            .first()

        if existing_patient:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Duplicate patient data"
            )
        
        patient = Patients(
            name=data.name,
            phone_number=data.phone_number
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)

    except HTTPException as he:
        system_logger.error(exception_message(he))
        raise he
  
    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
            )
    
    return JSONResponse(status_code=200, content="Create patient successfully")