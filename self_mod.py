
class SelfModifier:
    def __init__(self):
        self.log = []

    def modify_behavior(self, rule):
        self.log.append(rule)
        return f"Behavior modification rule applied: {rule}"

    def get_log(self):
        return self.log
