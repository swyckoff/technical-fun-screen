from enum import Enum


class Dispatch(Enum):
    """Specifies the stack types a package can dispatch to"""

    REJECTED = "REJECTED"
    SPECIAL = "SPECIAL"
    STANDARD = "STANDARD"
