from flask import Flask, request, jsonify
import config
import requests as r
from get_data import get_user_data, get_course_data, format_data
from events import user_enrolment_updated

app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG

# Webhook para receber dados do Moodle
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Verifica o tipo de conteúdo da requisição
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return jsonify({'status': 'error', 'message': 'Unsupported Content-Type'}), 400

        data = request.get_json()

        # Verifica o tipo de evento
        eventname = data.get('eventname')
        if eventname == '\\core\\event\\user_enrolment_updated':
            # Quando a inscrição é atualizada, enviar dados para o Power Automate
            studentid = user_enrolment_updated(data)
            if studentid:
                # Enviar dados para o Power Automate
                send_data_to_power_automate(studentid, data.get('courseid'))

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

def send_data_to_power_automate(studentid, courseid):
    try:
        # Recupera os dados do estudante
        user_data = get_user_data(studentid)
        
        # Recupera o nome do curso
        course_name = get_course_data(courseid)

        # Formata os dados conforme solicitado
        formatted_data = format_data(user_data)
        
        # Adiciona o nome do curso aos dados formatados
        formatted_data['course_fullname'] = course_name

        # URL do fluxo do Power Automate
        url = config.POWER_AUTOMATE_URL
        headers = {
            "Content-Type": "application/json",
        }

        # Envia a requisição para o Power Automate
        response = r.post(str(url), headers=headers, json=formatted_data)

        if response.status_code == 200:
            print("Dados enviados com sucesso para o Power Automate.")
        else:
            print(f"Erro ao enviar dados: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Erro ao enviar dados para o Power Automate: {str(e)}")

if __name__ == '__main__':
    app.run(port=config.PORT, debug=config.DEBUG)
