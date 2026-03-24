import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Start camera
cap = cv2.VideoCapture(0)

# Finger tip IDs
tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    # Flip image for natural interaction
    img = cv2.flip(img, 1)

    # Convert to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process hand
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            # Draw landmarks
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lmList = []

            # Get landmark positions
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if len(lmList) != 0:
                fingers = []

                # Thumb (x-axis comparison)
                if lmList[tip_ids[0]][0] > lmList[tip_ids[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Other 4 fingers (y-axis comparison)
                for id in range(1, 5):
                    if lmList[tip_ids[id]][1] < lmList[tip_ids[id] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = fingers.count(1)

                # Display count
                cv2.putText(img, f'Fingers: {total_fingers}', (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Show window
    cv2.imshow("Gesture Control", img)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
