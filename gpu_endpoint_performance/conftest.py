import pytest


def pytest_addoption(parser):
    parser.addoption("--rounds", action="store", default=1, help="Number of repeats")


@pytest.fixture
def rounds(request):
    return int(request.config.getoption("--rounds"))
