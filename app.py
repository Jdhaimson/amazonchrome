from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
import random
import os
import sys
from product_search.product_search.amazon_search import get_search_results
from boto.s3.connection import S3Connection

app = Flask(__name__)

@app.route("/summer", methods=['GET'])
@cross_origin()
def index():
    searchResults = get_search_results(os.environ['AMAZON_ACCESS_KEY'], os.environ['AMAZON_SECRET_KEY'], os.environ['AMAZON_ASSOC_TAG'])
    print (searchResults, file=sys.stderr)
    return jsonify(random.choice(list(searchResults)))

@app.route("/")
def yes():
    print("in", file=sys.stderr)
    return app.send_static_file('index.html')
