import boto3
import cv2

client = boto3.client('rekognition')

img = cv2.imread('tutorial0701.jpg')
photo = 'tutorial0701.jpg'

# Offline)
with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

collection_id='collection_photo'

response = client.search_faces_by_image(CollectionId = collection_id, Image = {'Bytes' : source_bytes})
print(response)