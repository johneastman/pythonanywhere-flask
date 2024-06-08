from flask import Flask, Response, request, make_response
import os
import json

app = Flask(__name__)


@app.route("/lists/<username>", methods=["GET", "POST"])
def lists(username):
    project_folder = os.path.expanduser(app.root_path)
    file_path = os.path.join(project_folder, f"{username}.json")

    # Get Data
    if request.method == "GET":
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
                body = json.loads(file_content)
                return make_response(body, 200)
        except FileNotFoundError:
            return make_response({"message": "File not found"}, 404)

    # Save Data
    try:
        with open(file_path, "w") as file:
            file_content = json.dumps(request.json)
            file.write(file_content)
    except Exception as e:
        return make_response({"message": str(e)}, 500)

    return make_response({"message": "Data saved successfully"}, 200)


if __name__ == "__main__":
    app.run()
