from requests import request
import config
import json

def get_user_data(userid):
    try:
        url = config.MOODLE_API_URL
        params = {
                "wstoken": config.MOODLE_API_TOKEN,
                "wsfunction": "core_user_get_users",
                "criteria[0][key]": "id",
                "criteria[0][value]": userid,
                "moodlewsrestformat": "json",
                }

        response = request("GET", str(url), params=params)
        data = response.json()

        if 'users' in data and len(data['users']) > 0:
            user_data = data.get('users')[0]
            print(json.dumps(user_data, indent=4, ensure_ascii=False, sort_keys=True))
            return extract_user_data(user_data)
        else:
            return f'Usuário com id={userid} não encontrado'

    except ValueError as ve:
        return f'Erro de requisição: {str(ve)}'


def extract_user_data(user_data):
    result = {
            'username': user_data.get('username', '?'),
            'fullname': user_data.get('fullname', '?'),
            'email': user_data.get('email', '?'),
            }

    custom_fields = user_data.get('customfields', [])

    interesting_fields = ['etinia', 'genero', 'vinculo', 'municipio', 'uf', 'nome_completo']

    for field in custom_fields:
        if field.get('shortname') in interesting_fields:
            value = field.get('value', '')

            if field.get('type') == 'menu' or field.get('type') == 'text':
                if '{mlang pt_br}' in value:
                    try:
                        pt_br_value = value.split('{mlang pt_br}')[1].split('{mlang')[0]
                        result[field['shortname']] = pt_br_value
                    except IndexError:
                        result[field['shortname']] = "Valor não encontrado"
                else:
                   result[field['shortname']] = value
            else:
                result[field['shortname']] = value
                                                                            
    return result
