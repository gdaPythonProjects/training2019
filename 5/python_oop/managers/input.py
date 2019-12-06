class InputManagerWrongValue(Exception):
    pass


class Input:
    def __init__(self):
        self.a = None
        self.b = None

    def get_a_value(self):
        self.a = self.get_value_stdin("Ustaw wartość A: ")

    def get_b_value(self):
        self.b = self.get_value_stdin("Ustaw wartość B: ")

    def get_a_b_values(self):
        self.get_a_value()
        self.get_b_value()

    @staticmethod
    def get_value_stdin(message: str) -> int:
        value = input(message)
        if value.isdigit():
            return int(value)
        raise InputManagerWrongValue("Please give me int value")
