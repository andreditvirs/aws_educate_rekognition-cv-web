import boto3
import cv2

client = boto3.client('rekognition')

collection_id='collection_photo'
face_id='2690b30d-c689-4b9e-b2fa-003e37248704'

response = client.delete_faces(CollectionId = collection_id, FaceIds = [face_id])
print(response)