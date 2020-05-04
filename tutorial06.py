import boto3
import cv2
from matplotlib import pyplot as plt

# On/Off) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photoSource = 'tutorial0601.jpg'
photoTarget = 'tutorial0602.jpg'
imgSource = cv2.imread('tutorial0601.jpg')
imgTarget = cv2.imread('tutorial0602.jpg')

client = boto3.client('rekognition')

# Offline)
with open(photoSource, 'rb') as source_image_Source:
	source_bytes_Source = source_image_Source.read()

# Offline)
with open(photoTarget, 'rb') as source_image_Target:
	source_bytes_Target = source_image_Target.read()

# Offline) Mengambil response dari method compare_faces yang mendeteksi gambar dari local komputer 
response = client.compare_faces(SourceImage={'Bytes' : source_bytes_Source}, TargetImage={'Bytes' : source_bytes_Target})

# # On) Mengambil response dari method untuk compare)faces yang mendeteksi gambar itu mirip atau tidak dari S3 storage cloud
# response = client.compare_faces(SourceImage={'S3Object' : {
# 								'Bucket' : 'cvbucketpens',
# 								'Name' : photoSource
# 								}}
#                                 , TargetImage={'S3Object' : {
# 								'Bucket' : 'cvbucketpens',
# 								'Name' : photoTarget
								# }})

# # On) Melooping agar output bisa dibedakan mana yang kembar dan tidak kembar
# for key, value in response.items():
#     if key == ('FacesMatches', 'UnmatchedFaces'):
#         print(key)
#         for att in value:
#             print(att)

# Off) Menentukan lebar dan panjang foto
width_shape = imgSource.shape[1]
height_shape = imgSource.shape[0]

# Off/On) Melooping agar output bisa dibedakan 
for key, value in response.items():
	if key == 'SourceImageFace':
		i = 0
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
		cv2.rectangle(imgSource, (kiri, atas), (kiri+lebar, atas+tinggi), (255, 0, 0), 2)
		i+=1

plt.title("Terdeteksi ada " + str(i) + " Objek"), plt.xticks([]), plt.yticks([])
plt.subplot(211)
plt.imshow(cv2.cvtColor(imgSource, cv2.COLOR_BGR2RGB))

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print(response)