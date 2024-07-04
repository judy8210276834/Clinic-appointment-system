from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey, CheckConstraint, Float, Uuid, Date
# from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base, relationship, mapped_column, DeclarativeBase, Mapped
from datetime import datetime
from typing import Optional, List
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    pass


class Patients(Base):
    __tablename__ = 'patients'

    uid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(60))
    phone_number: Mapped[str] = mapped_column(String(30))
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    
    appointments: Mapped[List["Appointments"]] = relationship(back_populates="patients")
    

class Users(Base):
    __tablename__ = 'users'

    uid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    account: Mapped[str] = mapped_column(String(60))
    password: Mapped[str] = mapped_column(String(60))
    name: Mapped[str] = mapped_column(String(60))
    user_group: Mapped[list] = mapped_column(String(60))
    level: Mapped[int] = mapped_column(Integer)
    email: Mapped[Optional[str]] = mapped_column(String(120))
    phone_number: Mapped[str] = mapped_column(String(30))
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    admin_basic: Mapped[List["AdminBasic"]] = relationship(back_populates="users")
    appointments: Mapped[List["Appointments"]] = relationship(back_populates="users")
    clinic_status: Mapped[List["ClinicStatus"]] = relationship(back_populates="users")


class AdminBasic(Base):
    __tablename__ = 'admin_basic'

    uid: Mapped[int] = mapped_column(primary_key=True)
    fk_user: Mapped[UUID] = mapped_column(ForeignKey("users.uid"))
    patient_medical_fees: Mapped[Optional[int]] = mapped_column(Integer)
    time_appointment_limit: Mapped[Optional[int]] = mapped_column(Integer)
    people_appointment_limit: Mapped[Optional[int]] = mapped_column(Integer)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    users: Mapped["Users"] = relationship(back_populates="admin_basic")


class Reports(Base):
    __tablename__ = 'reports'

    uid: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[str] = mapped_column(String(30))
    month: Mapped[str] = mapped_column(String(30))
    total_appointment_people: Mapped[int] = mapped_column(Integer)
    total_site_people: Mapped[int] = mapped_column(Integer)
    total_cancel_people: Mapped[int] = mapped_column(Integer)
    total_not_arrived_people: Mapped[int] = mapped_column(Integer)
    total_pay_people: Mapped[int] = mapped_column(Integer)
    total_money: Mapped[int] = mapped_column(Integer)

    appointments: Mapped[List["Appointments"]] = relationship(back_populates="reports")
    

class Appointments(Base):
    __tablename__ = 'appointments'

    uid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    fk_patient: Mapped[UUID] = mapped_column(ForeignKey("patients.uid"))
    fk_report: Mapped[Optional[int]] = mapped_column(ForeignKey("reports.uid"))
    fk_user: Mapped[Optional[UUID]] = mapped_column(ForeignKey("users.uid"))
    ip: Mapped[Optional[str]] = mapped_column(String(60))
    appointment_status: Mapped[int] = mapped_column(Integer)
    people_number: Mapped[int] = mapped_column(Integer)
    date: Mapped[Date] = mapped_column(Date)
    time_period: Mapped[str] = mapped_column(String(30))
    medical_fees: Mapped[Optional[int]] = mapped_column(Integer)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    is_reported: Mapped[bool] = mapped_column(Boolean, default=False)

    patients: Mapped["Patients"] = relationship(back_populates="appointments")
    reports: Mapped["Reports"] = relationship(back_populates="appointments")
    users: Mapped["Users"] = relationship(back_populates="appointments")
    

class ClinicStatus(Base):
    __tablename__ = 'clinic_status'

    uid: Mapped[int] = mapped_column(primary_key=True)
    fk_user: Mapped[UUID] = mapped_column(ForeignKey("users.uid"))
    date: Mapped[Date] = mapped_column(Date)
    time_period: Mapped[Optional[str]] = mapped_column(String(30))
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    is_closed: Mapped[bool] = mapped_column(Boolean, default=True)
    
    users: Mapped["Users"] = relationship(back_populates="clinic_status")

