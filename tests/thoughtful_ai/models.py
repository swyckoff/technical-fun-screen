from typing import Optional, Union
from pydantic import BaseModel, Field
from enum import Enum

from thoughtful_ai.dispatch import Dispatch


class PackageException(str, Enum):
    VALIDATION_ERROR = "ValidationError"


class SingleTestCase(BaseModel):
    """Store and validate the input for a package"""

    description: str
    width: Union[float, str]
    height: Union[float, str]
    length: Union[float, str]
    mass: Union[float, str]
    expected_dispatch: Optional[Dispatch] = Field(None)
    expected_exception: Optional[PackageException] = Field(None)


class AllTestCases(BaseModel):
    test_cases: list[SingleTestCase]
