from flask import request, jsonify
import requests

def get_medias(id):
    r = requests.get('127.0.0.1:5000/films')
    return jsonify(r.json), 200
