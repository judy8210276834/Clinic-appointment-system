import json
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status, Request
from starlette.responses import JSONResponse
from sqlalchemy import exc, func, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List

# from app.core.auth import basic_authenticate_user, get_hash_password
# from app.database.ai_integrations import get_conn
# from app.schemas.v1.system_users import SystemUserBase, SystemUserCreate, SystemUserGet
from app.middleware.exception import exception_message
# from app.models.ai_integrations import SystemUsers

# from app.middleware.exception import exception_message

# from app.crud import  as auth_crud

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