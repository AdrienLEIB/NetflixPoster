from flask import request, jsonify
from models.Poster import Poster

def get_posters():
    if request.get_json():
        return jsonify( Poster.objects(**request.get_json())), 200
    return jsonify(Poster.objects()), 200


def get_poster(id):
    return jsonify(Poster.objects.get_or_404(id=id)), 200

def create_poster():
    body = request.get_json()
    poster = Poster(**body).save()

    return jsonify(poster), 201

def update_poster(id):
    body = request.get_json()
    poster = Poster.objects.get_or_404(id=id)
    poster.update(**body)
    return jsonify(Poster.objects.get_or_404(id=id)), 201

def delete_poster(id):
    poster = Poster.objects.get_or_404(id=id)
    poster.delete()
    return jsonify(str(poster.id)), 200
