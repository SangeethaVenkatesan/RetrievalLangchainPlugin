import os

from dotenv import load_dotenv

load_dotenv()


class AppConfig:
    def __init__(self):
        self.bearer_token = os.getenv('BEARER_TOKEN')
        self.app_id = os.getenv('APP_ID')
        self.app_secret = os.getenv('APP_SECRET')


class EmbeddingsConfig:
    def __init__(self):
        self.cohere_api_key = os.getenv('COHERE_API_KEY')
        self.open_api_key = os.getenv('OPEN_API_KEY')
        self.hugging_face_private_key = os.getenv('HUGGING_FACE_PRIVATE_KEY')


class VectorDBConfig:
    def __init__(self, datastore):
        self.datastore = datastore


class PineconeConfig(VectorDBConfig):
    def __init__(self):
        super().__init__('pinecone')
        self.pinecone_api_key = os.getenv('PINECONE_API_KEY')
        self.pinecone_environment = os.getenv('PINECONE_ENVIRONMENT')
        self.pinecone_index = os.getenv('PINECONE_INDEX')


class WeaviateConfig(VectorDBConfig):
    def __init__(self):
        super().__init__('weaviate')
        self.weaviate_host = os.getenv('WEAVIATE_HOST')
        self.weaviate_port = os.getenv('WEAVIATE_PORT')
        self.weaviate_index = os.getenv('WEAVIATE_INDEX')
        self.weaviate_username = os.getenv('WEAVIATE_USERNAME')
        self.weaviate_password = os.getenv('WEAVIATE_PASSWORD')
        self.weaviate_scopes = os.getenv('WEAVIATE_SCOPES')
        self.weaviate_batch_size = os.getenv('WEAVIATE_BATCH_SIZE')
        self.weaviate_batch_dynamic = os.getenv('WEAVIATE_BATCH_DYNAMIC')
        self.weaviate_batch_timeout_retries = os.getenv('WEAVIATE_BATCH_TIMEOUT_RETRIES')
        self.weaviate_batch_num_workers = os.getenv('WEAVIATE_BATCH_NUM_WORKERS')


class ZillizConfig(VectorDBConfig):
    def __init__(self):
        super().__init__('zilliz')
        self.zilliz_collection = os.getenv('ZILLIZ_COLLECTION')
        self.zilliz_uri = os.getenv('ZILLIZ_URI')
        self.zilliz_user = os.getenv('ZILLIZ_USER')
        self.zilliz_password = os.getenv('ZILLIZ_PASSWORD')


class MilvusConfig(VectorDBConfig):
    def __init__(self):
        super().__init__('milvus')
        self.milvus_collection = os.getenv('MILVUS_COLLECTION')
        self.milvus_host = os.getenv('MILVUS_HOST')
        self.milvus_port = os.getenv('MILVUS_PORT')
        self.milvus_user = os.getenv('MILVUS_USER')
        self.milvus_password = os.getenv('MILVUS_PASSWORD')


class QdrantConfig(VectorDBConfig):
    def __init__(self):
        super().__init__('qdrant')
        self.qdrant_url = os.getenv('QDRANT_URL')
        self.qdrant_port = os.getenv('QDRANT_PORT')
        self.qdrant_grpc_port = os.getenv('QDRANT_GRPC_PORT')
        self.qdrant_api_key = os.getenv('QDRANT_API_KEY')
        self.qdrant_collection = os.getenv('QDRANT_COLLECTION')


class RedisConfig(VectorDBConfig):
    def __init__(self):
        super().__init__('redis')
        self.redis_host = os.getenv('REDIS_HOST')
        self.redis_port = os.getenv('REDIS_PORT')
        self.redis_password = os.getenv('REDIS_PASSWORD')
        self.redis_index_name = os.getenv('REDIS_INDEX_NAME')
        self.redis_doc_prefix = os.getenv('REDIS_DOC_PREFIX')
        self.redis_distance_metric = os.getenv('REDIS_DISTANCE_METRIC')
        self.redis_index_type = os.getenv('REDIS_INDEX_TYPE')

