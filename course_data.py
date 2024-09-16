from requests import request
import config

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

