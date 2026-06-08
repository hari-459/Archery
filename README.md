# 🏹 Archery Game

A fast-paced 2D archery game built with Python and Pygame. Take aim, time your shot, and hit the moving target to rack up points — before you run out of lives!

---

## 🎮 Gameplay

- A **target board** moves up and down the screen at increasing speeds.
- Press **SPACE** to launch an arrow from the left side of the screen.
- Score points based on how accurately your arrow hits the target.
- Miss 3 times and it's **Game Over**.

---

## 🕹️ Controls

| Key       | Action          |
|-----------|-----------------|
| `SPACE`   | Fire arrow       |
| `R`       | Restart after Game Over |

---

## 🏆 Scoring

| Hit Zone         | Points |
|------------------|--------|
| Bullseye (center) | +9     |
| Inner ring        | +4     |
| Outer ring        | +1     |

---

## 📈 Levels

| Score Range | Level   | Target Speed |
|-------------|---------|--------------|
| 0 – 19      | Level 1 | Normal       |
| 20 – 39     | Level 2 | Faster       |
| 40+         | Level 3 | Fastest      |

---

## 📋 Features

- 3 difficulty levels with progressively faster target movement
- Score tracking: current score, previous score, and high score
- Lives system (3 lives per game)
- Background music and hit sound effects
- Restart functionality without closing the window

---

## 🛠️ Requirements

- Python 3.x
- Pygame

Install Pygame via pip:

```bash
pip install pygame
```

---

## 📁 Required Assets

Make sure the following files are in the **same directory** as `archery.py`:

| File          | Description              |
|---------------|--------------------------|
| `arrow.png`   | Arrow sprite image       |
| `aimboard.png`| Target board sprite image|
| `bgm.mp3`     | Background music         |
| `hit.mp3`     | Hit sound effect         |
| `freesansbold.ttf` | Font file           |

---

## 🚀 How to Run

```bash
python archery.py
```

---

## 📸 Screenshots

![game1](<Screenshot 2026-06-08 214129.png>) ![game2](<Screenshot 2026-06-08 214159.png>) ![game3](<Screenshot 2026-06-08 214212.png>)

---

## 📄 License

This project is open-source. Feel free to use and modify it for personal or educational purposes.
