import os.path

import docker
import tempfile


class CodeCheck:
    def __init__(self, language, code):
        self.language = language
        self.code = code

    def check_code(self, docker_settings):
        client = docker.from_env()

        with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as script:
            script.write(self.code)
            script.seek(0)
            file_name = os.path.basename(script.name)
            file_path = os.path.dirname(script.name)

            output = client.containers.run(
                'python:3.12',
                'python3 /testing/' + file_name,
                detach=False,
                volumes=[file_path + ":/testing/"],
                stderr=True,
                stdout=True,
            )

        return {"errors": {}, "output": str(output, encoding='utf-8')}
