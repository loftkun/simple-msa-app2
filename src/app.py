import sys
import traceback
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
  try:
    # get param
    interval = request.args.get('sleep')
    if interval == None:
      interval = 0
    
    # sleep
    time.sleep(int(interval))
    return jsonify({"app2": "OK"})
  except Exception as e:
    return jsonify({"app2": "{0}".format(e)}), 500

if __name__ == '__main__':
  app.run()