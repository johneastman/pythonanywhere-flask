from flask import Flask, Response, request, make_response
import os
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
