import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    if not success:
        print("Camera error")
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lmList = []

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if len(lmList) != 0:
                fingers = []

                # Thumb (try both directions)
                if lmList[4][0] > lmList[3][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Fingers (index to pinky)
                for id in range(1, 5):
                    if lmList[tip_ids[id]][1] < lmList[tip_ids[id] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = fingers.count(1)

                # Debug print (important)
                print("Fingers:", total_fingers)

                # Display on screen
                cv2.putText(img, f'Fingers: {total_fingers}', (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    else:
        # No hand detected
        cv2.putText(img, 'No Hand', (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
