import flask 
# pip install Flask
from flask import request, jsonify
# pip install flask-requests
# pip install jsonify
import requests
# pip install requests
import json
# pip install jsonlib
import sqlite3
# pip install db-sqlite3
import numpy
# pip install numpy
from numpy import random
# pip install random2



app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d








@app.route('/przepisy', methods=['GET'])
def przepisy():
    db = sqlite3.connect('other/ZPI.db')
    db.row_factory = dict_factory
    c = db.cursor()
    wynik = c.execute('SELECT Przepisy.Nazwa_Przepisy, Przepisy.Przepis, Składniki.Nazwa_Składniki, Przep_Skład.Ilość, Przep_Skład.Typ FROM Przep_Skład LEFT JOIN Przepisy ON (Przep_Skład.Id_Przepis=Przepisy.Id_Przepisy) INNER JOIN Składniki ON (Przep_Skład.Id_Skład=Składniki.Id_Składniki)').fetchall()
    # db.close()
    return jsonify(wynik)


@app.route('/api', methods=['POST'])
def wstawianie():
        data = request.get_json()
        db = sqlite3.connect('other/ZPI.db')
        db.row_factory = dict_factory
        c = db.cursor()
        for x in data:
            c.execute("insert into Składniki values(?,?);", (data[x]['Id'], data[x]['Nazwa'])).fetchall()
        db.commit()

        # c.close()

        # except Exception as E:
        #     return jsonify('Error : ', E)
        # else:
        #     db.commit()
        return jsonify('data inserted')


@app.route('/skladniki', methods=['GET'])
def skladniki():

    db = sqlite3.connect('other/ZPI.db')
    db.row_factory = dict_factory
    c = db.cursor()
    wynik = c.execute('SELECT Nazwa_Składniki FROM Składniki WHERE Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ? OR Id_Składniki = ?', [random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62), random.randint(1, 62)]).fetchall()
    # db.close()
    return jsonify(wynik)


app.run()