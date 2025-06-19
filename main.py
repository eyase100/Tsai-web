
from modules.planner import Planner
from modules.thinker import Thinker
from modules.self_mod import SelfModifier

planner = Planner()
thinker = Thinker()
modifier = SelfModifier()

def interact(input_text):
    if input_text.startswith("plan:"):
        return planner.add_task(input_text[5:].strip())
    elif input_text.startswith("think:"):
        return thinker.analyze(input_text[6:].strip())
    elif input_text.startswith("mod:"):
        return modifier.modify_behavior(input_text[4:].strip())
    elif input_text.strip() == "tasks":
        return planner.get_tasks()
    elif input_text.strip() == "modlog":
        return modifier.get_log()
    elif input_text.strip() == "clear":
        return planner.clear_tasks()
    else:
        return "Command not recognized."
