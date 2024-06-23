import cv2
import numpy as np
from keras.applications.mobilenet_v2 import preprocess_input
from keras.models import load_model

_model = load_model("hand_gesture_Model.h5")

# Map the prediction to the class label
_class_labels = [
    "Palm",
    "L",
    "Fist",
    "Fist_moved",
    "Thumb",
    "Index",
    "Ok",
    "Palm_moved",
    "C",
    "Down",
]


def detect_gesture(img_data: bytes) -> str:
    # Convertir los bytes de la imagen a un numpy array
    nparr = np.frombuffer(img_data, np.uint8)

    # Decodificar la imagen con OpenCV
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Cargar y preprocesar la imagen
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image_rgb, (224, 224))
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    # Predict the gesture
    predictions = _model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)

    gesture = _class_labels[int(predicted_class[0])]

    return gesture
    # plt.title(gesture, color="green", fontsize=16)
    # plt.imshow(image_rgb)
    # plt.axis('off')
    # plt.show()
