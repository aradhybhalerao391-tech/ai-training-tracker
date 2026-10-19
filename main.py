from app.models import TrainingSession, TrainingTracker, InvalidSessionError
from app.storage import save_sessions , load_sessions
from app.analytics import average_accuracy, get_best_session
session = TrainingSession("Neural Network",20, 94.5)
print(session.info())

tracker = TrainingTracker()
session1 = TrainingSession("Neutral Network",20,94.5)
session2 = TrainingSession("CNN",30,87.2)

tracker.add_session(session1)
tracker.add_session(session2)

print(len(tracker.sessions))
save_sessions(tracker.sessions)
print(load_sessions())

def show_menu():
    print("\n==============================")
    print("      AI TRAINING TRACKER")
    print("==============================")
    print("1. Add training session")
    print("2. View all sessions")
    print("3. View successful sessions")
    print("4. Show average accuracy")
    print("5. Show best session")
    print("6. Save & Exit")


tracker = TrainingTracker()

# Load previously saved sessions
loaded_sessions = load_sessions()

for session in loaded_sessions:
    tracker.add_session(session)


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            model = input("Model name: ")
            epochs = int(input("Epochs: "))
            accuracy = float(input("Accuracy: "))

            session = TrainingSession(model, epochs, accuracy)
            tracker.add_session(session)

            print("Session added!")

        except ValueError:
            print("Please enter valid numbers for epochs and accuracy.")

        except InvalidSessionError as error:
            print(f"Invalid session: {error}")
    elif choice == "2":
        if not tracker.sessions:
            print("No sessions found.")
        else:
            for session in tracker.sessions:
                print(session.info())

    elif choice == "3":
        successful = tracker.get_successful_sessions()

        if not successful:
            print("No successful sessions found.")
        else:
            for session in successful:
                print(session.info())

    elif choice == "4":
        result = average_accuracy(tracker.sessions)
        print(f"Average accuracy: {result:.2f}%")

    elif choice == "5":
        if not tracker.sessions:
            print("No sessions found.")
        else:
            best = get_best_session(tracker.sessions)
            print("Best session:")
            print(best.info())

    elif choice == "6":
        save_sessions(tracker.sessions)
        print("Sessions saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-6.")