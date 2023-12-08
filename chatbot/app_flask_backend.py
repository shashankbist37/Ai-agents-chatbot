from model_autogen import multiagent
from flask import Flask, request, jsonify
from flask_cors import CORS




app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route('/api/chat', methods=['POST'])
def convo():

    data = request.get_json()
    responce = data.get('role_applied')
    aiResponse=multiagent(responce)  

    return jsonify({'aiResponse': aiResponse})


    
if __name__ == '__main__':
    app.run(port=3002,threaded=True)
    
