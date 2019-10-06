def commits_description(commits):
    template = "Пользователь {} \nсоздал коммит {} с сообщением \n'{}' в {}. \nСсылка на коммит: {}"
    return '\n'.join(
        [
            template.format(
                c['author']['name'],
                c['id'],
                c['message'],
                c['timestamp'],
                c['url']
            ) for c in commits
        ]
    )

def commits_keyboard(commits):
    return {
        "inline_keyboard": [
            [
                dict(
                    text=c['message'],
                    url=c['url']
                ) for c in commits
            ]
        ]
    }


def h_push(data):
    template = """
    Проект: {project_name} ({project_web_url})
    Тип события: push
    Пользователь: {push_initiator_name} ({push_initiator_username})
    Коммиты: {commits_description}
    """

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        push_initiator_name=data['user_name'],
        push_initiator_username=data['user_username'],
        commits_description=commits_description(data['commits']),
    )
    return {
        'chat_id': 3148864, # chat_id with me
        'text': message,
        'reply_markup': commits_keyboard(data['commits'])
    }