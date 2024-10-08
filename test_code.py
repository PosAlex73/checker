import os.path

import docker
import tempfile
from src import responses

from src.language import BaseLanguage


class CodeCheck:
    def __init__(self, language, code):
        self.language = language
        self.code = code

    def check_code(self, docker_settings: BaseLanguage):

        try:
            client = docker.from_env()

            with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as script:
                script.write(self.code)
                script.seek(0)
                file_name = os.path.basename(script.name)
                file_path = os.path.dirname(script.name)

                output = client.containers.run(
                    docker_settings.docker_image,
                    docker_settings.docker_command + file_name,
                    detach=False,
                    volumes=[file_path + ":/testing/"],
                    stderr=True,
                    stdout=True,
                    isolation='default'
                )
        except docker.errors.ContainerError as e:
            return responses.create_common_error_response(e)

        return responses.create_response(output)
