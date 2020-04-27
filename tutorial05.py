import boto3

# A1) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photo = 'tutorial0501.jpg'

client = boto3.client('rekognition')

# A2) Mengambil response dari method untuk deteksi selebriti yang mendeteksi gambar dari S3 storage cloud
response = client.recognize_celebrities(Image={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photo
								}})

# # A3) Melooping agar output bisa dibedakan, gunakan jika foto ada banyak selebriti
# for key, value in response.items():
#     if key == 'CelebrityFaces':
#         for people in value:
#             print(people)
#             print("========")

print(response)