""" This module contains the Quest and QuestStep classes. """

class QuestStep:
    """ This class represents a step in a quest. """
    def __init__(self, description, character=None, item=None,
                 special_responses=None, choices=None, correct_choices=None, reward_item=None):
        self.description = description
        self.character = character
        self.item = item
        self.special_responses = special_responses or []
        self.choices = choices or []
        self.correct_choices = correct_choices or []
        self.reward_item = reward_item
        self.current_substep = 0

    def advance_substep(self):
        """ Advance to the next substep. """
        if self.current_substep < len(self.special_responses) - 1:
            self.current_substep += 1
            return False
        return True

    def reset_substep(self):
        """ Reset the substep to the beginning. """
        self.current_substep = 0

    def get_current_response(self):
        """ 
        Get the current special response for this substep.
        Returns:
            str: The special response for this substep.
        """
        if self.current_substep < len(self.special_responses):
            return self.special_responses[self.current_substep]
        return None

    def get_current_choices(self):
        """
        Get the current choices for this substep.
        Returns:
            list: The choices for this substep.
        """
        if self.current_substep < len(self.choices):
            return self.choices[self.current_substep]
        return None

    def get_current_correct_choices(self):
        """
        Get the current correct choices for this substep.
        Returns:
            list: The correct choices for this substep.
        """
        if self.current_substep < len(self.correct_choices):
            return self.correct_choices[self.current_substep]
        return None

class Quest:
    """ This class represents a quest in the game. """
    def __init__(self, name, description, steps):
        self.name = name
        self.description = description
        self.steps = steps
        self.current_step = 0

    def advance(self):
        """ Advance to the next step in the quest. """
        if self.current_step < len(self.steps):
            self.current_step += 1

    def is_complete(self):
        """
        Check if the quest is complete.
        Returns:
            bool: True if the quest is complete, False otherwise.
        """
        return self.current_step >= len(self.steps)

    def get_current_step(self):
        """
        Get the current step of the quest.
        Returns:
            QuestStep: The current step of the quest.
        """
        if self.current_step < len(self.steps):
            return self.steps[self.current_step]
        return None
