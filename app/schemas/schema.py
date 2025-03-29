from pydantic import BaseModel


class GroupData(BaseModel):
    id: str
    type: str


class GroupRelationship(BaseModel):
    data: GroupData


class BreedRelationships(BaseModel):
    group: GroupRelationship


class BreedWeight(BaseModel):
    max: int
    min: int


class BreedLifeSpan(BaseModel):
    max: int
    min: int


class BreedAttributes(BaseModel):
    name: str
    description: str
    life: BreedLifeSpan
    male_weight: BreedWeight
    female_weight: BreedWeight
    hypoallergenic: bool


class Breed(BaseModel):
    id: str
    type: str
    attributes: BreedAttributes
    relationships: BreedRelationships


class DogAPIBreedResponse(BaseModel):
    data: Breed
    links: dict
