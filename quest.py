class QuestStep:
    def __init__(self, description, character=None, item=None):
        self.description = description
        self.character = character
        self.item = item

class Quest:
    def __init__(self, name, description, steps):
        self.name = name
        self.description = description
        self.steps = steps
        self.current_step = 0

    def advance(self):
        if self.current_step < len(self.steps):
            self.current_step += 1

    def is_complete(self):
        return self.current_step >= len(self.steps)

    def get_current_step(self):
        if self.current_step < len(self.steps):
            return self.steps[self.current_step]
        return None