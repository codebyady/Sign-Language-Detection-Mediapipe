import os

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 5
dataset_size = 100

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_BRIGHTNESS, 50)
cap.set(cv2.CAP_PROP_CONTRAST, 50)
cap.set(cv2.CAP_PROP_SATURATION, 50)
cap.set(cv2.CAP_PROP_HUE, 50)
cap.set(cv2.CAP_PROP_GAIN, 50)
cap.set(cv2.CAP_PROP_EXPOSURE, 50)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.rectangle(frame, (20, 698), (770, 615), (0, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (25, 675), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 255, 255), 2,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
