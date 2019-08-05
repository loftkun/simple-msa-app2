import sys
import traceback
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  try:
    time.sleep(3)
    return jsonify({"app2": "OK"})
  except Exception as e:
    return jsonify({"app2": "{0}".format(e)}), 500

if __name__ == '__main__':
  app.run()