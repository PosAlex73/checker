from flask import Flask, jsonify, request
from test_code import CodeCheck
from validator import JsonValidateForm
from config import getLangs, HOST, PORT

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    jsonData = request.get_json()
    form = JsonValidateForm(data=jsonData)

    if form.validate():
        code_checker = CodeCheck(jsonData["language"], jsonData["code"])
        result = code_checker.check_code()

        if len(result["errors"]) == 0:
            json = {"errors": 0, "output": result["output"]}
            return jsonify(json)
    else:
        json = {"errors": form.errors}
        return jsonify(json)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
