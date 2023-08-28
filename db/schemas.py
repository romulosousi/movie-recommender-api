from typing_extensions import Optional
from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    year: Optional[int] = None
    genres: str

class MovieRequest(MovieBase):
    ...

class MovieResponse(MovieBase):
    movieId: int 

    class Config:
        from_attributes = True 



class UserBase(BaseModel):
    userName: str

class UserRequest(UserBase):
    ...

class UserResponse(UserBase):
    userId: int

    class Config:
        from_attributes = True


class RatingsBase(BaseModel):
    rating: float

class RatingsRequest(RatingsBase):
    ...

class RatingsResponse(RatingsBase):
    user: UserResponse
    movie: MovieResponse 
    


    class Config:
        from_attributes = True 
