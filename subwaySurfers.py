import cv2
import mediapipe as mp
import time
import os

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Webcam feed
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Gesture logic
def get_gesture(landmarks):
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

# ADB Swipe Functions
def swipe_up():
    os.system("adb shell input swipe 500 1200 500 500 200")

def swipe_down():
    os.system("adb shell input swipe 500 800 500 1300 200")

def swipe_left():
    os.system("adb shell input swipe 700 1000 200 1000 200")

def swipe_right():
    os.system("adb shell input swipe 300 1000 800 1000 200")

# Main Loop
last_action_time = time.time()
cooldown = 1  # seconds

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            landmarks = handLms.landmark
            gesture = get_gesture(landmarks)

            now = time.time()
            if gesture and now - last_action_time > cooldown:
                print(f"Gesture detected: {gesture}")
                if gesture == 'up':
                    swipe_up()
                elif gesture == 'down':
                    swipe_down()
                elif gesture == 'left':
                    swipe_left()
                elif gesture == 'right':
                    swipe_right()
                last_action_time = now

    cv2.imshow("Hand Gesture Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
