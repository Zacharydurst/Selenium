import pytest


@pytest.mark.usefixtures("driver")
class BaseClass:
    """BaseClass takes in driver fixture."""
