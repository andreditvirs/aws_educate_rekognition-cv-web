import boto3

# 1) Mengambil gambar dari S3 storage cloud
photo = 'tutorial0301.jpg'

client = boto3.client('rekognition')

# 2) Mengambil response dari method detect_moderation_labels yang mendeteksi gambar dari S3 storage cloud
response = client.detect_moderation_labels(Image={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photo
								}})

print(response)