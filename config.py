PHP = 'php'
PYTHON = 'python'
GOLANG = 'go'

scripts_path = '/home/alex/PycharmProjects/pythonProject4/scripts/'


def getLangImage(self, name):
    if name == PHP:
        return 'php:8.2-cli'
    elif name == PYTHON:
        return 'python:3.12'
    elif name == GOLANG:
        return 'golang:1.22'


def getLangs():
    return [PHP, PYTHON, GOLANG]
