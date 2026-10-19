import unittest
from app.models import TrainingSession
from app.analytics import average_accuracy

class TestAnalytics(unittest.TestCase):
    def test_average_accuracy(self):
        sessions = [
            TrainingSession("CNN",10,80),
            TrainingSession("RNN",20,100)
        ]
        result = average_accuracy(sessions)
        self.assertEqual(result,90)
if __name__ == "__main__":
    unittest.main()