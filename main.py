from fastapi import FastAPI
from models import model
from models.database import engine
from routers.stars import star as star_router
from routers.wins import win as win_router
from routers.table import table as table_router

#model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical Pulse")

app.include_router(
    router=star_router,
    prefix='/stars',
)

app.include_router(
    router=win_router,
    prefix='/win',
)

#--------------------------------------------

app.include_router(
    router=table_router,
    prefix='/table',
)
