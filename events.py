from flask import jsonify
from get_data import get_user_data, get_course_data

def user_enrolment_created(data):
    try:
        # Extract specific fields
        studentid = data.get('relateduserid')
        courseid = data.get('courseid')
        enrol_type = data.get('other', {}).get('enrol')
        user_data = get_user_data(studentid)
        course_name = get_course_data(courseid)

        if enrol_type == 'manual':
            user_name = user_data.get('nome_completo')
            print(jsonify(user_data))
            print(f'O estudante {user_name} foi inserido ao curso {course_name} manualmente')

        return studentid

    except ValueError as ve:
        print(f"Erro ao processar dados do webhook: {str(ve)}")
        return None


def user_enrolment_updated(data):
    try:
        # Extrai campos específicos do evento
        studentid = data.get('relateduserid')
        courseid = data.get('courseid')

        # Obtém os dados do estudante
        user_data = get_user_data(studentid)
        course_data = get_course_data(courseid)

        # Extrai o nome completo do estudante
        fullname = user_data.get('nome_completo')

        # Valida os campos necessários
        if studentid is None or courseid is None:
            raise ValueError(f'Missing required fields: studentid={studentid}, courseid={courseid}')

        # Log para depuração
        print(f'Inscrição atualizada para o estudante {fullname} com ID {studentid} no curso {course_data} com ID {courseid}.')
        return studentid

    except ValueError as ve:
        print(f'Erro ao processar dados do webhook: {str(ve)}')
        return None
