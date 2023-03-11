from fastapi import APIRouter
from fastapi import Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.models.task import Task
from app.config.config import app_settings


router = APIRouter()
templates = Jinja2Templates(directory='app/templates')


@router.get('/')
async def index(request: Request, database: Session = Depends(get_db)):
    task = database.query(Task).first()
    if task is None:
        task = Task(
            id=0,
            title='You do not have any tasks. For actions, you must create a new one',
            is_completed=False
        )

    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'APP_NAME': app_settings.APP_NAME,
            'task': task,
        }
    )


@router.post('/add')
async def add_task(
        title: str | None = Form(default=None),
        database: Session = Depends(get_db)
) -> RedirectResponse:
    if title is not None:
        new_task = Task(title=title)
        database.add(new_task)
        database.commit()

    return RedirectResponse(
        url=router.url_path_for('index'),
        status_code=302
    )


@router.get('/update/{task_id}')
async def update_task(
        task_id: int,
        database: Session = Depends(get_db)
) -> RedirectResponse:
    task = database.query(Task).filter(Task.id == task_id).first()
    task.is_completed = not task.is_completed
    database.commit()

    return RedirectResponse(
        url=router.url_path_for('index'),
        status_code=302
    )


@router.get('/delete/{task_id}')
async def delete_task(
        task_id: int,
        database: Session = Depends(get_db)
) -> RedirectResponse:
    task = database.query(Task).filter_by(id=task_id).first()
    database.delete(task)
    database.commit()

    return RedirectResponse(
        url=router.url_path_for('index'),
        status_code=302
    )
