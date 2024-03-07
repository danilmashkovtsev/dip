from fastapi import APIRouter
from pydantic import BaseModel
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

star = APIRouter()

@star.post("/star1")
async def get_values(data: Star1):
    lung = data.P1 + data.P2 + data.P3 + data.P4
    spleen = data.RP1 + data.RP2 + data.RP3
    kidney = data.R1 + data.R2 + data.R3
    thelargeintestine = data.Gi1 + data.Gi2 + data.Gi3 + data.Gi4
    stomach = data.E1 + data.E2
    gallbladder = data.VB1 + data.VB2 + data.VB3
    bladder = data.V1 + data.V2 + data.V3
    hearth = data.C1 + data.C2 + data.C3 + data.C4
    liver = data.F1 + data.F2 + data.F3
    thesmallintestine = data.IG1 + data.IG2 + data.IG3 + data.IG4

    return {
        "lung ": lung,
        "spleen": spleen,
        "kidney": kidney,
        "thelargeintestine": thelargeintestine,
        "stomach": stomach,
        "gallbladder": gallbladder,
        "bladder": bladder,
        "hearth": hearth,
        "liver": liver,
        "thesmallintestine": thesmallintestine,
        "message": "Results saved successfully"
    }

@star.post("/star2")
async def get_values(data: Star2):
    pericardium = data.MC1 + data.MC2 + data.MC3 + data.MC4
    TR = data.TR1 + data.TR2 + data.TR3 + data.TR4 + data.TR5
    kidney = data.R + data.RP
    thelargeintestine = data.Gi
    stomach = data.E
    gallbladder = data.VB
    bladder = data.V
    hearth = data.C
    liver = data.F
    thesmallintestine = data.IG

    return {
        "pericardium": pericardium,
        "TR": TR,
        "kidney": kidney,
        "thelargeintestine": thelargeintestine,
        "stomach": stomach,
        "gallbladder": gallbladder,
        "bladder": bladder,
        "hearth": hearth,
        "liver": liver,
        "thesmallintestine": thesmallintestine,
        "message": "Results saved successfully"
    }