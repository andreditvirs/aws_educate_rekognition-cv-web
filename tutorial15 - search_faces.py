import boto3
import cv2

client = boto3.client('rekognition')

collection_id='collection_photo'
face_id='72bf2396-5adb-4792-91f1-8b930e0b2f50'

response = client.search_faces(CollectionId = collection_id, FaceId = face_id) #IDnya didapat dari tutorial14 saat list faces di collection
print(response)