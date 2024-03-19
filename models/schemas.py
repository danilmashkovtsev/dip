from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class PacientBase(BaseModel):
    card: str
    polis: str
    snils: Optional[str] = None
    fName: str
    sName: str
    tName: Optional[str] = None
    gender: bool
    birthDate: date
    region: str
    city: str
    street: str
    house: int
    aps: Optional[int] = None
    postIndex: Optional[int] = None
    jobPlace: Optional[str] = None
    jobProf: Optional[str] = None
    disability: Optional[bool] = None
    disabilityGroup: Optional[int] = None

class StudyBase(BaseModel):
    grade: str

class InsurBase(BaseModel):
    name: str

class LPUBase(BaseModel):
    ogrn: str
    lpuName: str
    sName: Optional[str] = None
    address: str
    phone: str
    email: str
    postIndex: Optional[int] = None

class DoctorBase(BaseModel):
    fName: str
    sName: str
    tName: Optional[str] = None
    spec: str
    regDate: date

class DiagnosticBase(BaseModel):
    ExamDate: date
    Diagnosis: str
    Recommendations: Optional[str] = None

# Модели с отношениями
class PacientModel(PacientBase):
    polOrg: List[InsurBase] = []
    studyGrade: List[StudyBase] = []

class StudyModel(StudyBase):
    pacient: PacientBase

class InsurModel(InsurBase):
    pacient: PacientBase

class LPUModel(LPUBase):
    doctors: List[DoctorBase] = []

class DoctorModel(DoctorBase):
    lpu: LPUBase
    diagnostics: List[DiagnosticBase] = []

class DiagnosticModel(DiagnosticBase):
    doctor: DoctorBase
    examinations: List[str] = []  # Предположим, что examinations это список строк для простоты

# Обратите внимание: Pydantic не поддерживает напрямую отношения SQLAlchemy,
# так что вы должны определить, как данные должны быть сериализованы/десериализованы между вашим API и базой данных.

class Star1(BaseModel):
    P1: int = 0
    Gi1: int = 0
    P2: int = 0
    Gi2: int = 0
    P3: int = 0
    Gi3: int = 0
    P4: int = 0
    Gi4: int = 0
    RP1: int = 0
    E1: int = 0
    RP2: int = 0
    E2: int = 0
    RP3: int = 0
    E3: int = 0
    R1: int = 0
    V1: int = 0
    R2: int = 0
    V2: int = 0
    F1: int = 0
    VB1: int = 0
    C1: int = 0
    IG1: int = 0
    F2: int = 0
    VB2: int = 0
    R3: int = 0
    V3: int = 0
    RP4: int = 0
    E4: int = 0
    C2: int = 0
    IG2: int = 0
    F3: int = 0
    VB3: int = 0
    R4: int = 0
    V4: int = 0
    F4: int = 0
    VB4: int = 0
    C3: int = 0
    IG3: int = 0
    C4: int = 0
    IG4: int = 0
class Star2(BaseModel):
    MC1: int = 0
    TR1: int = 0
    MC2: int = 0
    TR2: int = 0
    MC3: int = 0
    TR3: int = 0
    MC4: int = 0
    TR4: int = 0
    MC5: int = 0
    TR5: int = 0
    F: int = 0
    VB: int = 0
    C: int = 0
    IG: int = 0
    R: int = 0
    V: int = 0
    RP: int = 0
    E: int = 0
    P: int = 0
    Gi: int = 0