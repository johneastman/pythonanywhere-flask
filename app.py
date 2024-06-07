from flask import Flask, request
import os
import json

app = Flask(__name__)


@app.route("/lists", methods=["GET", "POST"])
def lists():
    project_folder = os.path.expanduser(app.root_path)
    file_path = os.path.join(project_folder, "data.json")

    if request.method == "GET":
        with open(file_path, "r") as file:
            file_content = file.read()
            return json.loads(file_content)

    # Save Data
    with open(file_path, "w") as file:
        file_content = json.dumps(request.json)
        file.write(file_content)

    return {"message": "OK"}


if __name__ == "__main__":
    app.run()
