from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


#creation of an Audio Data Structure
class AudioSchema(BaseModel):
    name:str
    language:str
    status:str
    created_at:datetime
    created_by:str
    updated_at:datetime
    updated_by:str

#Giving an example of the Scheme
    class Config:
        schema_extra={
            "example":{
                "name":"Sandhra",
                "language":"Malayalam",
                "status":"Process",
                "created_at":"2022-12-27 08:26:49.219717",
                "created_by":"admin",
                "updated_at":"2022-12-28 08:26:49.219717",
                "updated_by":"admin"
            }
        }

#Updation Schema for Put operation
        class UpdateAudioSchema(BaseModel):
            name:Optional[str]
            language:Optional[str]
            status:Optional[str]
            created_at:Optional[datetime]
            created_by:Optional[str]
            updated_at:Optional[datetime]
            updated_by:Optional[str]

            class Config:
                schema_extra={
                "example":{
                "name":"Bijoy",
                "language":"Hindi",
                "status":"Process",
                "created_at":"2022-12-27 08:26:49.219717",
                "created_by":"admin",
                "updated_at":"2022-12-28 08:26:49.219717",
                "updated_by":"admin"
                }}
#Define the response message to be obtained        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
#Define the error message to be obtained
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}