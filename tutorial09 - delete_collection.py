import boto3
client = boto3.client('rekognition')
response = client.delete_collection(CollectionId="collection_photo")
print(response)