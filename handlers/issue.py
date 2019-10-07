import json


def h_issue(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: issue {action} \nСсылка: {url}"

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        url=data['object_attributes']['url'],
        action=data['object_attributes']['action'],
    )
    reply_markup_body = {
        "inline_keyboard": [
            [
                {
                    'text': 'Смотреть 👀',
                    'url': data['object_attributes']['url'],
                }
            ]
        ]
    }
    return {
        'text': message,
        'reply_markup': json.dumps(reply_markup_body)
    }
