# 🧠 MindReader-RPS-AI

A Machine Learning inspired Rock-Paper-Scissors game that learns player behavior and adapts its strategy over time.

---

## 📌 Overview

Unlike traditional Rock-Paper-Scissors games that make random choices, this project records player moves, analyzes patterns, predicts future choices, and selects counter-moves accordingly.

The project demonstrates fundamental Machine Learning concepts such as:

- Data Collection
- Pattern Recognition
- Prediction
- Adaptive Decision Making
- Model Updating

---

## 🎯 Project Objectives

- Build an interactive Rock-Paper-Scissors game.
- Collect player move history.
- Predict future player moves.
- Demonstrate machine learning principles.
- Create a simple adaptive AI.

---

## ⚙️ Technologies Used

- Python 3
- Dictionaries
- Pattern Analysis
- Frequency-Based Prediction

---

## 🏗️ System Architecture

User Input
↓
Data Collection
↓
Learning Model
↓
Prediction Engine
↓
Counter Move Selection
↓
Result Display
↓
Model Update

---

## 🧠 How the AI Learns

The AI stores every move made by the player.

Example:

```python
{
    "rock": 10,
    "paper": 4,
    "scissors": 2
}
```

The most frequent move is predicted as the player's next choice.

If:

```python
rock = highest frequency
```

The AI predicts:

```python
Player will choose Rock
```

and plays:

```python
Paper
```

to counter it.

---

## 📊 Machine Learning Concepts Demonstrated

| Concept | Application |
|----------|-------------|
| Training Data | Previous user moves |
| Learning | Updating move statistics |
| Model | Frequency Analysis |
| Prediction | Guessing next move |
| Inference | Selecting counter move |

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/ayaan-2008/MindReader-RPS-AI.git
```

Navigate into the folder:

```bash
cd MindReader-RPS-AI
```

Run:

```bash
python reinforced_learning.py
```

---

## 📈 Future Improvements

- GUI using Tkinter
- Reinforcement Learning
- Markov Chain Prediction
- Accuracy Metrics Dashboard
- Multiplayer Support
- Web-Based Version

---

## 📚 Documentation

Detailed project documentation is included in:

```
documentation/
```

---

## 👨‍💻 Author

**Abdul Ayaan**

GitHub:
https://github.com/ayaan-2008

---

## ⭐ Project Highlights

- Interactive AI game
- Beginner-friendly ML concepts
- Real-time learning
- Pattern-based prediction
- Educational machine learning demonstration
