import pytest


def pytest_addoption(parser):
    parser.addoption("--rounds", action="store", default=1, help="Number of repeats")
    parser.addoption("--iterations", action="store", default=1, help="Number of iterations")


@pytest.fixture
def rounds(request):
    return int(request.config.getoption("--rounds"))


@pytest.fixture
def iterations(request):
    return int(request.config.getoption("--iterations"))
