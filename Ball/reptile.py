from flask import (Blueprint, request, redirect)
import json
from . import models

reptiles = json.load(open('reptiles.json'))

bp = Blueprint(
    'reptile',
    __name__,
    url_prefix='/reptiles'
)

@bp.route('/')
def index():
    return reptiles

@bp.route('/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def show(id):
    reptile = reptiles[id - 1]

    if request.method == 'POST':
 
        new_reptile = models.Reptiles(reptile_name = 'reptile_name', reptile_age = 'reptile_age', reptile_weight = 'reptile_weight')
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return redirect('/reptiles')
    
    elif request.method == 'PUT':
        new_reptile = models.Reptiles()
        reptile = new_reptile
        models.db.session.commit()
    
    elif request.method == 'DELETE':
        models.db.session.delete(reptile)
        models.db.session.commit()
    
    return reptile


