import streamlit as st
from minio import Minio
import os, uuid, qrcode, io

client = Minio(
    "minio.launchpencil.f5.si",
    access_key=os.environ.get("accesskey"),
    secret_key=os.environ.get("secretkey"),
)

st.title('QRdrop v1.0')
st.caption("選択されたファイルからQRコードを生成します。")

source_file = st.file_uploader("共有したいファイルを洗濯してください")
bucket_name = "qrdrop"

if source_file is not None:
    with st.spinner('QRコードを生成しています…'):
        st.info(source_file.name)

        destination_file = str(uuid.uuid4()) + source_file.name
        client.put_object(
            bucket_name, destination_file, source_file,length=-1, part_size=1024*1024*100
        )
        image_url = "https://minio.launchpencil.f5.si/qrdrop/" + destination_file
        print("saved as " + image_url)

        qr = qrcode.make(image_url)

        image_bytes = io.BytesIO()
        qr.save(image_bytes, format='JPEG')
        st.image(image_bytes)
        st.info("QRコードの生成が完了しました！")