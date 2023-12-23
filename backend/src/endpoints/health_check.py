from enum import Enum

from fastapi import status
from fastapi.routing import APIRouter

from fastapi_utils.api_model import APIModel
from pydantic import Field

router = APIRouter()


class ServiceHealthEnum(str, Enum):
    """Enumerator class for possible service health values"""

    OK = "OK"
    FAILURE = "FAILURE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


class HealthInfo(APIModel):
    """Pydantic model for health information response"""

    title: str = Field(..., description="Name of the service")
    description: str = Field(..., description="Brief overview of the service")
    version: str = Field(..., description="Service version identifier")
    status: ServiceHealthEnum = Field(..., description="Current health state of the service")


@router.get(
    "/status",
    response_model=HealthInfo,
    status_code=status.HTTP_200_OK,
    tags=["Health Check"],
    summary="Execute health check",
    description="Carries out a health check and provides information about the active service.",
    responses={200: {"description": "Health state of the service"}},
)
async def get_health_status():
    """Conduct a health check and return the status."""
    return {
        "title": "Backend Service",
        "description": "API Service for Backend",
        "version": "v1.0",
        "status": ServiceHealthEnum.OK,
    }