import boto3

# A1) Mengambil gambar dari S3 storage cloud yang mengandung banyak wajah
photoSource = 'tutorial0601.jpg'
photoTarget = 'tutorial0602.jpg'

client = boto3.client('rekognition')

# A2) Mengambil response dari method untuk compare)faces yang mendeteksi gambar itu mirip atau tidak dari S3 storage cloud
response = client.compare_faces(SourceImage={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photoSource
								}}
                                , TargetImage={'S3Object' : {
								'Bucket' : 'cvbucketpens',
								'Name' : photoTarget
								}})

# A3) Melooping agar output bisa dibedakan mana yang kembar dan tidak kembar
for key, value in response.items():
    if key == ('FacesMatches', 'UnmatchedFaces'):
        print(key)
        for att in value:
            print(att)

print(response)