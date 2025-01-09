class QuestStep:
    def __init__(self, description, character=None, item=None, special_responses=None, choices=None, correct_choices=None, reward_item=None):
        self.description = description
        self.character = character
        self.item = item
        self.special_responses = special_responses or []
        self.choices = choices or []
        self.correct_choices = correct_choices or []
        self.reward_item = reward_item
        self.current_substep = 0

    def advance_substep(self):
        if self.current_substep < len(self.special_responses) - 1:
            self.current_substep += 1
            return False
        return True

    def reset_substep(self):
        self.current_substep = 0

    def get_current_response(self):
        if self.current_substep < len(self.special_responses):
            return self.special_responses[self.current_substep]
        return None

    def get_current_choices(self):
        if self.current_substep < len(self.choices):
            return self.choices[self.current_substep]
        return None

    def get_current_correct_choices(self):
        if self.current_substep < len(self.correct_choices):
            return self.correct_choices[self.current_substep]
        return None

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