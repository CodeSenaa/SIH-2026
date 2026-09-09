from fastapi import APIRouter
from .abc_route import router as abc_router


sample_router = APIRouter()
sample_router.include_router(abc_router)


