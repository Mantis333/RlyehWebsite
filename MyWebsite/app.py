import requests
from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime, timedelta
import time
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')


if __name__=="__main__":
    app.debug=False