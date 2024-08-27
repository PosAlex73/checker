import docker
import tempfile


class CodeCheck:
    def __init__(self, language, code):
        self.language = language
        self.code = code

    def check_code(self):
        client = docker.from_env()

        with tempfile.NamedTemporaryFile(delete=True) as script:
            script.write(bytes(self.code, 'utf-8'))

            output = client.containers.run('python:3.12', 'python3 /testing/script.py', detach=True,
                                           volumes=["/home/alex/PycharmProjects/pythonProject4/testing:/testing/"])

        return {"errors": {}, "output": str(output.logs())}
