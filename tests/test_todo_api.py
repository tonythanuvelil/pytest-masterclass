import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data.get("task").get("task_id")
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data.get("content") == payload.get("content")
    assert get_task_data.get("user_id") == payload.get("user_id")


def test_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json().get("task").get("task_id")

    new_payload = {
        "content": "My updated content",
        "user_id": payload.get("user_id"),
        "task_id": task_id,
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    print(update_task_response.json())
    assert update_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data.get("content") == new_payload.get("content")
    assert get_task_data.get("is_done") == new_payload.get("is_done")


def create_task(payload):
    return requests.put(f"{ENDPOINT}/create-task", json=payload)


def update_task(payload):
    return requests.put(f"{ENDPOINT}/update-task", json=payload)


def get_task(task_id):
    return requests.get(f"{ENDPOINT}/get-task/{task_id}")


def new_task_payload():
    return {
        "content": "My test content",
        "user_id": str(uuid.uuid4()),
        "is_done": False,
    }
