
def average_accuracy(sessions):
    if len(sessions) != 0:
        accuracies = [session.accuracy for session in sessions]
        return sum(accuracies)/len(accuracies)
    else:
        return 0.0

def get_best_session(sessions):
    return max(sessions, key=lambda session:session.accuracy)
