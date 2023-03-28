# Invoker class
class SimpleRemoteControl:
    def __init__(self):
        self.slot = None

    def set_command(self, command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()