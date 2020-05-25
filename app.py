#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from language_identification import LanguageIdentification
app = Flask(__name__)

LANGUAGE = LanguageIdentification()

@app.route('/detect_language', methods=['POST'])
def add_message():
    content = request.json
    lang = LANGUAGE.predict_lang(content['text'])
    return {"lang":lang[0][0], "score": lang[1][0]}

"""
curl request is as follows

curl -X POST \
  http://127.0.0.1:5000/detect_language \
  -H 'Content-Type: application/json' \
  -d '{"text":"hello"}'
"""

if __name__ == '__main__':
    app.run(host= '127.0.0.1', port= 5000)

