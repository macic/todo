from pydantic import BaseModel

# Shared properties
class ItemBase(BaseModel):
    title: str = None
    priority: int = 0



# Properties to receive on item creation
class ItemCreate(ItemBase):
    user_id: str
    user_name: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    priority: int
    user_id: str
    user_name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
