import json


def commits_description(commits):
    template = "{idx}. {message} ({author})."
    return '\n'.join(
        [
            template.format(
                idx=idx,
                message=c['message'],
                author=c['author']['name'],
            ) for idx, c in enumerate(commits)
        ]
    )


def commits_keyboard(commits):
    return {
        "inline_keyboard": [
            [
                dict(
                    text=idx,
                    url=c['url']
                ) for idx, c in enumerate(commits)
            ]
        ]
    }


def h_push(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: push в {ref}\nКто: {push_initiator_name} ({push_initiator_username})\nКоммиты: \n{commits_description}"

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        ref=data['ref'],
        push_initiator_name=data['user_name'],
        push_initiator_username=data['user_username'],
        commits_description=commits_description(data['commits']),
    )
    return {
        'text': message,
        'reply_markup': json.dumps(commits_keyboard(data['commits']))
    }
