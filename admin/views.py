from sqladmin import ModelView

from models.model import Doctor, LPU, Pacient, Insurance,Study,Diagnostic


class PacAdmin(ModelView, model=Pacient):
    column_list = [c.name for c in Pacient.__table__.c] + [Pacient.polOrg]
    can_delete = False
    name = "Пациент"
    name_plural = "Пациенты"
    icon = "fa-solid fa-user"
class LPUAdmin(ModelView, model=LPU):
    column_list = [c.name for c in LPU.__table__.c]
    can_delete = False
    name = "Больница"
    name_plural = "Больницы"
    icon = "fa-solid fa-hospital"
class DocAdmin(ModelView, model=Doctor):
    column_list = [Doctor.id,Doctor.sName ,Doctor.id_LPU]
    column_details_exclude_list = [Doctor.regDate]
    can_delete = False
    name = "Врач"
    name_plural = "Врачи"
    icon = "fa-solid fa-user-md"
    #category = "accounts"
class InsAdmin(ModelView, model=Insurance):
    column_list = [c.name for c in Insurance.__table__.c]
    can_delete = False
    name = "Страховая"
    name_plural = "Страховые организации"
    icon = "fa-solid fa-shield-alt"

class StudyAdmin(ModelView, model=Study):
    column_list = [c.name for c in Study.__table__.c]
    can_delete = False
    name = "Образование"
    name_plural = "Уровень образования"
    icon = "fa-solid fa-graduation-cap"

class DiagAdmin(ModelView, model=Diagnostic):
    column_list = [c.name for c in Diagnostic.__table__.c]
    can_delete = False
    name = "Диагностика"
    name_plural = "Диагностики"
    icon = "fa-solid fa-microscope"
