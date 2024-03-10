from fastapi import APIRouter
from models.schemas import Star1, Star2

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