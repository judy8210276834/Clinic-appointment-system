from datetime import date, datetime
from pydantic import BaseModel, Field
from uuid import UUID


"""
Patients Pydantic Schema
"""

class PatientsBase(BaseModel):

    uid: UUID = Field(description="Patient uid")
    name: str = Field(description="Patient name")
    phone_number: str = Field(description="Patient phone number")
    create_time: datetime = Field(description="Patient create time")
    
    class Config:
        from_attributes = True


class PatientsCreate(BaseModel):

    name: str = Field(description="Patient name")
    phone_number: str = Field(description="Patient phone number")

    class Config:
        from_attributes = True

