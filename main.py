from flask import Flask, jsonify, request
from test_code import CodeCheck
from validator import JsonValidateForm
from config import HOST, PORT, DEBUG
from language import get_docker_settings

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    jsonData = request.get_json()
    form = JsonValidateForm(data=jsonData)

    if form.validate():
        code_checker = CodeCheck(jsonData["language"], jsonData["code"])
        docker_settings = get_docker_settings(code_checker.language)
        result = code_checker.check_code(docker_settings)
        json = result.toJson()
        return jsonify(json)
    else:
        json = {"errors": form.errors}
        return jsonify(json)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
