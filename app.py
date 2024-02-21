import streamlit as st
from minio import Minio

client = Minio("minio.launchpencil.f5.si",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
)

st.title('hello world!')

source_file = "requirements.txt"

# The destination bucket and filename on the MinIO server
bucket_name = "python-test-bucket"
destination_file = "my-test-file.txt"


# Upload the file, renaming it in the process
client.fput_object(
    bucket_name, destination_file, source_file,
)
print(
    source_file, "successfully uploaded as object",
    destination_file, "to bucket", bucket_name,
)