from flask import Flask, request, Response
import led_functions as led

app = Flask(__name__)
LED_handler = None

@app.route("/")
def handle_default():
    print("No Arguments Given!")
    return "This is the LED server!"

@app.route('/LED')
def handle_led():
    status = request.args.get('status')
    color = request.args.get('color')
    intensity = request.args.get('intensity')
    
    print("Changed LED Configuration:\n\tStatus: ", status, "\n\tColor: ", color, "\n\tIntensity: ", intensity)

    LED_handler.set_status(status)
    LED_handler.set_color(color)
    LED_handler.set_intensity(int(intensity))
    LED_handler.update()
    return "LED SET"

if __name__ == "__main__":
    LED_handler = led.PI_LED()
    app.run(host='0.0.0.0', port=8081, debug=False)
