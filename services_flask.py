from flask import Flask, request, Response
from functools import wraps
import argparse as ap
import requests
import services

app = Flask(__name__)
LED_IP = ""
LED_Port = "8081"

def check_auth(username, password):
    #Here given userbame returns password
    return services.get_password(username) == password

def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/")
@requires_auth
def handle_default():
    print("No Arguments Given!")
    return "No Arguments Given!"

@app.route('/LED')
@requires_auth
def handle_led():
    status = request.args.get('status','')
    color = request.args.get('color','')
    intensity = request.args.get('intensity','')

    print(status)
    print(color)
    print(intensity)

    request_str = "http://"+LED_IP+":"+LED_Port+"/LED?status=" + str(status) + "&color=" + str(color) + "&intensity=" + str(intensity)
    return requests.get(request_str)

if __name__ == "__main__":
    parser = ap.ArgumentParser(description="Launch the services pi for assignment 3")
    parser.add_argument('-led',action='store',dest='IP',type=str,nargs='+',help="IP led pi is hosting",default='localhost',required=False)
    args = parser.parse_args()

    LED_IP = "".join(args.IP)
    LED_Port = "8081"

    app.run(host='0.0.0.0', port=8081, debug=False)
