import uuid

from fastapi import APIRouter

from app.characters import Character
from app.characters import CharacterGenerator


router = APIRouter()

class Response(Character):
    seed: uuid.UUID


@router.get('/bastards', response_model=Response, operation_id="get_new_character", tags=['bastards'])
@router.get('/bastards/{character_id}', response_model=Response, operation_id="get_character", tags=['bastards'])
def get_character(commoner: bool = False, extra_classes: bool = False, character_id: uuid.UUID = None):
    seed = uuid.uuid4() if character_id is None else character_id
    return {
        "seed": seed,
        **CharacterGenerator.create(
            commoner=commoner,
            extra_classes=extra_classes,
            seed=seed,
        ).dict(),
    }
