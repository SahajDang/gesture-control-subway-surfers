# Gesture-Controlled Subway Surfers 🎮

Control Subway Surfers using hand gestures via webcam using Python, MediaPipe, and ADB.

## 🚀 Features
- Raise your hand to **jump**
- Lower your hand to **slide**
- Swipe left/right in the air to **move left or right**
- Works with BlueStacks + ADB for in-game control

## 🛠 Tech Stack
- Python
- OpenCV
- MediaPipe
- ADB (Android Debug Bridge)

## 🧠 How It Works
- Uses MediaPipe to detect hand landmarks in real-time
- Maps gestures to game actions
- Sends swipe commands to BlueStacks via ADB

## 🖥 Setup
```bash
pip install mediapipe opencv-python

📱 Run the script
Make sure BlueStacks is running with Subway Surfers opened:
python subwaySurfers.py

💡 Notes
Make sure adb is connected to 127.0.0.1:5555 (BlueStacks)

Keep only one hand visible for best accuracy

🙌 Made with passion by Sahaj Dang

---

## ✅ Step 2: Add, Commit, and Push

After saving the `README.md`, run these commands:

```bash
git add README.md
git commit -m "Add project README"
git push
