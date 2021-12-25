import numpy as np
import cv2

import os

def extract_data(name):
	with open(name, 'a') as file:
		base = os.path.abspath('Images/')

		for file_name in os.listdir(base):
			path = os.path.join(base, file_name)
			image = cv2.imread(path, 0)
			extracted = image.reshape(1, -1)

			file.write(','.join(extracted.astype(str)[0]) + '\n')

	return 'Data extracted successfully!'

extract_data('data.csv')

