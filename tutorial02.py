import csv
import boto3

photo = 'test.jpg'

client = boto3.client('rekognition')

with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

response = client.detect_labels(Image={'Bytes' : source_bytes},
								MaxLabels=10)

print(response)