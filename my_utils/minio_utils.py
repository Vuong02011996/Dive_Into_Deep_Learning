import io
from io import BytesIO
from PIL import Image
import cv2
import requests
import numpy as np
from my_utils.connect_db import connect_minio

minio_client, bucket_name = connect_minio()


def upload_image(image, bucket=bucket_name, folder_name="group", image_name="test1"):
    """
    Upload image into MinIO Server. Parse the path of image and upload to
    server.
    :param image: numpy array
    :param bucket: bucket name in minio
    :param folder_name: folder in bucket
    :param image_name:
    :param mode_rgb:
    :return:
    """
    # img_name = "{}/{}.jpg".format(folder_name, generate_rand_string(30))
    img_name = "{}/{}.jpeg".format(folder_name, image_name)

    # Make  bucket if not exist.
    found = minio_client.bucket_exists(bucket)
    if not found:
        minio_client.make_bucket(bucket)
    try:
        image = Image.fromarray(image)

        out_img = io.BytesIO()

        image.save(out_img, quality=100, format="jpeg")
        out_img.seek(0)

        minio_client.put_object(
            bucket, img_name, out_img, length=out_img.getbuffer().nbytes, content_type="image/jpeg",
        )

    except Exception as error:
        print(error)
        return
    # url_image = "{}/{}/{}".format(host_domain, bucket, img_name)
    url = minio_client.presigned_get_object(bucket, img_name)
    return url


def read_url_img_minio_to_array(url):
    response = requests.get(url)
    img_base64 = Image.open(BytesIO(response.content))
    # if the image mode is not RGB, convert it
    if img_base64.mode != "RGB":
        img_base64 = img_base64.convert("RGB")
    img_arr = np.array(img_base64)
    # cv2.imwrite("/home/vuong/Desktop/Project/MyGitHub/ai-engineer/Database/Minio/test2.png", img_array)
    return img_arr


def read_stream_img(url, timeout=0.6):
    """
    :param url: url in minio
    :param timeout:
    :return: numpy array
    """
    i = 0
    response = None
    while i < 5:
        try:
            i += 1
            response = requests.get(url, timeout=timeout)
        except Exception as e:
            print(e)
            print("Error read_stream_img")

        if response is not None:
            break

    if response is None:
        return response

    return np.array(Image.open(io.BytesIO(response.content)))


def image_array_from_object_name(bucket="clover", object_name="/group/test1.jpg"):
    data = minio_client.get_object(bucket_name=bucket, object_name=object_name)
    img_base64 = Image.open(BytesIO(data.data))
    # if the image mode is not RGB, convert it
    if img_base64.mode != "RGB":
        img_base64 = img_base64.convert("RGB")
    img_arr = np.array(img_base64)
    # cv2.imwrite("/home/vuong/Desktop/Project/MyGitHub/ai-engineer/Database/Minio/test.png", img_array)
    return img_arr


def delete_folder(bucket_name, folder_name):
    # Delete using "remove_object"
    objects_to_delete = minio_client.list_objects(bucket_name, prefix=folder_name, recursive=True)
    for obj in objects_to_delete:
        minio_client.remove_object(bucket_name, obj.object_name.replace("+", " "))


def get_info_minio(bucket_name, folder_name):
    objects_info = minio_client.list_objects(bucket_name, prefix=folder_name, recursive=True)
    for obj in objects_info:
        result = minio_client.stat_object(bucket_name, obj.object_name)
        print(
            "last-modified: {0}, size: {1}".format(
                result.last_modified, result.size,
            ),
        )


if __name__ == '__main__':
    # img = cv2.imread("/home/vuong/Downloads/Flow AI.png")
    # url_image = upload_image(img)
    # # url_image = "https://minio.core.greenlabs.ai/local/processed3.jpeg"
    # print(url_image)
    # img_array = read_url_img_minio_to_array(url_image)
    # print(img_array)
    delete_folder(bucket_name="local", folder_name="Clover_anh_vung_an_toan")
    # get_info_minio(bucket_name="local", folder_name="clover")