from fastapi import APIRouter

router = APIRouter(prefix="/sample",tags=["sample"])

@router.get("/test")
def test():
    return {"message": "test"}

