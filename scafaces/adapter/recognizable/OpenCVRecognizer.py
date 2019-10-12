from scafaces.domain.ports.Recognizable import Recognizable
from os import environ
import cv2
import pickle
import imutils
import numpy as np


class OpenCVRecognizer(Recognizable):

    def __init__(self):
        self.__labelEncoder = environ.get("LABEL_OUTPUT")
        self.__recognizer = environ.get("RECOGNIZER_OUTPUT")
        self.__protoPath = environ.get("DETECTOR_PROTO")
        self.__modelPath = environ.get("DETECTOR_MODEL")

    def identify(self, embedder=None, image=None):

        detector = cv2.dnn.readNetFromCaffe(self.__protoPath, self.__modelPath)
        recognizer = pickle.loads(open(self.__recognizer, "rb").read())
        labelEncoder = pickle.loads(open(self.__labelEncoder, "rb").read())

        image = cv2.imread(image)
        image = imutils.resize(image, width=600)
        (h, w) = image.shape[:2]

        imageBlob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300),
                                          (104.0, 177.0, 123.0), swapRB=False, crop=False)

        print(detector)

        detector.setInput(imageBlob)
        detections = detector.forward()

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.8:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                face = image[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                if fW < 20 or fH < 20:
                    continue

                faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
                                                 (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput(faceBlob)
                vec = embedder.forward()

                preds = recognizer.predict_proba(vec)[0]
                j = np.argmax(preds)
                proba = preds[j]
                name = labelEncoder.classes_[j]

                text = "{}: {:.2f}%".format(name, proba * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(image, (startX, startY), (endX, endY),
                              (0, 0, 255), 2)
                cv2.putText(image, text, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)