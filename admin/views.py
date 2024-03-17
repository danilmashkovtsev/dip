from sqladmin import ModelView

from models.model import Doctor, LPU, Pacient


class PacAdmin(ModelView, model=Pacient):
    column_list = [c.name for c in Pacient.__table__.c]
    can_delete = False
    name = "Пациент"
    name_plural = "Пациенты"
    icon = "fa-solid fa-user"
class LPUAdmin(ModelView, model=LPU):
    column_list = [c.name for c in LPU.__table__.c]
    can_delete = False
    name = "Больница"
    name_plural = "Больницы"
class DocAdmin(ModelView, model=Doctor):
    column_list = [Doctor.id,Doctor.sName ,Doctor.id_LPU]
    column_details_exclude_list = [Doctor.regDate]
    can_delete = False
    name = "Врач"
    name_plural = "Врачи"
    icon = "fa-solid fa-user"
   # category = "accounts"