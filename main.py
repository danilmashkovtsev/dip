from fastapi import FastAPI

from admin.views import DocAdmin, LPUAdmin, PacAdmin
from models import model
from models.database import engine
from routers.stars import star as star_router
from routers.wins import win as win_router
from routers.table import table as table_router
from sqladmin import Admin

model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical Pulse")

admin = Admin(app, engine)

admin.add_view(DocAdmin)
admin.add_view(LPUAdmin)
admin.add_view(PacAdmin)

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
