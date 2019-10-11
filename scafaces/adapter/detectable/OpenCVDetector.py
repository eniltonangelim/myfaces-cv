from scafaces.domain.ports.Detectable import Detectable
from scafaces.domain.models.People import People
from typing import List
from os import path, environ
import cv2, imutils
import numpy as np


class OpenCVDetector(Detectable):

    def __init__(self):
        super()
        self.__protoPath = environ.get("DETECTOR_PROTO")
        self.__modelPath = environ.get("DETECTOR_MODEL")
        self.__detector = cv2.dnn.readNetFromCaffe(self.__protoPath, self.__modelPath)
        self.__people: People = People()

    def read(self):
        return self.detector

    def detector(self, images: List[str], embedder = None) -> People:
        for (i, imagePath) in enumerate(images):
            name = imagePath.split(path.sep)[-2]

            image = cv2.imread(imagePath)
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]

            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(image, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            self.__detector.setInput(imageBlob)
            detections = self.__detector.forward()

            # ensure at least one face was found
            if len(detections) > 0:
                # we're making the assumption that each image has only ONE
                # face, so find the bounding box with the largest probability
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]

                # ensure that the detection with the largest probability also
                # means our minimum probability test (thus helping filter out
                # weak detections)
                if confidence > 0.5:
                    # compute the (x, y)-coordinates of the bounding box for
                    # the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI and grab the ROI dimensions
                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI, then pass the blob
                    # through our face embedding model to obtain the 128-d
                    # quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                     (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    embedder.setInput(faceBlob)
                    vec = embedder.forward()

                    # add the name of the person + corresponding face
                    # embedding to their respective lists
                    self.__people.names.append(name)
                    self.__people.embeddings.append(vec.flatten())

        return self.__people