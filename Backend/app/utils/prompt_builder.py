def build_npc_prompt(context: str, player_input: str, npc_name: str) -> str:
    """
    Build a prompt that matches the training format exactly.
    """

    ctx = context.strip() if context else "No major events. Player is on good terms with everyone."
    player = player_input.strip()
    name = npc_name.strip()

    prompt = (
        f"<CONTEXT> {ctx}\n"
        f"<PLAYER> {player}\n"
        f"<NPC>({name}) "
    )
    return prompt
