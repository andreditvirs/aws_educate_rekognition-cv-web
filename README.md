# aws_educate_rekognition-cv-web
AWS Rekognition dengan menggunakan akun dari AWS Educate

LANGKAH AWAL (SETUP)

1.  Buat akun dengan menggunakan AWS Educate di microsoft.pens.ac.id
2.  Daftar AWS Educate dengan mengisikan biodata jangan lupa tulis email dengan format it.student.pens.ac.id
3.  Lihat email verifikasi di student.pens.ac.id email website
4.  Verifikasi email dengan klik link email verifikasi di email student
5.  Tunggu balasan email selanjutnya selama kurang lebih 2jam - 1hari
6.  Jika sudah dapat, cari email accepted dan login ke website aws educate
7.  Akan muncul login page, setelah diketikkan email dan password ternyata masih salah, dikarenakan memang belum set password, gunakan "forget password" untuk mengatur password melalui email student
8.  Kembali ke email student dan temukan email konfirmasi forget password dari aws educate
9.  Akan diarahkan ke website aws educate atau https://labs.vocareum.com/ untuk set password dan accept aggreement
10. Jika, sudah set password, coba login ke awseducate dan akan muncul aws educate account (Workbench)
11. Copy crecidentials dari tombol "Account details", taruh ke notepad atau editor text yang lainnya
12. Install awscli 2 (recomended)
13. Buat virtual environtment dan download library "boto3" dengan pip install boto3
14. Buka explorer dan cari folder .aws di C:\Users\<nama user>\.aws contoh : C:\Users\AndreDitVirs\.aws
15. Terdapat file config dan credentials, jika belum ada, buka cmd dan jalankan perintah "aws configure"
16. Ketikkan access key, secret key, ...., sesuai dengan yang ada di step 11, jika ditanyakan region tulis : "us-east-1" dan output : "json"
17. Silahkan mengikuti tutorial yang ada di video playlist yang telah dibagikan
