import boto3
import cv2

client = boto3.client('rekognition')

collection_id='collection_photo'
face_id='2690b30d-c689-4b9e-b2fa-003e37248704'

response = client.search_faces(CollectionId = collection_id, FaceId = face_id) #IDnya didapat dari tutorial14 saat list faces di collection
print(response)