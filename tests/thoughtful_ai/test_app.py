from pydantic import ValidationError
import pytest

from thoughtful_ai.dispatch import Dispatch
from thoughtful_ai.package import Package
from tests.thoughtful_ai.models import (
    AllTestCases,
    SingleTestCase,
)


import json

from pathlib import Path

TEST_CASES_FILE = Path(__file__).parent / "data" / "package_sort_test_cases.json"


def load_test_cases() -> list[SingleTestCase]:
    with TEST_CASES_FILE.open("r") as f:
        raw_data = json.load(f)
        test_cases_obj = AllTestCases.model_validate(raw_data)
        return test_cases_obj.test_cases


test_cases: list[SingleTestCase] = load_test_cases()


@pytest.mark.parametrize(
    "case", test_cases, ids=[case.description for case in test_cases]
)
def test_package_sort(case: SingleTestCase) -> None:
    """Test the sort method for packages with invalid and input that tests the thresholds expected for the package dimensions and mass.

    Args:
        case (SingleTestCase)

    Asserts:
        Either the calculated dispatch type matches the expected dispatch type or the input throws a ValidationError.

    """
    if case.expected_exception:
        with pytest.raises(ValidationError):
            package = Package(
                width=case.width,
                height=case.height,
                length=case.length,
                mass=case.mass,
            )
            dispatch: Dispatch = package.sort()
    else:
        package = Package(
            width=case.width,
            height=case.height,
            length=case.length,
            mass=case.mass,
        )
        dispatch = package.sort()
        assert (
            dispatch == case.expected_dispatch
        ), f"Expected {case.expected_dispatch}, got {dispatch}"
