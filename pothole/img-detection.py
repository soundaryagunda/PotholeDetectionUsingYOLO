import cv2
import numpy as np

net = cv2.dnn.readNet('yolov4.weights','yolo_416.cfg') #yolov4-custom_best validation No:2
classes = []

with open('damage.names','r') as f: 
    classes = f.read().splitlines()
img = cv2.imread('hjk1.jpeg')

height , width , _ = img.shape
# With this part we can open image
blob = cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),swapRB=True,crop= False)
net.setInput(blob)
output_layers_names = net.getUnconnectedOutLayersNames()
layerOutPuts = net.forward(output_layers_names)

boxes = []
confidences = []
class_ids = []

for output in layerOutPuts:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w/2)
            y = int (center_y - h/2)

            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)


# Print how many object is detected
print(len(boxes))

indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
#print(indexes.flatten())
# Now we need to show more information in a picture

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0,255, size = (len(boxes),3) )
# Loop for all object detected
if len(indexes) > 0:
    for i in indexes.flatten():
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i],2))
        color = colors[i]
        cv2.rectangle(img, (x,y),(x+w,y+h),color,2)
        cv2.putText(img,label+" "+ confidence,(x,y+20),font,2,(255,255,255),2)


cv2.imshow('image',img)
cv2.imwrite("C:\\Users\\HP\\OneDrive\\Desktop\\pothole\\output\\image.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
