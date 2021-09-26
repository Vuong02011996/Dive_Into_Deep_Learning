import numpy as np
from my_utils.milvus_dal.clover_dal import MilvusCloverDAL, milvus_client
from my_utils.minio_utils import read_url_img_minio_to_array
import cv2
import base64
import requests

# Compare L2 and angle two image.


def angle(v, w):
    return np.arccos(v.dot(w) / (np.linalg.norm(v) * np.linalg.norm(w)))


def cosine_distance(a, b, data_is_normalized=False):
    if not data_is_normalized:
        a = np.asarray(a) / np.linalg.norm(a, axis=1, keepdims=True)
        b = np.asarray(b) / np.linalg.norm(b, axis=1, keepdims=True)
    # from scipy.spatial import distance
    # dst = distance.cosine(a, b) = 1 - np.dot(a, b.T) = 1 - result_milvus.(with IP)
    return 1 - np.dot(a, b.T)


def distance_l2(a, b):
    # from scipy.spatial import distance
    # dst = distance.euclidean(a, b)
    # dst = np.sqrt(np.sum((x-y)**2)) = np.linalg.norm(a - b) = sqrt(result_milvus)(With L2)
    return np.linalg.norm(a - b)


def convert_np_array_to_base64(image):
    """

    :param image: np array image
    :return: string image base64
    """
    success, encoded_image = cv2.imencode('.png', image)
    image_face = encoded_image.tobytes()
    image_base64 = base64.b64encode(image_face).decode('ascii')
    return image_base64


def test_dot_product():
    url_avatar_match = "http://14.241.120.239:11039/clover-mytest/identities/origin_Ho%C3%A0ng%20Thi%C3%AAn%20Kim_78.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20210921%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210921T105654Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=82467066e7a89360db74b511d510c7d70b2cae0046fa1d88de804d01d06ee206"
    url_avatar = "http://14.241.120.239:11039/clover-mytest/objects/process_x_frame32_track_1.0.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20210925%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210925T075202Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=68813a0c5fdb3ce18830a0b13d50e9a47f30585acadc728741223eba561683eb"

    img_arr_1 = read_url_img_minio_to_array(url_avatar_match)
    img_arr_2 = read_url_img_minio_to_array(url_avatar)

    # print(angle(np.array([0, 1, 2]), np.array([2, 3, 4])))
    img_arr_1 = cv2.resize(img_arr_1, (112, 112), interpolation=cv2.INTER_AREA)
    img_arr_2 = cv2.resize(img_arr_2, (112, 112), interpolation=cv2.INTER_AREA)
    img_arr_1 = convert_np_array_to_base64(img_arr_1)
    img_arr_2 = convert_np_array_to_base64(img_arr_2)
    list_face_base64 = [img_arr_1, img_arr_2]
    req = {"images": {"data": list_face_base64}, "embed_only": True}
    resp = requests.post('http://localhost:18081/extract', json=req)
    data = resp.json()
    list_facial_vector_all_image = []
    for idx_face in range(len(data["data"])):
        list_facial_vector_all_image.append(data["data"][idx_face]["vec"])

    arr1 = np.array(list_facial_vector_all_image[0])
    arr2 = np.array(list_facial_vector_all_image[1])
    angle_2_image = angle(arr1, arr2)
    print("angle_2_image: ", angle_2_image)
    cosine_dis = cosine_distance(arr1, arr2, True)
    print("cosine_dis:", cosine_dis)

    l2_dist = distance_l2(arr1, arr2)
    print("l2_dist: ", l2_dist)

    from scipy.spatial import distance
    dst = distance.euclidean(arr1, arr2)
    print("l2_dist_lib: ", dst)
    dst = distance.cosine(arr1, arr2)
    print("cosin_dist_lib: ", dst)
    # print(dist(arr1, arr2))
    test_milvus_distance(list_facial_vector_all_image)


def test_milvus_distance(list_facial_vector):
    # milvus_client.drop_collection("test_distance")
    milvus_staging_dal = MilvusCloverDAL(collection="test_distance", partition="test1")
    # list_face_id = milvus_staging_dal.insert_data([list_facial_vector[0]])
    match_identity = milvus_staging_dal.search_vector([list_facial_vector[1]])
    for idx in range(len(match_identity)):
        dis = match_identity[idx]["distance"]
        print("dis milvus: ", 1 - dis)
        # print("dis milvus sqrt: ", np.sqrt(dis))


if __name__ == '__main__':
    # transpose()
    # gauss_elimination()
    test_dot_product()