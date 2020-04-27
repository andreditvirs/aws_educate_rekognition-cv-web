import boto3

# A1) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photo = 'tutorial0401.jpeg'

client = boto3.client('rekognition')

# A2) Mengambil response dari method detect_faces yang mendeteksi gambar dari S3 storage cloud
response = client.detect_faces(Image={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photo
								}}
                                , Attributes = ['ALL'])

# A3) Melooping agar output bisa dibedakan 
for key, value in response.items():
    if key == 'FaceDetails':
        for people_att in value:
            print(people_att)
            print("========")

print(response)