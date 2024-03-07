from sqlalchemy  import MetaData, Integer, String , Boolean, ForeignKey,Column,Date

from .database import Base

metadata = MetaData()

class Pacient(Base):
    __tablename__ = "pacients"
    metadata
    PacId = Column(Integer, primary_key=True, nullable=False, index=True)
    Card = Column(String, nullable=False)
    Polis = Column(String, nullable=False)
    PolOrg = Column(String, nullable=False)
    Snils = Column(String, nullable=True) # Сделать необязательным или убрать
    FName = Column(String, nullable=False)
    SName = Column(String, nullable=False)
    TName = Column(String, nullable=True)
    Gender = Column(Boolean, nullable=False)
    BirthDate = Column(Date, nullable=False)
    Region = Column(String, nullable=False)
    City = Column(String, nullable=False)
    Street = Column(String, nullable=False)
    House = Column(Integer, nullable=False)
    Aps = Column(Integer, nullable=True)
    PostIndex = Column(Integer, nullable=True)
    StudyGrade = Column(Integer, ForeignKey("study.StudyId"), nullable=False)
    JobPlace = Column(String, nullable=True)
    JobProf = Column(String, nullable=True)
    Disability = Column(Boolean, nullable=True)
    DisabilityGroup = Column(Integer, nullable=True)

class Study(Base):
    __tablename__ = "study"
    metadata
    StudyId = Column(Integer, primary_key=True, index=True)
    Grade = Column(String, nullable=False)

class LPU(Base):
    __tablename__ = "lpu"
    metadata
    LPUId = Column(Integer, primary_key=True, index=True)
    OGRN = Column(String, nullable=False)
    LPUName = Column(String, nullable=False)
    ShortName = Column(String, nullable=True)
    Adress = Column(String, nullable=False)
    MainDoc = Column(Integer, ForeignKey("doctor.DocId"), nullable=False)
    SecondDoc = Column(Integer, ForeignKey("doctor.DocId"), nullable=False)
    Phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    PostIndex = Column(Integer, nullable=True)


class Doctor(Base):
    __tablename__ = "doctor"
    metadata
    DocId = Column(Integer, primary_key=True, index=True)
    Id_LPU = Column(Integer, ForeignKey("lpu.LPUId"), nullable=False)
    FName = Column(String, nullable=False)
    SName = Column(String, nullable=False)
    TName = Column(String, nullable=True)
    Spec = Column(String, nullable=False)
    RegDate = Column(Date, nullable=True)

class Diagnostic(Base):
    __tablename__ = "diagnostic"
    metadata
    DiagId = Column(Integer, primary_key=True, index=True)
    PacId = Column(Integer, ForeignKey("pacients.PacId"), nullable=False)
    DocId = Column(Integer, ForeignKey("doctor.DocId"), nullable=False)
    ExamDate = Column(Date, nullable=False)
    Diagnosis = Column(String, nullable=False)
    Recommendations = Column(String, nullable=True)

class Examination(Base):
    __tablename__ = "examinations"
    metadata
    ExamId = Column(Integer, primary_key=True, index=True)
    PacId = Column(Integer, ForeignKey("pacients.PacId"), nullable=False)
    DiagId = Column(Integer, ForeignKey("diagnostic.DiagId"), nullable=False)
    ExamType = Column(String, nullable=False)
    ExamDate = Column(Date, nullable=False)
    ExamResults = Column(String, nullable=True)

class Star1Data(Base):
    __tablename__ = 'star1_data'
    metadata
    id = Column(Integer, primary_key=True, index=True)
    P1 = Column(Integer)
    Gi1 = Column(Integer)
    P2 = Column(Integer)
    Gi2 = Column(Integer)
    P3 = Column(Integer)
    Gi3 = Column(Integer)
    P4 = Column(Integer)
    Gi4= Column(Integer)
    RP1= Column(Integer)
    E1= Column(Integer)
    RP2= Column(Integer)
    E2= Column(Integer)
    RP3= Column(Integer)
    E3= Column(Integer)
    R1= Column(Integer)
    V1= Column(Integer)
    R2= Column(Integer)
    V2= Column(Integer)
    F1= Column(Integer)
    VB1= Column(Integer)
    C1= Column(Integer)
    IG1= Column(Integer)
    F2= Column(Integer)
    VB2= Column(Integer)
    R3= Column(Integer)
    V3= Column(Integer)
    RP4= Column(Integer)
    E4= Column(Integer)
    C2= Column(Integer)
    IG2= Column(Integer)
    F3= Column(Integer)
    VB3= Column(Integer)
    R4= Column(Integer)
    V4= Column(Integer)
    F4= Column(Integer)
    VB4= Column(Integer)
    C3= Column(Integer)
    IG3= Column(Integer)
    C4= Column(Integer)
    IG4= Column(Integer)