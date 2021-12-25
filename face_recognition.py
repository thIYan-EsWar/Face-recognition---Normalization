import cv2
import numpy as np

def sigmoid(z):
	# 1 / (1 - exp(-z))
	return 1 / (1 + np.exp(-z))

video = cv2.VideoCapture(0)
weights = np.genfromtxt(fname = 'weights.csv', dtype = np.uint8, delimiter = ',')		# 4096x1

face_cascade = cv2.CascadeClassifier('face_cascade.xml')

f1_score = 0.92

while True:
	_, frame = video.read()
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	for x, y, w, h in face_cascade.detectMultiScale(gray_image, 1.2, 3):
		image = gray_image[y: y + h, x: x + w]
		flattened = cv2.resize(image, (64, 64)).reshape(1, -1) / 255.0					# 1x4096 * 4096x1 = 1x1

		if (accuracy := sigmoid(flattened @ weights)) >= f1_score:
			print(accuracy)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 3)

	cv2.imshow('Face Recogntion', frame)

	key = cv2.waitKey(1)
	if key == 27: break

video.release()
cv2.destroyAllWindows()




