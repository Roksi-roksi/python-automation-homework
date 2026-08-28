import requests

class YougileProjectsClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def create_project(self, title: str, users: dict = None) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects"
        payload = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, title: str = None, deleted: bool = None) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {}
        if title is not None:
            payload["title"] = title
        if deleted is not None:
            payload["deleted"] = deleted
        return requests.put(url, json=payload, headers=self.headers)




