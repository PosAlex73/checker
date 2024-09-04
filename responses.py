import json


class Response:
    def __init__(self, output: str, errors: {}):
        self.output = output
        self.errors = errors

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def create_common_error_response(e):
    return Response(
                'Ошибка при исполнении кода',
                {
                    'errors': f"{e}"
                }
            )


def create_response(output):
    return Response(
        str(output, encoding='utf-8'),
        {}
    )