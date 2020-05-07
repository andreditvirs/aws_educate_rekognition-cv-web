import boto3
import cv2
from matplotlib import pyplot as plt

client = boto3.client('rekognition')

imgSource = cv2.imread('one.jpg')
photoSource = 'one.jpg'

imgTarget = cv2.imread('all.jpeg')
photoTarget = 'all.jpeg'

# Offline)
with open(photoSource, 'rb') as source_image:
	source_bytes_Source = source_image.read()

# Offline)
with open(photoTarget, 'rb') as source_image:
	source_bytes_Target = source_image.read()

collection_id='collection_photo'

response = client.search_faces_by_image(CollectionId = collection_id, Image = {'Bytes' : source_bytes_Source})

width_shape_Source = imgSource.shape[1]
height_shape_Source = imgSource.shape[0]

i=0

for key, value in response.items():
	if key == 'SearchedFaceBoundingBox':
		lebar = int(value['Width']*width_shape_Source)
		tinggi = int(value['Height']*height_shape_Source)
		kiri = int(value['Left']*width_shape_Source)
		atas = int(value['Top']*height_shape_Source)
	i+=1
cv2.rectangle(imgSource, (kiri, atas), (kiri+lebar, atas+tinggi), (255, 0, 0), 2)

plt.title("Terdeteksi ada " + str(i) + " Objek"), plt.xticks([]), plt.yticks([])
plt.subplot(121)
plt.imshow(cv2.cvtColor(imgSource, cv2.COLOR_BGR2RGB))

width_shape_Target = imgTarget.shape[1]
height_shape_Target = imgTarget.shape[0]

i=0
for key, value in response.items():
	if key == 'FaceMatches':
		for face_matches in value:
			for key, value in face_matches.items():
				if key == 'Face':
					for key, value in value.items():
						if key == 'BoundingBox':
							lebar = int(value['Width']*width_shape_Target)
							tinggi = int(value['Height']*height_shape_Target)
							kiri = int(value['Left']*width_shape_Target)
							atas = int(value['Top']*height_shape_Target)
					cv2.rectangle(imgTarget, (kiri, atas), (kiri+lebar, atas+tinggi), (255, 0, 0), 2)
					i+=1

plt.title("Terdeteksi ada " + str(i) + " Objek"), plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(cv2.cvtColor(imgTarget, cv2.COLOR_BGR2RGB))

plt.show()

print(response)