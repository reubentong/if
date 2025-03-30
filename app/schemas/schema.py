import uuid

from pydantic import BaseModel


class GroupData(BaseModel):
    id: uuid.UUID
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
    id: uuid.UUID
    type: str
    attributes: BreedAttributes
    relationships: BreedRelationships


class Pagination(BaseModel):
    current: int | None = None
    next: int | None = None
    last: int | None = None
    records: int | None = None


class Meta(BaseModel):
    pagination: Pagination


class Links(BaseModel):
    self: str | None = None
    current: str | None = None
    next: str | None = None
    last: str | None = None


class BreedsResponse(BaseModel):
    data: list[Breed]
    meta: Meta | None = None
    links: Links | None = None
