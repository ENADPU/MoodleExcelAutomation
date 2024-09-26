from get_data import get_user_data, get_course_data

def user_enrolment_created(data):
    try:
        # Extract specific fields
        userid = data.get('userid')
        courseid = data.get('courseid')
        timecreated = data.get('timecreated')
        eventname = data.get('eventname')
        enrol_type = data.get('other', {}).get('enrol')

        # Validate fields are not None (check if required fields are missing)
        if userid is None or courseid is None or timecreated is None or eventname is None or enrol_type is None:
            raise ValueError(f"Missing required fields: userid={userid}, courseid={courseid}, timecreated={timecreated}, eventname={eventname}, enrol_type={enrol_type}")

        # Log the received data for debugging
        print(f"Received webhook data: userid={userid}, courseid={courseid}, timecreated={timecreated}, eventname={eventname}, enrol_type={enrol_type}")

        return userid

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
        fullname = user_data.get('fullname')

        # Valida os campos necessários
        if studentid is None or courseid is None:
            raise ValueError(f'Missing required fields: studentid={studentid}, courseid={courseid}')

        # Log para depuração
        print(f'Inscrição atualizada para o estudante {fullname} com ID {studentid} no curso {course_data} com ID {courseid}.')
        return studentid

    except ValueError as ve:
        print(f'Erro ao processar dados do webhook: {str(ve)}')
        return None

