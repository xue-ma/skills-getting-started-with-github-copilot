import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


BASE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activity state before each test."""
    app_module.activities = copy.deepcopy(BASE_ACTIVITIES)
    yield


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app_module.app)
