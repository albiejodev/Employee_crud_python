from fastapi import FastAPI

from src.controllers.employee_controller import router as employee_router


app = FastAPI()

app.include_router(
    employee_router,
    prefix="/api"
)


@app.get("/")
def home():
    return {"message": "Hello World"}
