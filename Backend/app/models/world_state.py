from collections import defaultdict, deque

MAX_RUMORS_PER_NPC = 8
MAX_GLOBAL_EVENTS = 50

class WorldState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.npc_status = defaultdict(lambda: {
            'rude': False,
            'apology': False,
            'rumors': deque(maxlen=MAX_RUMORS_PER_NPC),
        })
        self.global_events = deque(maxlen=MAX_GLOBAL_EVENTS)

    def update(self, npc_name, rude=False, apology=False):
        _ = self.npc_status[npc_name]  # ensure exists

        if rude:
            self.npc_status[npc_name]['rude'] = True
            evt = f"Player was rude to {npc_name}."
            self.global_events.append(evt)
            self.spread_rumor(evt, exclude=[npc_name])

        if apology:
            self.npc_status[npc_name]['apology'] = True
            self.npc_status[npc_name]['rude'] = False
            evt = f"Player apologized to {npc_name}."
            self.global_events.append(evt)
            self.spread_rumor(evt, exclude=[npc_name])

    def spread_rumor(self, rumor, exclude=None):
        exclude = exclude or []
        for npc in self.npc_status:
            if npc not in exclude:
                self.npc_status[npc]['rumors'].append(rumor)

    def get_context_for_npc(self, npc_name):
        status = self.npc_status[npc_name]
        ctx = []
        if status['rude']:
            ctx.append(f"The player was recently rude to {npc_name}.")
        if status['apology']:
            ctx.append(f"The player apologized to {npc_name} and was forgiven.")
        if status['rumors']:
            ctx.append("Rumors in the village: " + " ".join(status['rumors']))
        if not ctx:
            ctx = [f"The player is on good terms with {npc_name}."]
        return " ".join(ctx)

    def print_state(self):
        print("Current world state:")
        for npc, status in self.npc_status.items():
            print(f"  {npc}: rude={status['rude']} apology={status['apology']} rumors={list(status['rumors'])}")


world_state = WorldState()

def update_world_state(player_input, npc_name, rude=False, apology=False):
    world_state.update(npc_name, rude, apology)

def get_context_for_npc(npc_name):
    return world_state.get_context_for_npc(npc_name)

def get_global_context(num_events=10):
    if not world_state.global_events:
        return ""
    tail = list(world_state.global_events)[-num_events:]
    return "Recent events: " + " ".join(tail)

def reset_world_state():
    world_state.reset()

def debug_print_state():
    world_state.print_state()
