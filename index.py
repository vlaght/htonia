import logging

from handlers import h_push

from flask import Flask
from flask import Response
from flask import request
from flask import jsonify

import requests

try:
    from cfg import TOKEN
    from cfg import GITLAB_TOKEN
except ImportError:
    raise ImportError(
        'Create cfg.py and place TOKEN="your_token_goes_here" there'
    )
logging.basicConfig(format=logging.BASIC_FORMAT)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

api_url = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

app = Flask(__name__)

@app.route('/gitlab', defaults={'path': 'gitlab'}, methods=['POST', 'GET'])
def gitlab(path):

    if request.headers.get('X-Gitlab-Token') != GITLAB_TOKEN:
        return jsonify({}), 401

    if request.method == 'POST':
        try:
            data = request.json
            logger.debug('Recieved: %s', data)
            response_data = h_push(data)
            response = requests.post(
                api_url,
                data=response_data,
            )
            return jsonify(
                {
                    'telegram_api_response_code': response.status_code
                }
            ), 200
        except Exception as e:
            return jsonify({'error': e}), 500
    return jsonify({'endpoint':'/gitlab'}), 200

@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
def catch_all(path):
    logging.debug('catch_all')
    if request.method == 'POST':
        try:
            data = request.json
            logger.debug('Recieved: %s', data)
            message = {
                'chat_id': data['message']['chat']['id'],
                'text': data['message']['text']+"```{}```".format(data)
            }
            requests.post(
                api_url,
                data=message
            )
            return jsonify({}), 200
        except Exception as e:
            return jsonify({'error': e}), 500
    return jsonify({'endpoint': '/'}), 200
