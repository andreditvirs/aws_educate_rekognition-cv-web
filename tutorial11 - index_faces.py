import boto3
import cv2
from matplotlib import pyplot as plt

client = boto3.client('rekognition')

img = cv2.imread('all.jpeg')
photo = 'all.jpeg'

# Offline)
with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

response = client.index_faces(CollectionId="collection_photo", Image={'Bytes' : source_bytes})

# Off) Menentukan lebar dan panjang foto
width_shape = img.shape[1]
height_shape = img.shape[0]

i=0
for key, value in response.items():
	if key == 'FaceRecords':
		for face in value:
			for key, value in face.items():
				if key == 'Face':
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

cv2.waitKey(0)
cv2.destroyAllWindows()

print(response)