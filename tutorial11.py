import boto3
import cv2

client = boto3.client('rekognition')

img = cv2.imread('tutorial0701.jpg')
photo = 'tutorial0701.jpg'

# Offline)
with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

response = client.index_faces(CollectionId="collection_photo", Image={'Bytes' : source_bytes})
print(response)