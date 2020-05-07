import boto3
import cv2

client = boto3.client('rekognition')

response = client.get_celebrity_info(Id = 'mm7At2u') #IDnya mark zuckerberg dari method recognize_celebrities

print(response)