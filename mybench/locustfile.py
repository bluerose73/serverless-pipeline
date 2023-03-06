from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post(
            '/',
            json={
                "bucket":{
                    "input": "msj-sebs-input",
                    "output": "msj-sebs-output"
                },
                "object":{
                    "key": "210.thumbnailer/9_cobblestone-granite-pebbles-1029604.jpg",
                    "width": 200,
                    "height": 200
                }
            }
        )