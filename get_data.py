from requests import request
import config

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
            return extract_user_data(user_data)
        else:
            return f'Usuário com id={userid} não encontrado'

    except ValueError as ve:
        return f'Erro de requisição: {str(ve)}'

def get_course_data(courseid):
    try:
        url = config.MOODLE_API_URL
        params = {
            "wstoken": config.MOODLE_API_TOKEN,
            "wsfunction": "core_course_get_courses",
            "moodlewsrestformat": "json",
            "options[ids][0]": courseid
        }

        response = request("GET", str(url), params=params)
        data = response.json()[0]

        course_name = data.get('fullname')

        return course_name

    except ValueError as ve:
        return f'Erro de requisição {str(ve)}'


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


def format_data(data):
    # Formatar CPF
    cpf = data.get('username', '?')
    if len(cpf) == 11 and cpf.isdigit():
        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        cpf = "?"

    # Formatar Nome
    name = data.get('fullname', 'Nome Não Encontrado')
    name_parts = name.split()
    prepositions = ['de', 'da', 'do', 'das', 'dos']
    formatted_name = ' '.join([part.capitalize() if part.lower() not in prepositions else part.lower() for part in name_parts])
    
    municipio = data.get('municipio', 'Município Não Encontrado')
    municipio_parts = municipio.split()
    formatted_municipio = ' '.join([part.capitalize() for part in municipio_parts])

    # Abreviar Vínculo
    vinculo_map = {
        'Estagiário': 'E',
        'Voluntário': 'V',
        'Defensor Público': 'D',
        'Servidor / Empregado Público': 'S',
        'Terceirizado': 'T',
        'Público Externo': 'P/Ext'
    }
    vinculo = data.get('vinculo', 'P/Ext')
    vinculo_abbr = vinculo_map.get(vinculo, 'P/Ext')

    # Extrair UF
    uf = data.get('uf', '')
    uf_parts = uf.split(' - ')
    uf_abbr = uf_parts[-1] if len(uf_parts) > 1 else uf

    # Formatar Gênero
    genero_map = {
        'Masculino': 'M',
        'Feminino': 'F'
    }
    genero = data.get('genero', '')
    genero_abbr = genero_map.get(genero, '')

    # Montar os dados formatados
    formatted_data = {
        'username': cpf,
        'fullname': formatted_name,
        'vinculo': vinculo_abbr,
        'uf': uf_abbr,
        'genero': genero_abbr,
        'etinia': data.get('etinia', ''),
        'email': data.get('email', ''),
        'municipio': formatted_municipio
    }
    print(f"Formatted data: {formatted_data}")

    return formatted_data
