import uuid


def test_create_project_positive(api_client):
    """Позитивный тест: Создание проекта с валидным названием"""
    project_title = f"Project_{uuid.uuid4().hex[:6]}"
    response = api_client.create_project(title=project_title)

    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data

    api_client.update_project(data["id"], deleted=True)


def test_create_project_negative_empty_title(api_client):
    """Негативный тест: Создание проекта с пустым
    заголовком (отсутствие обязательного поля)"""
    response = api_client.create_project(title="")
    assert response.status_code == 400


def test_get_project_positive(api_client, temp_project):
    """Позитивный тест: Получение данных существующего проекта"""
    response = api_client.get_project(project_id=temp_project)

    assert response.status_code == 200
    data = response.json()
    assert data.get("id") == temp_project
    assert "title" in data


def test_get_project_negative_invalid_id(api_client):
    """Негативный тест: Запрос несуществующего или некорректного ID проекта"""
    invalid_id = "non-existent-id-12345"
    response = api_client.get_project(project_id=invalid_id)

    assert response.status_code in [404, 400]


def test_update_project_positive(api_client, temp_project):
    """Позитивный тест:
    Обновление названия существующего проекта"""
    new_title = f"Updated_{uuid.uuid4().hex[:6]}"
    response = api_client.update_project(
        project_id=temp_project, title=new_title)
    assert response.status_code == 200

    get_res = api_client.get_project(project_id=temp_project)
    assert get_res.json().get("title") == new_title


def test_update_project_negative_non_existent(api_client):
    """Негативный тест:
    Попытка обновить параметры у несуществующего проекта"""
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.update_project(
        project_id=invalid_id, title="New Title")
    assert response.status_code in [404, 400]
