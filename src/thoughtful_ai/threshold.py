from enum import IntEnum


class Threshold(IntEnum):
    """The thresholds to determine how to sort the packages"""

    BULKY_VOLUME_CM3 = 1_000_000
    BULKY_DIMENSION_CM = 150
    HEAVY_MASS_KG = 20
