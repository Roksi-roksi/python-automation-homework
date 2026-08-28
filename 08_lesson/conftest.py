import pytest
from yougile_api import YougileProjectsClient


def pytest_addoption(parser):
    parser.addoption(
        "--token", action="store", default=None, help="API token for Yougile"
    )


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"


@pytest.fixture(scope="session")
def api_key(request):
    token = request.config.getoption("--token")

    if not token:
        pytest.fail(
            "Ошибка: Передайте API токен через команду: "
            "pytest <путь_к_папке> --token=ВАШ_ТОКЕН"
        )
    return token


@pytest.fixture(scope="session")
def api_client(base_url, api_key):
    return YougileProjectsClient(base_url, api_key)


@pytest.fixture
def temp_project(api_client):
    response = api_client.create_project(title="Autotest Temp Project")

    assert response.status_code in [
        200,
        201,
    ], f"Не удалось создать проект: {response.text}"

    project_id = response.json().get("id")
    yield project_id

    api_client.update_project(project_id, deleted=True)
