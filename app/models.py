class TrainingSession:
    def __init__(self, model, epochs, accuracy):

        if not model:
            raise InvalidSessionError("Model name cannot be empty.")

        if epochs <= 0:
            raise InvalidSessionError("Epochs must be greater than 0.")

        if accuracy < 0 or accuracy > 100:
            raise InvalidSessionError("Accuracy must be between 0 and 100.")

        self.model = model
        self.epochs = epochs
        self.accuracy = accuracy

    def __repr__(self):
        return f"TrainingSession(model='{self.model}', epochs={self.epochs}, accuracy={self.accuracy})"

    def info(self):
        return f"{self.model} | {self.epochs} epochs | {self.accuracy}% accuracy"

    def is_successful(self):
        return self.accuracy >= 90
class TrainingTracker:
    def __init__(self):
        self.sessions =[]
    def add_session(self, session: TrainingSession) -> None:
        self.sessions.append(session)
    def get_successful_sessions(self) -> list[TrainingSession]:
        return [i for i in self.sessions if i.accuracy>=90]
    def successful_sessions(self):
        for session in self.sessions:
            if session.accuracy >= 90:
                yield session
class InvalidSessionError(Exception):
    pass                