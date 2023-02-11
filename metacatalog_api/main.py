from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import routes
from metacatalog_api import uuid

# build app
app = FastAPI()
app.include_router(uuid.router, prefix='/uuid')

#enable cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)


@app.get('/')
async def main():
    return {'message': 'Main Metacatalog API Endpoint'}