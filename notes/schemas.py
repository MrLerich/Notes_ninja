#схемы – они в Django Ninja выполняют те же самые функции, что и сериализатор в Django REST Framework,
# то есть определяют, какие именно данные поступают в базу и какие запрашиваются.
# Обратите внимание на разницу в наборах данных между схемами NoteIn, NoteOut, NoteUpd, CategoryIn, CategoryOut
from datetime import date

from ninja import Schema, ModelSchema

from notes.models import Note


class CategoryIn(Schema):
    title: str
    description: str


class CategoryOut(Schema):
    id: int
    title: str
    description: str
    created: date


class NoteIn(ModelSchema):
    class Config:
        model = Note
        model_fields = ['title', 'category']


class NoteUpd(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'completed']


class NoteOut(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'title', 'category', 'created', 'completed']


