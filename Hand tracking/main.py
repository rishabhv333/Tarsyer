import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('out.mp4', -1, 20.0, (640, 480))
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    # checking whether a hand is detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 3:
                    thumb_low = [cy]
                    Tl = thumb_low[-1]

                if id == 4:
                    thumb = [cy]
                    T = thumb[-1]
                    if T < Tl - 25:
                        S = 'T'
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale=1, color=(1, 0, 0))

                if id == 8:
                    index = [cy]
                    I = index[-1]
                    if I < Il:
                        S = 'I'
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale=1, color=(1, 0, 0))

                if id == 7:
                    index_low = [cy]
                    Il = index_low[-1]

                if id == 12:
                    middle = [cy]
                    M = middle[-1]
                    if M < Ml:
                        S = 'M'
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale=1, color=(1, 0, 0))

                if id == 11:
                    middle_low = [cy]
                    Ml = middle_low[-1]

                if id == 16:
                    Ring = [cy]
                    R = Ring[-1]
                    if R < Rl:
                        S = 'R'
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale=1, color=(1, 0, 0))

                if id == 15:
                    Ring_low = [cy]
                    Rl = Ring_low[-1]

                if id == 19:
                    baby_low = [cy]
                    Bl = baby_low[-1]

                if id == 20:
                    baby = [cy]
                    B = baby[-1]
                    if B < Bl:
                        S = 'B'
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                        cv2.putText(image, S, (cx, cy), fontFace=3, fontScale=1, color=(1, 0, 0))
        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Output", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
