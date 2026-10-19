import json
from app.models import TrainingSession
from app.utils import log_function
@log_function
def save_sessions(sessions) -> None:
    data =[]
    for session in sessions:
        data.append({
            "model": session.model,
            "epochs": session.epochs,
            "accuracy": session.accuracy
        })
    with open("sessions.json","w") as file:
        json.dump(data, file, indent=4)

def load_sessions():
    try:
        with open("sessions.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No saved sessions found.")
        return []        
    except json.JSONDecodeError:
        print("Session file contain invaild JSON.")
        return []
    sessions = []

    for item in data:
        session = TrainingSession(
            item["model"],
            item["epochs"],
            item["accuracy"]
        )
        sessions.append(session)

    return sessions