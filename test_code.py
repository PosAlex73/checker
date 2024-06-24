import docker
import tempfile


class CodeCheck:
    def __init__(self, language, code):
        self.language = language
        self.code = code

    def check_code(self):
        client = docker.from_env()

        with tempfile.NamedTemporaryFile(delete=True) as script:
            script.write(self.code)

            output = client.containers.run('python:3.12', 'python3 /testing/script.py', detach=False,
                                           volumes=["/home/alex/PycharmProjects/pythonProject4/testing:/testing/"])

        return {"errors": {}, "output": "code done"}
