import json
import logging
import os

import urllib3
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from config import AppConfig, VectorDBConfig, EmbeddingsConfig

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


# Initialize app, vector db config, and embeddings config ##
app_config = AppConfig()
vector_db_config = VectorDBConfig(datastore=os.getenv('DATASTORE'))
embeddings_config = EmbeddingsConfig()


# Initialize app
app = FastAPI()

# Initialize http client
http = urllib3.PoolManager()

logging.info('Application started.')


@app.get("/")
async def health_check():
    """Health check endpoint"""
    logging.debug('Health check passed.')
    return {'statusCode': 200,
            'body': json.dumps('Health check passed')}