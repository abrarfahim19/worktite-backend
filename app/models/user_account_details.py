from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl, AnyHttpUrl
from typing import Annotated, List, Optional
from pydantic.functional_validators import BeforeValidator
from ..models.user import UserModel
from ..models.account_details import AccountDetailsModel 

PyObjectId = Annotated[str, BeforeValidator(str)]

class UserAccountDetailsModel(BaseModel):
    user: UserModel
    accountDetails: AccountDetailsModel