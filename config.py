class Config:
    PHP = 'php'
    PYTHON = 'python'
    GOLANG = 'go'

    scripts_path = '/home/alex/PycharmProjects/pythonProject4/scripts/'

    def getLangImage(self, name):
        if name == self.PHP:
            return 'php:8.2-cli'
        elif name == self.PYTHON:
            return 'python:3.12'
        elif name == self.GOLANG:
            return 'golang:1.22'

    def getLangs(self):
        return [self.PHP, self.PYTHON, self.GOLANG]
