from flask import request, render_template, jsonify
from . import main

@main.route('/')
def index():
    return "Hello, world."
