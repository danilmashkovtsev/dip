from datetime import date

from sqlalchemy import Column, Integer, ForeignKey, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING, Optional, List

from .database import Base

metadata = MetaData()
'''
if TYPE_CHECKING:
    from .diagnostic import Diagnostic  # Пример условного импорта
    from .study import Study
    from .insurance import Insurance
    from .lpu import LPU
    from .doctor import Doctor
'''
class Pacient(Base):
    __tablename__ = "pacients"
    id: Mapped[int] = mapped_column(primary_key=True)
    card: Mapped[str] = mapped_column()
    polis: Mapped[str] = mapped_column()
    snils: Mapped[Optional[str]] = mapped_column(nullable=True)
    fName: Mapped[str] = mapped_column()
    sName: Mapped[str] = mapped_column()
    tName: Mapped[Optional[str]] = mapped_column(nullable=True)
    gender: Mapped[bool] = mapped_column()
    birthDate: Mapped[date] = mapped_column()
    region: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    street: Mapped[str] = mapped_column()
    house: Mapped[int] = mapped_column()
    aps: Mapped[Optional[int]] = mapped_column(nullable=True)
    postIndex: Mapped[Optional[int]] = mapped_column(nullable=True)
    jobPlace: Mapped[Optional[str]] = mapped_column(nullable=True)
    jobProf: Mapped[Optional[str]] = mapped_column(nullable=True)
    disability: Mapped[Optional[bool]] = mapped_column(nullable=True)
    disabilityGroup: Mapped[Optional[int]] = mapped_column(nullable=True)
    polOrg: Mapped[List["Insurance"]] = relationship("Insurance", back_populates="pacient", cascade="all, delete-orphan")
    studyGrade: Mapped[List["Study"]] = relationship("Study", back_populates="pacient", cascade="all, delete-orphan")
    def __str__(self):
        return f"Pacient {self.card}"

class Study(Base):
    __tablename__ = "studies"
    id: Mapped[int] = mapped_column(primary_key=True)
    pacId: Mapped[int] = mapped_column(ForeignKey("pacients.id", ondelete="CASCADE"))
    grade: Mapped[str] = mapped_column()
    pacient: Mapped["Pacient"] = relationship("Pacient", back_populates="studyGrade")
    def __str__(self):
        return f"Study {self.grade}"

class Insurance(Base):
    __tablename__ = "insurances"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    pacId: Mapped[int] = mapped_column(ForeignKey("pacients.id", ondelete="CASCADE"))
    pacient: Mapped["Pacient"] = relationship("Pacient", back_populates="polOrg")
    def __str__(self):
        return f"Insur {self.name}"

class LPU(Base):
    __tablename__ = "lpus"
    id: Mapped[int] = mapped_column(primary_key=True)
    ogrn: Mapped[str] = mapped_column()
    lpuName: Mapped[str] = mapped_column()
    sName: Mapped[Optional[str]] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    postIndex: Mapped[Optional[int]] = mapped_column(nullable=True)
    doctors: Mapped[List["Doctor"]] = relationship("Doctor", back_populates="lpu", cascade="all, delete-orphan")
    def __str__(self):
        return f"LPU {self.sName}"

class Doctor(Base):
    __tablename__ = "doctors"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_LPU: Mapped[int] = mapped_column(ForeignKey("lpus.id", ondelete="CASCADE"))
    fName: Mapped[str] = mapped_column()
    sName: Mapped[str] = mapped_column()
    tName: Mapped[Optional[str]] = mapped_column(nullable=True)
    spec: Mapped[str] = mapped_column()
    regDate: Mapped[date] = mapped_column()
    lpu: Mapped["LPU"] = relationship("LPU", back_populates="doctors")
    diagnostics: Mapped[List["Diagnostic"]] = relationship("Diagnostic", back_populates="doctor", cascade="all, delete-orphan")
    def __str__(self):
        return f"Doc {self.sName}"

class Diagnostic(Base):
    __tablename__ = "diagnostics"
    id: Mapped[int] = mapped_column(primary_key=True)
    pacId: Mapped[int] = mapped_column(ForeignKey("pacients.id", ondelete="CASCADE"))
    docId: Mapped[int] = mapped_column(ForeignKey("doctors.id", ondelete="CASCADE"))
    ExamDate: Mapped[date] = mapped_column()
    Diagnosis: Mapped[str] = mapped_column()
    Recommendations: Mapped[Optional[str]] = mapped_column(nullable=True)
    doctor: Mapped["Doctor"] = relationship("Doctor", back_populates="diagnostics")
   # examinations: Mapped[List[str]] = relationship("Examination", back_populates="diagnostic", cascade="all, delete-orphan")  # Предположение
    def __str__(self):
        return f"Diag {self.ExamDate}"
'''
class Examination(Base):
    __tablename__ = "examinations"
    id = Column(Integer, primary_key=True, index=True)
    diagId = Column(Integer, ForeignKey("diagnostics.id", ondelete="CASCADE"))
    ExamType = Column(String)
    ExamDate = Column(Date)
    ExamResults = Column(String, nullable=True)
    diagnostic = relationship("Diagnostic", back_populates="examinations")
'''
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
