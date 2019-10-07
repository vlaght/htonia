import json


def read_button(data):
    reply_markup_body = {
        "inline_keyboard": [
            [
                {
                    'text': 'Читать 👀',
                    'url': data['object_attributes']['url'],
                }
            ]
        ]
    }
    return json.dumps(reply_markup_body)


def h_commit_comment(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: комментарии к коммиту 💩\nО чём был коммит: {commit_message}\nКомментирует: {user_name} ({user_username}) "

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        user_name=data['user']['name'],
        commit_message=data['commit']['message'],
        user_username=data['user']['username'],
    )

    return {
        'text': message,
        'reply_markup': read_button(data)
    }


def h_merge_request_comment(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: комментарии к мердж-реквесту 💩\nЗаголовок МР: {title}\nВетки: {source_branch} ➡️ {target_branch} \nКомментирует: {user_name} ({user_username}) "

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        user_name=data['user']['name'],
        user_username=data['user']['username'],
        title=data['merge_request']['title'],
        source_branch=data['merge_request']['source_branch'],
        target_branch=data['merge_request']['target_branch'],
    )

    return {
        'text': message,
        'reply_markup': read_button(data)
    }


def h_issue_comment(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: комментарии к тикету 💩\nТикет: {issue_title}\nКомментирует: {user_name} ({user_username}) "

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        user_name=data['user']['name'],
        issue_title=data['issue']['title'],
        user_username=data['user']['username'],
    )

    return {
        'text': message,
        'reply_markup': read_button(data)
    }


def h_snippet_comment(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: комментарии к сниппету 💩\nСниппет: {snippet_title}\nКомментирует: {user_name} ({user_username}) "

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        user_name=data['user']['name'],
        snippet_title=data['snippet']['title'],
        user_username=data['user']['username'],
    )

    return {
        'text': message,
        'reply_markup': read_button(data)
    }


def h_comment(data):
    resolvers = {
        'commit': h_commit_comment,
        'mergerequest': h_merge_request_comment,
        'issue': h_issue_comment,
        'snippet': h_snippet_comment
    }
    noteable_type = data['object_attributes']['noteable_type'].lower()
    return resolvers[noteable_type](data)
