import cap
import cv2
#import frame as frame
import numpy as np

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
classes = []
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

capture = cv2.VideoCapture('video1.mp4')
# img = cv2.imread('image.jpg')

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(12, 154, size=(100, 3))
count = 0
frame_no = 0
timestamp = 0

while True:
    _, img = capture.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

    net.setInput(blob)

    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []
    count = 0
    count_detection = 0
    print("for frame : " + str(frame_no) + "   timestamp is: ", str(capture.get(cv2.CAP_PROP_POS_MSEC)))
    frame_no +=1

    for output in layerOutputs:
        for detection in output:

            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                centre_x = int(detection[0] * width)
                centre_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(centre_x - w / 2)
                y = int(centre_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (225, 225, 225), 2)
            count_detection += 1
        if count_detection > count:
            count = count_detection
            timestamp = str(capture.get(cv2.CAP_PROP_POS_MSEC))
            print('obj_count:', count, 'timestamp:' + timestamp)




