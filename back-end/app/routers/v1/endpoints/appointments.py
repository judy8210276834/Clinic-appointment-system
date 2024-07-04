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
from app.models.model import Appointments, Patients
from app.routers.v1.endpoints.patients import create_patient
from app.schemas.v1.appointments import (
    AppointmentsBase,
    AppointmentsCreate
)

# router = APIRouter(
#     dependencies=[Depends(authenticate_basic)],
#     responses={404: {"detail": "data not found"}})

router = APIRouter()

# Declare Logger
uvicorn_logger = logging.getLogger('uvicorn.error')
system_logger = logging.getLogger('custom.error')

@router.get("/")
async def test():
    return JSONResponse(status_code=200, content="Here goes the apis")


### [GET]: Get all appointments
@router.get("", response_model=List[AppointmentsBase], name="Get all appointments", description="Get all appointments", include_in_schema=True)
async def get_all_appointments(
    db: Session=Depends(get_conn)
    ):
    '''
    Get all appointments

    Parameters:
        db (Session): Database Session Dependency

    Return:
        data (Pydantic Model): List[AppointmentsBase]
    '''
    try: 
        data = db.query(Appointments).order_by(Appointments.create_time.desc()).all()

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500)
    
    if not data:
        raise HTTPException(status_code=404, detail=f"No appointment found")
    
    return data


### [POST]: Create appointment
@router.post("", name="Create appointment", description="Create appointment", include_in_schema=True)
async def create_appointment(
    data: AppointmentsCreate,
    db: Session=Depends(get_conn)
    ):
    '''Create appointment

    Parameters:
        data (Pydantic Model): AppointmentsCreate 
        db (Session): Database Session Dependency
    
    Return:
        JSONResponse: Create appointment successfully
    '''
    try:
        patient_data = db.query(Patients)\
            .filter(
                Patients.name==data.name,
                Patients.phone_number==data.phone_number
                )\
            .one_or_none()

        if patient_data is None:
            patient = Patients(
                name=data.name,
                phone_number=data.phone_number
            )
            await create_patient(patient, db)

            patient_data = db.query(Patients)\
            .filter(
                Patients.name==data.name,
                Patients.phone_number==data.phone_number
                )\
            .one_or_none()
        
        fk_patient = patient_data.uid

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
            )
    
    try:
        appointment = Appointments(
            fk_patient=fk_patient,
            fk_user=data.fk_user,
            ip=data.ip,
            appointment_status=data.appointment_status,
            people_number=data.people_number,
            date=data.appointment_date,
            time_period=data.time_period,
            medical_fees=data.medical_fees,
        )
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
  
    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
            )
    
    return JSONResponse(status_code=200, content="Create appointment successfully")