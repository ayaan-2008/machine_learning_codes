<div align="center">

# Rock Paper Scissors AI

### An Adaptive Game AI That Learns Player Patterns Using Reinforcement Learning

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

[View Code](reinforced_learning.py) | [Back to Index](../README.md)

</div>

---

## Overview

**MindReader RPS AI** is a Machine Learning inspired Rock-Paper-Scissors game that learns player behavior and adapts its strategy over time. Unlike traditional games that make random choices, this AI records player moves, analyzes patterns, predicts future choices, and selects counter-moves.

---

## How It Works

```
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
```

The AI stores every move made by the player and uses frequency analysis to predict the next move.

### Example

```python
# Player move history
{
    "rock": 10,
    "paper": 4,
    "scissors": 2
}

# AI predicts: Player will choose Rock (highest frequency)
# AI plays: Paper (to counter)
```

---

## Demo

<img width="1914" height="1031" alt="image" src="https://github.com/user-attachments/assets/48b443c8-0676-47fd-953c-b20481c865a0" />


## Features

- Interactive Rock-Paper-Scissors game
- Real-time player move tracking
- Pattern recognition and prediction
- Adaptive AI strategy
- Educational ML demonstration

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| Dictionaries | Data storage |
| Pattern Analysis | Move prediction |
| Frequency-Based Prediction | Decision making |

---

## Project Structure

```
reinforced_learning/
├── README.md                     # This file
├── reinforced_learning.py        # Main code
└── requirements.txt              # Dependencies
```

---

## Installation & Usage

### Prerequisites

- Python 3.7 or higher

### Steps

```bash
# Clone the repository
git clone https://github.com/ayaan-2008/machine_learning_codes.git

# Navigate to project folder
cd machine_learning_codes/reinforced_learning

# Run the project
python reinforced_learning.py
```

---

## ML Concepts Demonstrated

| Concept | Application |
|---------|-------------|
| Training Data | Previous user moves |
| Learning | Updating move statistics |
| Model | Frequency Analysis |
| Prediction | Guessing next move |
| Inference | Selecting counter move |

---

## Future Improvements

- GUI using Tkinter
- Advanced Reinforcement Learning algorithms
- Markov Chain Prediction
- Accuracy Metrics Dashboard
- Multiplayer Support
- Web-Based Version

---

## Author

**Mohammed Abdul Ayaan**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/ayaan-2008)

---

<div align="center">

[Back to Main Index](../README.md)

</div>
