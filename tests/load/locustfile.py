# type: ignore


from locust import HttpUser, task

from os import environ


TOKEN = environ["BEARER_TOKEN"]
headers = {"Authorization": f"Bearer {TOKEN}"}


class TestUser(HttpUser):
    @task
    def test(self):
        self.client.get("/users", headers=headers)

# async capping out about about 725 RPS
