from thoughtful_ai.threshold import Threshold
from thoughtful_ai.dispatch import Dispatch

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Package:
    """A package that requires strict dispatch rules for how it's handled. Assumes scales
    and measuring devices are precise up to 2 decimal points.

    Notes:
    1. Using float but if we needed it to be exact then we could use Decimal to store
    the measurements instead.

    However since this is a short exercise and I can't ask for clarification, float will suffice.

    """

    width: float = Field(..., gt=0, description="Width must be a positive number")
    height: float = Field(..., gt=0, description="Height must be a positive number")
    length: float = Field(..., gt=0, description="Length must be a positive number")
    mass: float = Field(..., gt=0, description="Mass must be a positive number")
    is_bulky: bool = Field(init=False)
    is_heavy: bool = Field(init=False)

    def __post_init__(self) -> None:
        """
        Automatically computes whether the package is bulky or heavy after initialization.
        """
        self.is_bulky = self._compute_is_bulky()
        self.is_heavy = self._compute_is_heavy()

    def _compute_is_bulky(self) -> bool:
        """
        Determines if the package is bulky based on the volume or any dimension.
        """
        volume = self.width * self.height * self.length
        max_dimension = max(self.width, self.height, self.length)
        return (
            volume >= Threshold.BULKY_VOLUME_CM3
            or max_dimension >= Threshold.BULKY_DIMENSION_CM
        )

    def _compute_is_heavy(self) -> bool:
        """
        Determines if the package is heavy based on mass.
        """
        return self.mass >= Threshold.HEAVY_MASS_KG

    def sort(self) -> Dispatch:
        """
        Determines the appropriate stack for a package based on its dimensions and mass.

        Returns:
            Dispatch: The stack where the package should go ('STANDARD', 'SPECIAL', 'REJECTED').
        """
        if self.is_bulky and self.is_heavy:
            return Dispatch.REJECTED
        elif self.is_bulky or self.is_heavy:
            return Dispatch.SPECIAL

        return Dispatch.STANDARD
