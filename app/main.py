from fastapi import FastAPI
from app.routes.students import students_router
from app.routes.users import user_router

app = FastAPI(
    title="Student Course API",
    summary="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection.",
)

app.include_router(students_router)
app.include_router(user_router)
