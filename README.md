# ⏱️ TIME RUSH
### Think Fast. Answer Smart. Beat the Clock.

**TIME RUSH** is a Python-based, terminal quiz game developed as a first-year B.Tech Information Technology project at **Vellore Institute of Technology (VIT), Vellore**.

Inspired by popular quiz-show gameplay, TIME RUSH challenges players to test their knowledge, manage limited lifelines, and climb a progressive prize ladder while racing against the clock.

What started as a basic Python coursework assignment evolved into an interactive quiz experience featuring randomized questions, three difficulty levels, timed challenges, strategic lifelines, and an engaging terminal-based interface.

**Answer correctly. Use your lifelines wisely. Keep climbing.**

---

## 🎮 About the Game

TIME RUSH puts players through 15 questions of increasing difficulty, divided into three stages:

- **Easy:** Questions 1–5
- **Medium:** Questions 6–10
- **Hard:** Questions 11–15

Each correctly answered question takes the player one step closer to the ultimate prize of **₹1 Crore**.

Players must balance speed, accuracy, and strategy while making the most of their limited lifelines.

## ✨ Features

- **Question Bank** — A collection of 30 questions distributed across Easy, Medium, and Hard difficulty levels.
- **Randomized Gameplay** — Five questions are randomly selected from each difficulty category, with randomized answer options.
- **Countdown Timer** — Time-based challenges that add pressure to every answer.
- **Progressive Difficulty** — Three stages with increasingly challenging questions.
- **Prize Ladder** — A 15-level prize progression, culminating in ₹1 Crore.
- **Milestone Rewards** — Guaranteed winnings of ₹10,000 and ₹3,20,000 upon clearing the respective milestones.
- **Lifeline System** — Four strategic lifelines, each available once per game:
  - **50-50:** Eliminates two incorrect options.
  - **Ask the Audience:** Generates a simulated audience poll.
  - **Switch the Question:** Replaces the current question with an unused question of the same difficulty.
  - **Extra Time:** Adds 60 seconds to the active countdown.
- **Interactive Terminal UI** — Formatted questions, answer options, prize ladder, lifeline indicators, and game screens.
- **Game Progression** — Dedicated screens for correct answers, incorrect answers, timeouts, quitting, and winning.

## ⏳ Time & Difficulty System

The game uses different time limits depending on the difficulty level.

| Difficulty | Questions | Time Limit |
|---|---|---|
| Easy | 1–5 | 45 seconds |
| Medium | 6–10 | 60 seconds |
| Hard | 11–15 | Unlimited |

The Extra Time lifeline is available only during the first ten questions.

## 💰 Prize Ladder

| Question | Prize |
|---|---:|
| 1 | ₹1,000 |
| 2 | ₹2,000 |
| 3 | ₹3,000 |
| 4 | ₹5,000 |
| 5 | ₹10,000 |
| 6 | ₹20,000 |
| 7 | ₹40,000 |
| 8 | ₹80,000 |
| 9 | ₹1,60,000 |
| 10 | ₹3,20,000 |
| 11 | ₹6,40,000 |
| 12 | ₹12,50,000 |
| 13 | ₹25,00,000 |
| 14 | ₹50,00,000 |
| 15 | ₹1,00,00,000 |

**Milestone Rewards:**
- Clear Question 5 to secure ₹10,000.
- Clear Question 10 to secure ₹3,20,000.

Incorrect answers or timeouts result in the player receiving the applicable milestone reward, if achieved. Players can also quit and walk away with the prize from their last correctly answered question.

## 🛠️ Built With

- **Python 3** — Core game logic and functionality.
- **Standard Python Libraries:**
  - `random` — Question selection, option shuffling, and audience poll simulation.
  - `time` — Countdown and time-based input handling.
  - `math` — Countdown calculations.
  - `os` and `sys` — Terminal operations and platform detection.
  - `ctypes` and `msvcrt` — Windows console configuration and keyboard input.
  - `select` — Non-blocking input handling on Unix-like systems.
  - `textwrap` and `re` — Terminal text formatting.

No external Python packages are required.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A terminal or command-line interface

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/KunjTibrewal/Time-Rush.git
```

**2. Navigate to the project directory**

```bash
cd Time-Rush
```

**3. Run the game**

```bash
python game-code.py
```

Follow the on-screen instructions to start playing!

## 🎯 Project Objectives

TIME RUSH was developed to apply fundamental Python programming concepts to a practical, interactive project.

The primary objectives include:

- Applying conditional statements, loops, functions, and data structures.
- Implementing question management, answer validation, and game progression.
- Exploring randomization and time-based input handling.
- Developing interactive terminal interfaces.
- Understanding modular programming through separate functions for game mechanics and lifelines.
- Improving logical thinking, problem-solving, and collaborative development skills.

## 🗺️ Future Enhancements

Potential improvements for future iterations include:

- [ ] **Player Statistics** — Track scores, performance, and game history.
- [ ] **Multiple User Login** — Introduce individual player profiles.
- [ ] **Local Data Storage** — Save player information and statistics locally.
- [ ] **Live Timer Display** — Implement a continuously updating countdown during gameplay.
- [ ] **Enhanced User Interface** — Explore a graphical interface beyond the terminal.

*These are proposed enhancements and are not part of the current implementation.*

## 🎓 Academic Project

**Course:** First-Year B.Tech Information Technology  
**Institution:** Vellore Institute of Technology (VIT), Vellore  
**Faculty:** Jenifa G

TIME RUSH was developed as part of the first-year academic coursework and successfully presented through both project reviews.

The development process involved conceptualization, implementation, testing, debugging, and refinement of the game's core mechanics.

The central gameplay loop:

**Question → Answer → Lifeline → Progress → Prize**

## 👥 Team

Developed collaboratively as part of the first-year B.Tech Information Technology coursework at VIT Vellore.

| Team Member | GitHub |
|---|---|
| **Kunj Tibrewal** | [@KunjTibrewal](https://github.com/KunjTibrewal) |
| **Saurav Gupta** | [@sauravgupta260061](https://github.com/sauravgupta260061) |
| **Ronit Kumar** | [@Ronit-Kumar2408](https://github.com/Ronit-Kumar2408) |

## 📌 Project Status

<sub>Current Release: Final Academic Submission</sub>

TIME RUSH has completed both academic project reviews. The current implementation includes the complete core gameplay experience, featuring randomized questions, difficulty progression, timed rounds, four lifelines, milestone rewards, and terminal-based game screens.

Further improvements may be introduced in future versions.

---

### ⏱️ TIME RUSH
**Every second counts.**