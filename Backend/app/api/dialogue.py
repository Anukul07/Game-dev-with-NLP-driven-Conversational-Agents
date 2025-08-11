from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.sentiment import detect_rudeness, detect_apology
from app.models.world_state import update_world_state, get_context_for_npc, get_global_context
from app.utils.prompt_builder import build_npc_prompt
from app.nlp.generator import generate_npc_reply

router = APIRouter()

class DialogueRequest(BaseModel):
    player_input: str
    npc_name: str

@router.post("/npc_dialogue")
def npc_dialogue(request: DialogueRequest):
    player_input = request.player_input
    npc_name = request.npc_name.strip()
    print(f"[REQUEST] NPC={npc_name} | Player='{player_input}'")

    rude = detect_rudeness(player_input)
    apology = detect_apology(player_input)
    update_world_state(player_input, npc_name, rude, apology)

    npc_context = get_context_for_npc(npc_name)
    global_context = get_global_context(10)
    full_context = npc_context if not global_context else f"{npc_context} {global_context}"

    prompt = build_npc_prompt(full_context, player_input, npc_name)
    npc_response = generate_npc_reply(prompt)
    print(f"[REPLY] {npc_response}")

    return {"npc_response": npc_response}
