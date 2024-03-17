from datetime import date
from typing import Optional, List

from sqlalchemy  import MetaData, Integer, ForeignKey,Column
from sqlalchemy.orm import Mapped , mapped_column, relationship

from .database import Base

metadata = MetaData()

class Pacient(Base):
    __tablename__ = "pacients"
    id: Mapped[int] = mapped_column(primary_key=True)
    card: Mapped[str]
    polis: Mapped[str]
    polOrg: Mapped[List["Insur"]] = relationship(
        back_populates="name" , cascade = "all, delete-orphan"
    )
    snils: Mapped[Optional[str]]
    fName: Mapped[str]
    sName: Mapped[str]
    tName: Mapped[Optional[str]]
    gender: Mapped[bool]
    birthDate: Mapped[date]
    region: Mapped[str]
    city: Mapped[str]
    street: Mapped[str]
    house: Mapped[int]
    aps: Mapped[Optional[int]]
    postIndex: Mapped[Optional[int]]
    #studyGrade = Column(Integer, ForeignKey("studies.StudyId"), nullable=False)
    studyGrade: Mapped[List["Study"]] = relationship(
        back_populates="grade" , cascade = "all, delete-orphan"
    )
    jobPlace: Mapped[Optional[str]]
    jobProf: Mapped[Optional[str]]
    disability: Mapped[Optional[bool]]
    disabilityGroup: Mapped[Optional[int]]

class Study(Base):
    __tablename__ = "studies"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    pacId: Mapped[int] = mapped_column(ForeignKey("pacients.id"))
    grade: Mapped["Pacient"] = relationship(back_populates = "studyGrade")

class Insur(Base):
    __tablename__ = "insurances"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    pacId: Mapped[int] = mapped_column (ForeignKey ("pacients.id"))
    name: Mapped["Pacient"] = relationship(back_populates = "polOrg")

class LPU(Base):
    __tablename__ = "lpus"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ogrn: Mapped[str]
    lpuName: Mapped[str]
    sName: Mapped[Optional[str]]
    adress: Mapped[str]
    #mainDoc: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    #secondDoc: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    phone: Mapped[str]
    email: Mapped[str]
    postIndex: Mapped[Optional[int]]


class Doctor(Base):
    __tablename__ = "doctors"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_LPU: Mapped[int] = mapped_column(ForeignKey("lpus.id"))
    fName: Mapped[str]
    sName: Mapped[str]
    tName: Mapped[Optional[str]]
    spec: Mapped[str] # Возможно добавить таблицу Specs...
    regDate: Mapped[date]

class Diagnostic(Base):
    __tablename__ = "diagnostics"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    pacId: Mapped[int] = mapped_column(ForeignKey("pacients.id"))
    docId: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
   # examid: Mapped[List["Examination"]] = relationship(
    #    back_populates = "id", cascade = "all, delete-orphan"
    #)

    ExamDate: Mapped[date]
    Diagnosis: Mapped[str]
    Recommendations: Mapped[Optional[str]] 

class Examination(Base):
    __tablename__ = "examinations"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    pacId: Mapped[int] = mapped_column(ForeignKey("pacients.id"))
    diagId: Mapped[int] = mapped_column(ForeignKey("diagnostics.id"))
   # diag: Mapped["Diagnostic"] = relationship(back_populates = "examid")

    ExamType: Mapped[str]
    ExamDate: Mapped[date]
    ExamResults: Mapped[Optional[str]]

class Star1Data(Base):
    __tablename__ = 'star1_data'
    id = Column (Integer, primary_key = True, index = True)
    P1 = Column (Integer)
    Gi1 = Column (Integer)
    P2 = Column (Integer)
    Gi2 = Column (Integer)
    P3 = Column (Integer)
    Gi3 = Column (Integer)
    P4 = Column (Integer)
    Gi4 = Column (Integer)
    RP1 = Column (Integer)
    E1 = Column (Integer)
    RP2 = Column (Integer)
    E2 = Column (Integer)
    RP3 = Column (Integer)
    E3 = Column (Integer)
    R1 = Column (Integer)
    V1 = Column (Integer)
    R2 = Column (Integer)
    V2 = Column (Integer)
    F1 = Column (Integer)
    VB1 = Column (Integer)
    C1 = Column (Integer)
    IG1 = Column (Integer)
    F2 = Column (Integer)
    VB2 = Column (Integer)
    R3 = Column (Integer)
    V3 = Column (Integer)
    RP4 = Column (Integer)
    E4 = Column (Integer)
    C2 = Column (Integer)
    IG2 = Column (Integer)
    F3 = Column (Integer)
    VB3 = Column (Integer)
    R4 = Column (Integer)
    V4 = Column (Integer)
    F4 = Column (Integer)
    VB4 = Column (Integer)
    C3 = Column (Integer)
    IG3 = Column (Integer)
    C4 = Column (Integer)
    IG4 = Column (Integer)

class Star2Data(Base):
    __tablename__ = 'star2_data'
    id = Column (Integer, primary_key = True, index = True)
    MC1 = Column (Integer)
    TR1 = Column (Integer)
    MC2 = Column (Integer)
    TR2 = Column (Integer)
    MC3 = Column (Integer)
    TR3 = Column (Integer)
    MC4 = Column (Integer)
    TR4 = Column (Integer)
    MC5 = Column (Integer)
    TR5 = Column (Integer)
    F = Column (Integer)
    VB = Column (Integer)
    C = Column (Integer)
    IG = Column (Integer)
    R = Column (Integer)
    V = Column (Integer)
    RP = Column (Integer)
    E = Column (Integer)
    P = Column (Integer)
    Gi = Column (Integer)
