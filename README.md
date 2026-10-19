# 🤖 AI Training Tracker

A Python-based CLI application for tracking and analyzing AI/ML model training sessions.

This project was built as a practical Python learning project to apply concepts such as **OOP, exceptions, modules, packages, JSON storage, generators, decorators, unit testing, virtual environments, Git, and GitHub**.

## 🚀 Features

* Add AI/ML training sessions
* Store:

  * Model name
  * Number of epochs
  * Accuracy
* View all training sessions
* Filter successful sessions
* Calculate average model accuracy
* Find the best-performing model
* Save training data locally using JSON
* Load saved sessions when the application starts
* Input validation with custom exceptions
* Logging using a Python decorator
* Generator for processing successful sessions
* Unit tests for analytics functionality

## 🛠️ Technologies

* **Python 3.11**
* Object-Oriented Programming
* JSON
* `unittest`
* Git
* GitHub
* Python Virtual Environment (`venv`)

## 📁 Project Structure

```text
ai-training-tracker/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── analytics.py
│   └── utils.py
│
├── tests/
│   └── test_analytics.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── sessions.json
```

> `sessions.json` is runtime data and is excluded from Git using `.gitignore`.

## 🧠 Concepts Practiced

### Object-Oriented Programming

The project uses classes such as:

```python
TrainingSession
TrainingTracker
```

The `TrainingSession` class represents an individual AI training run, while `TrainingTracker` manages multiple sessions.

### Exception Handling

The application uses:

* `try`
* `except`
* `raise`
* Custom exceptions

Example:

```python
class InvalidSessionError(Exception):
    pass
```

### JSON Storage

Training sessions are converted into JSON data so they can be saved and loaded between program executions.

### Generators

The tracker provides a generator for retrieving successful training sessions without creating another complete list in memory.

### Decorators

A logging decorator is used to track when important functions start and finish executing.

### Unit Testing

The project includes tests using Python's built-in `unittest` framework.

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/aradhybhalerao391-tech/ai-training-tracker.git
```

### 2. Enter the project

```bash
cd ai-training-tracker
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

## 🧪 Running Tests

Run:

```bash
python -m unittest discover
```

## 📋 Example

The application provides a menu similar to:

```text
==============================
      AI TRAINING TRACKER
==============================
1. Add training session
2. View all sessions
3. View successful sessions
4. Show average accuracy
5. Show best session
6. Save & Exit
```

A training session might look like:

```text
Neural Network | 20 epochs | 94.5% accuracy
```

## 🎯 Purpose

The main purpose of this project was to move from learning Python concepts individually to applying them together in a working application.

It serves as a foundation for building more advanced **AI/ML and data-processing projects**.

## 🔮 Future Improvements

Possible future versions could include:

* 📊 Training accuracy graphs
* 🐼 Pandas integration
* 🔢 NumPy-based analysis
* 📈 Training history visualization
* 🗄️ SQLite database support
* 📁 CSV dataset support
* 🧠 ML model performance comparison
* 🌐 Web dashboard
* 🔌 REST API
* 🤖 Integration with real ML training workflows

## 👨‍💻 Author

**Aradhy Bhalerao**

Student exploring **Python, Artificial Intelligence, Machine Learning, and Software Engineering**.

---

⭐ If you find this project useful, feel free to explore the code and build upon it.
