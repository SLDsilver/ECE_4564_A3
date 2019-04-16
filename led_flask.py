from flask import Flask, request, Response
import led

app = Flask(__name__)
LED_handler = None

@app.route("/")
def handle_default():
    print("No Arguments Given!")
    return "No Arguments Given!"

@app.route('/LED')
def handle_led():
    status = request.args.get('status')
    color = request.args.get('color')
    intensity = request.args.get('intensity')

    LED_handler.set_status(status)
    LED_handler.set_color(color)
    LED_handler.set_intensity(int(intensity))
    LED_handler.update
    return "LED SET"

if __name__ == "__main__":
    LED_handler = led.PI_LED()
    app.run(host='0.0.0.0', port=8081, debug=True)
