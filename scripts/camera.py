import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("C:/Users/beren/OneDrive/Masaüstü/P4_BerentTanKÜÇÜK_2004040034/Project/models/model.keras")

class_labels = ['bench_press', 'pull_up', 'squat', 'leg_extension', 'deadlift', 'push_up', 'chest_fly_machine']

display_labels = {
    'bench_press': 'Punches',
    'pull_up': 'Superman',
    'squat': 'Squat',
    'leg_extension': 'High Knees',
    'deadlift': 'Leg Curls',
    'push_up': 'Elbow Plank',
    'chest_fly_machine': 'Chest Squeezes'
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    input_img = cv2.resize(frame, (128, 128))
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
    input_img = input_img.astype('float32') / 255.0
    input_img = np.expand_dims(input_img, axis=0)
    
    prediction = model.predict(input_img)
    class_index = np.argmax(prediction, axis=1)[0]
    class_name = class_labels[class_index]
    display_name = display_labels[class_name]
    
    cv2.putText(frame, display_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("Exercise Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
