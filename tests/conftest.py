import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app
import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore the in-memory activity data before and after each test."""
    original_state = copy.deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_state))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
