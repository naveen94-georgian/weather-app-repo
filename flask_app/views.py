from flask import Flask, render_template, request, json, Response, jsonify
from flask_app.app_lib.mongo_api import MongoAPI

app = Flask(__name__)

mongo = MongoAPI(db_name='hpracdb', doc_name='house_exp')
lst = mongo.fetch_all()

@app.route("/")
def index():
	return render_template('index.html' , data=lst)

# @app.route('/get_data')
# def get_data():
#     return Response(response=json.dumps(mongo.fetch_all()), status=200, mimetype='application/json')

@app.route('/get_data')
def get_data():
    return render_template('./components/mongo_table.html', data=lst)







