import cv2
import mediapipe as mp
import time
import os

# ========== Constants ==========
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
COOLDOWN = 0.8  # seconds

# ADB Swipe Coordinates (x1, y1, x2, y2, duration)
SWIPES = {
    'up':    "adb shell input swipe 500 1200 500 500 200",
    'down':  "adb shell input swipe 500 800 500 1300 200",
    'left':  "adb shell input swipe 700 1000 200 1000 200",
    'right': "adb shell input swipe 300 1000 800 1000 200"
}

# ========== MediaPipe Setup ==========
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# ========== Utility Functions ==========
def adb_connected():
    result = os.popen("adb get-state").read()
    return "device" in result

def perform_swipe(direction):
    if adb_connected():
        print(f"Performing swipe: {direction}")
        os.system(SWIPES[direction])
    else:
        print("⚠ ADB device not connected.")

def fingers_up(landmarks):
    finger_tips = [8, 12, 16, 20]  # Index to pinky
    fingers = []
    for tip in finger_tips:
        # Compare tip.y and pip.y (tip-2)
        fingers.append(landmarks[tip].y < landmarks[tip - 2].y)
    return fingers

def get_gesture(landmarks):
    fingers = fingers_up(landmarks)
    if fingers == [True, False, False, False]:  # Only index finger up
        wrist = landmarks[0]
        index_tip = landmarks[8]
        x_diff = index_tip.x - wrist.x
        y_diff = index_tip.y - wrist.y

        if y_diff < -0.2:
            return 'up'
        elif y_diff > 0.2:
            return 'down'
        elif x_diff < -0.2:
            return 'left'
        elif x_diff > 0.2:
            return 'right'
    return None

# ========== Main Function ==========
def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    last_action_time = time.time()
    last_gesture = None

    while True:
        success, img = cap.read()
        if not success:
            print("❌ Failed to grab frame")
            break

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
                landmarks = handLms.landmark
                gesture = get_gesture(landmarks)

                now = time.time()
                if gesture and (gesture != last_gesture or now - last_action_time > COOLDOWN):
                    print(f"Gesture detected: {gesture}")
                    perform_swipe(gesture)
                    last_action_time = now
                    last_gesture = gesture

                # Show gesture text
                if gesture:
                    cv2.putText(img, f'Gesture: {gesture}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 255, 0), 3, cv2.LINE_AA)

        cv2.imshow("🖐 Hand Gesture Controller", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ========== Run ==========
if _name_ == "_main_":
    main()