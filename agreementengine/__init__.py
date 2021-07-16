class AgreementPath:
    def __init__(self) -> None:
        self.states = [
            Registration()
        ]


class State:
    def __init__(self):
        pass

    def begin(self):
        pass

    def end(self):
        pass

class Registration(State):
    def __init__(self):
        super().__init__()

class NDARegistration(Registration):
    def __init__(self):
        super().__init__()

new_state = State()

State.begin(new_state)
