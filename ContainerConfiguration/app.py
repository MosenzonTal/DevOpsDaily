import json
from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello! this is DevOpsDaily!"


@app.route("/users")
def getAllUsers():
    # Opening JSON file
    # f = open('users.json')    # users.json is a Dummy JSON Data
    # data = json.load(f)       # In this project we will use jsonPlaceHolder as a fake database .
    response = requests.get('https://my-json-server.typicode.com/MosenzonTal/JsonHolder/db')
    if response.ok:
        data = response.json()
        for value in data.values():
            value.pop('id')
            result_dict = json.dumps(data)  # object to JSON
        return result_dict
    else:
        return 'HTTP code 404 - Bad response from server'


@app.route('/users/<username>')
def searchUserByName(username):
    response = requests.get('https://my-json-server.typicode.com/MosenzonTal/JsonHolder/db')
    if response.ok:
        data = response.json()
        if username in data:
            username_json = json.dumps({username: data[username]})
            return username_json
        else:
            return "HTTP code 404 - the user does not exist in the database"
    else:
        return 'Bad Response'


if __name__ == "__main__":
    app.run()
