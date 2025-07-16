# 🕹️ Gesture-Controlled Subway Surfers

Control Subway Surfers using **hand gestures** via webcam — no touch or keyboard required.  
Built using **MediaPipe**, **OpenCV**, and Python for real-time hand tracking and gesture-based input.

---

## 🎮 Features

- ✋ Real-time hand gesture recognition
- 🎯 Accurate finger pattern detection
- ⌨️ Simulates arrow key presses (`up`, `down`, `left`, `right`)
- 🧠 Compatible with GameLoop emulator version of Subway Surfers
- ⚡ Fast response with minimal lag
- 🟡 On-screen feedback with gesture labels

---

## ✋ Gesture Mappings

| Hand Gesture                    | Game Action     | Visual Feedback    |
|----------------------------------|------------------|---------------------|
| ☝️ Index finger up                | Jump             | 🟢 Jump             |
| ✌️ Index + Middle fingers         | Roll             | 🔵 Roll             |
| 🤟 Index + Middle + Ring         | Move Right       | 🟡 Right            |
| 🖖 All four fingers (except thumb) | Move Left        | 🟠 Left             |

---

## 🧠 Tech Stack

- [MediaPipe](https://google.github.io/mediapipe/) – hand tracking
- [OpenCV](https://opencv.org/) – camera input + drawing
- [keyboard](https://pypi.org/project/keyboard/) – simulate keystrokes
- Python 3.x

---

## 🚀 How to Run

1. **Clone the repo**
```bash
git clone https://github.com/SahajDang/gesture-control-subway-surfers.git
cd gesture-control-subway-surfers
```
2. **Install dependencies**
```
pip install opencv-python mediapipe keyboard
```
3. **Run the script**
   
Make sure to run as Administrator (important for key simulation)
```
python gesture_controller.py
```
4. **Start the game**

- Launch Subway Surfers in GameLoop or any emulator that supports arrow key input.

- Focus the game window and control the player using hand gestures!

## 📌 Notes
- The script must be run with admin privileges so that simulated keystrokes reach the game.

- The game window (GameLoop) must be focused to receive input.

- For smoother detection, use gestures in a well-lit environment and keep your hand within the frame.

## 📄 License
MIT License © 2025 Sahaj Dang
