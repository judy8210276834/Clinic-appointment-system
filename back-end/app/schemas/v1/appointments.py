from datetime import date, datetime
from pydantic import BaseModel, Field
from uuid import UUID


"""
Appointments Pydantic Schema
"""


class AppointmentsBase(BaseModel):

    uid: UUID = Field(description="Appointment uid")
    fk_patient: UUID = Field(description="Patient uid")
    fk_report: int | None = Field(None, description="Report uid")
    fk_user: UUID | None = Field(None, description="User uid")
    ip: str | None = Field(None, description="IP address")
    appointment_status: int = Field(description="Appoint status")
    people_number: int = Field(description="Number of people")
    appointment_date: date = Field(description="Appointment date")
    time_period: str = Field(description="Appointment time period")
    medical_fees: int | None = Field(None, description="Medical fees")
    create_time: datetime = Field(description="Appointment create time")
    is_completed: bool = Field(description="Is appointment completed")
    is_reported: bool = Field(description="Is appointment reported")

    class Config:
        from_attributes = True


class AppointmentsCreate(BaseModel):

    # fk_patient: UUID = Field(description="Patient uid")
    name: str = Field(description="Patient name")
    phone_number: str = Field(description="Patient phone number")
    fk_user: UUID | None = Field(None, description="User uid")
    ip: str | None = Field(None, description="IP address")
    appointment_status: int = Field(description="Appoint status")
    people_number: int = Field(description="Number of people")
    appointment_date: date = Field(description="Appointment date")
    time_period: str = Field(description="Appointment time period")
    medical_fees: int | None = Field(None, description="Medical fees")

    class Config:
        from_attributes = True

