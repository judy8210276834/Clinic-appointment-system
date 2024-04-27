import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status, Request
from starlette.responses import JSONResponse
from sqlalchemy import exc, func, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List

from app.middleware.exception import exception_message

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