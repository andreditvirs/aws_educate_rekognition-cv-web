import boto3

# A1) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photo = 'tutorial0701.jpg'

client = boto3.client('rekognition')

# A2) Mengambil response dari method untuk deteksi selebriti yang mendeteksi gambar dari S3 storage cloud
response = client.detect_text(Image={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photo
								}})

print(response)