import os
import re

import cv2
import numpy as np

def find_count():
	file = os.listdir('Negatives/')
	number = file[-1] if file else ''
	pattern = r'\d'
	out = re.compile(pattern)
	count = int(''.join(out.findall(number))) if number else 0

	return count

def face_detection(capture, count):
	while True:
		_, frame = video.read()
		gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		key = cv2.waitKey(1)
		if key == 27: break

		if key == ord('s'): capture = not capture

		for x, y, w, h in face_cascade.detectMultiScale(gray_scale, 1.2, 4):


			if capture:
				string = 'Negatives/image_'+str(count).zfill(4)+'.jpg'
				image = cv2.resize(gray_scale[y: y + h, x: x + w], (64, 64))
				cv2.imwrite(string, image)

				count += 1

			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 3)
			cv2.imshow('Face', frame)

	video.release()
	cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('face_cascade.xml')
video = cv2.VideoCapture(0)

capture = False
count = find_count()

face_detection(capture, count)