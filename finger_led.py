import cv2
import mediapipe as mp
import serial
import time


arduino = serial.Serial('COM3', 9600)
time.sleep(2)  


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)  

finger_tips = [8, 12, 16, 20, 4]  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    finger_count = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark

        
            if landmarks[finger_tips[4]].x < landmarks[finger_tips[4] - 1].x:
                finger_count += 1

            
            for tip in finger_tips[:4]:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    finger_count += 1

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    
    if 0 <= finger_count <= 5:
        arduino.write(f"{finger_count}\n".encode())  
    cv2.putText(frame, f'Fingers: {finger_count}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
