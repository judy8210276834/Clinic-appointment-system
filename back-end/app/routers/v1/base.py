from fastapi import APIRouter, Depends

# from app.core.auth import basic_authenticate_user
from app.routers.v1.endpoints import (
    auth,
    patients,
    users,
    admin_basic,
    reports,
    appointments,
    clinic_status
)

router_v1 = APIRouter()
# router_v1 = APIRouter(dependencies=[Depends(basic_authenticate_user)])

router_v1.include_router(auth.router, prefix="/auth", tags=["Token Authentication"])
router_v1.include_router(patients.router, prefix="/patients", tags=["Patients"])
router_v1.include_router(users.router, prefix="/users", tags=["Users"])
router_v1.include_router(admin_basic.router, prefix="/admin-basic", tags=["Admin Basic"])
router_v1.include_router(reports.router, prefix="/reports", tags=["Reports"])
router_v1.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
router_v1.include_router(clinic_status.router, prefix="/clinic-status", tags=["Clinic Status"])


