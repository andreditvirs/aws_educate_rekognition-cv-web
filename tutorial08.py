import boto3
client = boto3.client('rekognition')
response = client.create_collection(CollectionId="collection_photo")
print(response)