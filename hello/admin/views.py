from flask import request, render_template, jsonify
from . import admin

@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/check-name', methods=['POST'])
def checkNameAjax():
	name = request.form.get('name')
	return jsonify('server get: %s' % name)