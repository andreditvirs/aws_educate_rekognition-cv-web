import boto3
import cv2
from matplotlib import pyplot as plt

# On/Off) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photo = 'tutorial0701.jpg'
img = cv2.imread('tutorial0701.jpg')

client = boto3.client('rekognition')

# Offline)
with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

# Offline) Mengambil response dari method untuk deteksi teks
response = client.detect_text(Image={'Bytes' : source_bytes})

width_shape = img.shape[1]
height_shape = img.shape[0]

for key, value in response.items():
	i=0
	if key == 'TextDetections':
		for teks in value:
			for key, value in teks.items():
				if key == 'Geometry':
					for key, value in value.items():
						if key == 'BoundingBox':
							lebar = int(value['Width']*width_shape)
							tinggi = int(value['Height']*height_shape)
							kiri = int(value['Left']*width_shape)
							atas = int(value['Top']*height_shape)
					cv2.rectangle(img, (kiri, atas), (kiri+lebar, atas+tinggi), (255, 0, 0), 2)
					i+=1

plt.title("Terdeteksi ada " + str(i) + " Objek"), plt.xticks([]), plt.yticks([])
plt.subplot(111)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()
print(response)