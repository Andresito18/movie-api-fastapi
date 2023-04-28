from pydantic import BaseModel, Field
from typing import Optional



class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(max_length=50, min_length=15)
    year:int = Field(le=2023)
    rating:float = Field(ge=1, le=10)
    category:str = Field(max_length=15, min_length=5)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la peli",
                "year": 2022,
                "rating": 9.8,
                "category": "Accion"
            }
        }