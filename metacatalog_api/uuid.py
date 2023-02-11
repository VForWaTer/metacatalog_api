from fastapi import APIRouter

from metacatalog import api


session = api.connect_database()
router = APIRouter()


@router.get('/{uuid}')
async def get_uuid(uuid: str):
    # connet to the database
    result = api.get_uuid(session, uuid=uuid, as_result=True)

    if hasattr(result, 'to_dict'):
        return result.to_dict()
    else:
        return {
            'message': 'The requested object refused to represent itself as dict.',
            'type': type(result),
            'representation': str(result)
        }
