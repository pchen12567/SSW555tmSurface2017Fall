def error_constructor(error, scope, user_story, line_number, _id, description):
    return {'error': error,
            'scope': scope,
            'user_story': 'US' + str(user_story),
            'line_number': line_number,
            'id': _id,
            'description': description}
