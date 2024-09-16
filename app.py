from flask import Flask, request, jsonify
import config
import json
from user_data import get_user_data
from course_data import get_course_data
from events import user_enrolment_created, user_enrolment_updated

app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG

@app.route('/webhook', methods=['POST'])
def webhook():
        # Check if content-type is application/json
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            raise ValueError("Unsupported Content-Type: ", content_type)

        data = request.get_json()

        # Verifica o tipo de evento
        eventname = data.get('eventname')
        print(eventname)
        if eventname == r'\core\event\user_enrolment_created':
            userid = user_enrolment_created(data)
            if userid:
                user_data = get_user_data(userid)
                print(json.dumps(user_data, indent=4, ensure_ascii=False, sort_keys=True))
        elif eventname == r'\core\event\user_enrolment_updated':
            enrol_update = user_enrolment_updated(data)
            print(json.dumps(enrol_update, indent=4, ensure_ascii=False, sort_keys=True))

        # Get course data
        courseid = data.get('courseid')
        course_name = get_course_data(courseid)
        print(course_name)

        # Return success response
        return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=config.PORT, debug=config.DEBUG)
