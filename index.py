import logging

from flask import Flask
from flask import Response
from flask import request
from flask import jsonify

import requests

try:
    from cfg import TOKEN
except ImportError:
    raise ImportError(
        'Create cfg.py and place TOKEN="your_token_goes_here" there'
    )
logging.basicConfig(format=logging.BASIC_FORMAT)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

api_url = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>')
def catch_all(path):
    if request.method == 'POST':
        try:
            data = request.json
            logger.debug('Recieved: %s', data)
            message = {
                'chat_id': data['message']['chat']['id'],
                'text': data['message']['text']
            }
            requests.post(
                api_url,
                data=message
            )
            return jsonify({}), 200
        except Exception as e:
            return jsonify({'error': e}), 500
    return jsonify({}), 422
