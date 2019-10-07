import logging

from handlers import h_push
from handlers import h_tag_push
from handlers import h_issue
from handlers import h_comment

try:
    from cfg import TOKEN
    from cfg import SECRET_TOKEN
    from cfg import CHAT_ID
except ImportError:
    raise ImportError(
        'Create your personal cfg.py'
    )

from flask import Flask
from flask import Response
from flask import request
from flask import jsonify

import requests


logging.basicConfig(format=logging.BASIC_FORMAT)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

api_url = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

app = Flask(__name__)

def resolve(data):
    tp = data['object_kind']
    handlers = {
        'push': h_push,
        'tag_push': h_tag_push,
        'issue': h_issue,
        'note': h_comment,
    }
    assert tp in handlers.keys(), 'Can`t handle this one yet'
    return handlers[tp](data)

@app.route('/gitlab', defaults={'path': 'gitlab'}, methods=['POST', 'GET'])
def gitlab(path):

    if request.headers.get('X-Gitlab-Token') != SECRET_TOKEN:
        return jsonify({}), 401

    if request.method == 'POST':
        try:
            data = request.json
            logger.debug('Recieved: %s', data)
            response_data = resolve(data)
            response_data['chat_id'] = CHAT_ID
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
            chat_id = data['message']['chat']['id']
            message = {
                'chat_id': data['message']['chat']['id'],
                'text': "chat_id for cfg.py: {}".format(chat_id)
            }
            requests.post(
                api_url,
                data=message
            )
            return jsonify({}), 200
        except Exception as e:
            return jsonify({'error': e}), 500
    return jsonify({'endpoint': '/'}), 200
