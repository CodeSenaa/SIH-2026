import uvicorn

from connect import app
from SAMPLE_MODULE.api import sample_router

def create_app():
    app.include_router(sample_router)
    return app


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )