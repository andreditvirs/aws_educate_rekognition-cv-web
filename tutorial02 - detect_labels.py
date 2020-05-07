import boto3

# # 1) Mengambil gambar dari local komputer
# photo = 'tutorial0201.jpg'

# # 2) Mengambil gambar dari S3 storage cloud
photo = 'tutorial0202.jpg'

client = boto3.client('rekognition')

with open(photo, 'rb') as source_image:
	source_bytes = source_image.read()

# # 1) Mengambil response dari method detect_labels yang mendeteksi gambar dari local komputer 
# response = client.detect_labels(Image={'Bytes' : source_bytes},
# 								MaxLabels=2,
# 								MinConfidence=95)

# 2) Mengambil response dari method detect_labels yang mendeteksi gambar dari S3 storage cloud
response = client.detect_labels(Image={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photo
								}},
								MaxLabels=2,
								MinConfidence=95)

print(response)