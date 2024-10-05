from config import PHP, PYTHON, GOLANG


class BaseLanguage:
    def __init__(self, docker_command, docker_image):
        self.docker_command = docker_command
        self.docker_image = docker_image


class Php(BaseLanguage):
    def __init__(self):
        super().__init__('php /testing/', 'php:8.2-cli')


class Python(BaseLanguage):
    def __init__(self):
        super().__init__('python3 /testing/', 'python:3.12')


class Golang(BaseLanguage):
    def __init__(self):
        super().__init__('go run /testing/', 'golang:1.23')


def get_docker_settings(lang):
    if lang == GOLANG:
        return Golang()
    elif lang == PHP:
        return Php()
    elif lang == PYTHON:
        return Python()
    else:
        raise ValueError(f"Unsupported language: {lang}")
