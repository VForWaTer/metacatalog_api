from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# build app
app = FastAPI()

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
