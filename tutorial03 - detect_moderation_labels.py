import boto3
import cv2

photo ='tutorial0301.jpg'
img = cv2.imread('tutorial0301.jpg')

with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

client = boto3.client('rekognition')

# 2) Mengambil response dari method detect_moderation_labels yang mendeteksi gambar dari S3 storage cloud
response = client.detect_moderation_labels(Image={'Bytes' : source_bytes})

print(response)