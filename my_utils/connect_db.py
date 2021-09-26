from mongoengine import connect
from milvus import Milvus
from minio import Minio
import os
from dotenv import load_dotenv
import redis
import sys

debug = True
load_dotenv()


def connect_mongo_db():
    connect(
        db=os.getenv("MONGO_DB_NAME"),
        host=os.getenv("MONGO_HOST"),
        port=int(os.getenv("MONGO_PORT")),
        username=os.getenv("MONGO_USERNAME"),
        password=os.getenv("MONGO_PASSWORD"),
        authentication_source="admin"
    )


def connect_milvus():
    milvus_client = Milvus(os.getenv("MILVUS_HOST"), int(os.getenv("MILVUS_PORT")))
    collection_name = os.getenv("collection_name")
    partition_name = os.getenv("partition_name")
    return milvus_client, collection_name, partition_name


def connect_minio():
    host = os.getenv("MINIO_HOST").split("//")[1]
    host = "{}:{}".format(host, os.getenv("MINIO_PORT"))
    bucket_name = os.getenv("MINIO_BUCKET")

    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")
    is_secure = os.getenv("MINIO_HOST").split(":")[0] == "https"

    minio_client = Minio(host, access_key=access_key, secret_key=secret_key, secure=is_secure)

    host_domain = "https://minio.core.greenlabs.ai"
    # host = ("https://" if is_secure else "http://") + host
    return minio_client, bucket_name


def connect_redis():
    # REDIS
    if os.getenv("REDIS_PASSWORD") is None:
        redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), db=0)
    else:
        redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), db=0,
                                         password=os.getenv("REDIS_PASSWORD"))
    return redis_client


if __name__ == '__main__':
    """
    MongoDB: docker-compose https://github.com/Vuong02011996/mongo_db/blob/master/docker-compose.yml
    MilvusDB: https://github.com/Vuong02011996/ai-engineer/blob/master/Database/Milvus/Milvus_0_10_6/install.sh
             http://localhost:3033/#/data/collections/clover_staging
    Minio: https://github.com/Vuong02011996/ai-engineer/blob/master/Database/Minio/docker-compose.yml
            https://minio.core.greenlabs.ai/minio/clover-staging/
    API: https://konga.core.greenlabs.ai/#!/upstreams (Vuong | 02011996)        
    """