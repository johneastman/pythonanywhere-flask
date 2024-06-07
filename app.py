from flask import Flask, Response, request, make_response
import os
import json

app = Flask(__name__)


@app.route("/lists", methods=["GET", "POST"])
def lists():
    project_folder = os.path.expanduser(app.root_path)
    file_path = os.path.join(project_folder, "data.json")

    if request.method == "GET":
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                body = json.loads(file_content)
                return make_response(body, 200)
        except FileNotFoundError:
            return make_response({"message": "File not found"}, 404)

    # Save Data
    with open(file_path, "w") as file:
        file_content = json.dumps(request.json)
        file.write(file_content)

    return make_response({"message": "OK"}, 200)


if __name__ == "__main__":
    app.run()
