from fastapi import APIRouter, HTTPException

router = APIRouter()

# Assuming 'fake_db' is a global variable that you have defined somewhere in your code
fake_db = [{
    "lung": "Metal",  # P
    "heart": "Fire",  # C
    "spleen": "Earth",  # RP
    "liver": "Wood",  # F
    "pericardium": "Fire",  # MC
    "kidney": "Water",  # R
    "large_intestine": "Metal",  # GI
    "small_intestine": "Fire",  # IG
    "stomach": "Earth",  # E
    "gall_bladder": "Wood",  # VB
    "triple_heater": "Fire",  # TR
    "bladder": "Water",  # V
}]

# Map organs to their elements
organ_to_element = {
    "lung": "Metal",  # P
    "heart": "Fire",  # C
    "spleen": "Earth",  # RP
    "liver": "Wood",  # F
    "pericardium": "Fire",  # MC
    "kidney": "Water",  # R
    "large_intestine": "Metal",  # GI
    "small_intestine": "Fire",  # IG
    "stomach": "Earth",  # E
    "gall_bladder": "Wood",  # VB
    "triple_heater": "Fire",  # TR
    "bladder": "Water",  # V
}

# Define the sequence of elements
element_sequence = ["Water", "Wood", "Earth", "Fire", "Metal"]


def calculate_disbalance(element1: str, element2: str) -> int:
    position1 = element_sequence.index (element1)
    position2 = element_sequence.index (element2)
    # Calculate the circular distance in the sequence
    disbalance = abs (position1 - position2)
    # Considering the circular nature of the sequence
    disbalance = min (disbalance, len (element_sequence) - disbalance)
    return disbalance


@router.post ("/disbalance")
async def get_disbalance():
    result = fake_db[0]  # Assuming we always work with the first entry for this example

    # Calculate the disbalance for each pair
    disbalances = {
        "Gi_P": calculate_disbalance (organ_to_element["large_intestine"], organ_to_element["lung"]),
        "IG_C": calculate_disbalance (organ_to_element["small_intestine"], organ_to_element["heart"]),
        "E_RP": calculate_disbalance (organ_to_element["stomach"], organ_to_element["spleen"]),
        "VB_F": calculate_disbalance (organ_to_element["gall_bladder"], organ_to_element["liver"]),
        "TR_MC": calculate_disbalance (organ_to_element["triple_heater"], organ_to_element["pericardium"]),
    }

    return disbalances
