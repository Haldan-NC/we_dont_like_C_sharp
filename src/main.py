# Main pipeline for the project which should be run and await for interactions with the front end.
# Host the backend server using flask and use REST APIs to interact with the front end.

from flask import Flask, request, jsonify
from Graph import Graph
from Delivery import Delivery
from CargoType import CargoType

from flask import Flask, request, jsonify

def run_server():
    app = Flask(__name__)


if __name__ == "__main__":
    app = Flask(__name__)