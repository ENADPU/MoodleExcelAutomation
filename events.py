from user_data import get_user_data
from course_data import get_course_data

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
        userid = data.get('userid')
        courseid = data.get('courseid')

        user_data = get_user_data(userid)
        course_name = get_course_data(courseid)

        user_fullname = user_data.get('fullname', 'Usuário não encontrado')

        if userid is None or courseid is None:
            raise ValueError(f'Missing required fields: userid={userid}, courseid={courseid}')

        print(f'Inscrição do usuário {user_fullname} (ID: {userid}) no curso {course_name} (ID:{courseid}), foi atualizada.')

        return True

    except ValueError as ve:
        print(f'ValueError: {str(ve)}')
        return False
