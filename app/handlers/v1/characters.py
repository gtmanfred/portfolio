import uuid

from fastapi import APIRouter

from app.characters import Character
from app.characters import CharacterGenerator


router = APIRouter()

class Response(Character):
    seed: uuid.UUID


@router.get('/bastards', response_model=Response)
def get_new_character(commoner: bool = False, extra_classes: bool = False):
    seed = uuid.uuid4()
    return {
        "seed": seed,
        **CharacterGenerator.create(
            commoner=commoner,
            extra_classes=extra_classes,
            seed=seed,
        ).dict(),
    }


@router.get('/bastards/{character_id}', response_model=Response)
def get_new_character(character_id: uuid.UUID, commoner: bool = False, extra_classes: bool = False):
    return {
        "seed": character_id,
        **CharacterGenerator.create(
            commoner=commoner,
            extra_classes=extra_classes,
            seed=character_id,
        ).dict(),
    }
