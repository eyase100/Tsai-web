
class Thinker:
    def analyze(self, context):
        if 'urgent' in context.lower():
            return "High-priority action required."
        elif 'error' in context.lower():
            return "Diagnose system faults."
        else:
            return "Proceed with normal operations."
