from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

# Listar buckets
for bucket in client.list_buckets():
    print(bucket.creation_date)


# Subir
client.fput_object("pruebahugo", "agua.pdf", "downloadedData/agua.pdf")
print("Subido!")