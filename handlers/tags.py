def h_tag_push(data):
    template = "Куда: {project_name} ({project_web_url})\nЧто: tag push {ref}\nКто: {push_initiator_name}"

    message = template.format(
        project_name=data['project']['name'],
        project_web_url=data['project']['web_url'],
        ref=data['ref'],
        push_initiator_name=data['user_name'],
    )
    return {
        'text': message,
    }
