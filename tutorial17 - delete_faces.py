import boto3
import cv2

client = boto3.client('rekognition')

collection_id='collection_photo'
face_id='00e7cdac-edac-442f-8c44-928f6d3778b5'

response = client.delete_faces(CollectionId = collection_id, FaceIds = [face_id])
print(response)