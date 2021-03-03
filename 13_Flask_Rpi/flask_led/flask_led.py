from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

relay_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setwarnings(False)

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "." # . 代表在程式執行的當前目錄，加入這個設定讓程式知道我的 templates 在這邊
@app.route("/", methods=['GET'])
def main():
    return render_template("main.html")

@app.route("/on")
def on():
    GPIO.output(relay_pin, GPIO.HIGH)
    return render_template("main.html")

@app.route("/off")
def off():
    GPIO.output(relay_pin, GPIO.LOW)
    return render_template("main.html")

@app.route("/shining")
def shining():
    while True:
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(.5)
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080, debug = True, threaded = True)