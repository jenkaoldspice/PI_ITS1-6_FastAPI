import uvicorn
from fastapi import FastAPI, Request, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from db.base import database
from domains.employee import EmployeeIn
from endpoints import employees
from endpoints.depends import get_employee_repository
from repositories.employees import EmployeeRepository

app = FastAPI(title="WEBSTUDIO")
templates = Jinja2Templates(directory="templates/")

app.include_router(employees.router, prefix="/employees", tags=["employess"])

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.get('/')
async def mainpage(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request}) \

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
