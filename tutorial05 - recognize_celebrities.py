import boto3
import cv2
from matplotlib import pyplot as plt

# On/Off) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photo = 'tutorial0501.jpg'
img = cv2.imread('tutorial0501.jpg')

client = boto3.client('rekognition')

# Offline)
with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

# Offline) Mengambil response dari method detect_labels yang mendeteksi gambar dari local komputer 
response = client.recognize_celebrities(Image={'Bytes' : source_bytes})

# Online) Mengambil response dari method untuk deteksi selebriti yang mendeteksi gambar dari S3 storage cloud
# response = client.recognize_celebrities(Image={'S3Object' : {
# 								'Bucket' : 'cvbucketpens',
# 								'Name' : photo
# 								}})


# # Online) Melooping agar output bisa dibedakan, gunakan jika foto ada banyak selebriti
# for key, value in response.items():
#     if key == 'CelebrityFaces':
#         for people in value:
#             print(people)
#             print("========")

# Off) Menentukan lebar dan panjang foto
width_shape = img.shape[1]
height_shape = img.shape[0]

# Off/On) Melooping agar output bisa dibedakan 
for key, value in response.items():
	if key == 'CelebrityFaces':
		i = 0
		for people in value:
			for key, value in people.items():
				if key == 'Face' :
					for key, value in value.items():
						if key == 'BoundingBox' :
							for key, value in value.items():
								if key == 'Width' :
									lebar = int(value*width_shape)
								elif key == 'Height' :
									tinggi = int(value*height_shape)
								elif key == 'Left' :
									kiri = int(value*width_shape)
								elif key == 'Top' :
									atas = int(value*height_shape)
					cv2.rectangle(img, (kiri, atas), (kiri+lebar, atas+tinggi), (255, 0, 0), 2)
					i+=1

plt.title("Terdeteksi ada " + str(i) + " Objek"), plt.xticks([]), plt.yticks([])
plt.subplot(111)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# print(response)