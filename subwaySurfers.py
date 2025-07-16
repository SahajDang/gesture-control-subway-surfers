import cv2
import mediapipe as mp
import keyboard as kb
import time

# Setup webcam and MediaPipe Hands
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Gesture detection logic
def get_finger_pattern(hand_landmarks):
    fingers_up = []

    # Index Finger
    fingers_up.append(hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y)
    # Middle Finger
    fingers_up.append(hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y)
    # Ring Finger
    fingers_up.append(hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y)
    # Pinky Finger
    fingers_up.append(hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y)

    return fingers_up  # [Index, Middle, Ring, Pinky]

# Variables to prevent rapid key spamming
prev_pattern = ""
action_text = ""
last_action_time = 0
cooldown = 0.2  # seconds between actions

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            pattern = get_finger_pattern(hand_landmarks)
            pattern_str = ''.join(['1' if f else '0' for f in pattern])
            current_time = time.time()

            if pattern_str != prev_pattern and current_time - last_action_time > cooldown:
                prev_pattern = pattern_str
                last_action_time = current_time

                if pattern_str == "1000":  # Only Index
                    kb.press_and_release('up')
                    action_text = "🟢 Jump"

                elif pattern_str == "1100":  # Index + Middle
                    kb.press_and_release('down')
                    action_text = "🔵 Roll"

                elif pattern_str == "1110":  # Index + Middle + Ring
                    kb.press_and_release('right')
                    action_text = "🟡 Right"

                elif pattern_str == "1111":  # All 4 fingers
                    kb.press_and_release('left')
                    action_text = "🟠 Left"

                else:
                    action_text = "👀 Unknown gesture"

    # Show detected action on screen
    if action_text:
        cv2.putText(frame, f"Detected: {action_text}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 3)

    cv2.imshow("Subway Surfers Hand Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()