from flask import request, render_template, jsonify
from . import api

@api.route('/')
def index():
	return 'welcome'

@api.route('/0.1/search/<word>')
def search(word):
	result = {
		"code": 0,
		"msge": "has found",
		"data": {"name": "%s" % word}
	}
	return jsonify(result)
