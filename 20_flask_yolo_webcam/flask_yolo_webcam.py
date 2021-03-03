import os
import sys
import time
from flask import Flask, render_template
sys.path.append("/home/pi/darknet/")
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

def default_yolo(): 
    path = os.getcwd()
    imgpath = '/home/pi/darknet/data/dog.jpg'
    output_path = '/home/pi/d28/flask_webcam/static/prediction.jpg'
    configPath = "/home/pi/darknet/cfg/yolov4-tiny.cfg"
    weightPath = "/home/pi/darknet/yolov4-tiny.weights"
    metaPath= "/home/pi/darknet/cfg/coco.data"
    
    os.chdir('/home/pi/darknet')
    ### by pychih
    import darknet
    from darknet_images import load_images
    from darknet_images import image_detection
    network, class_names, class_colors = darknet.load_network(
        configPath,
        metaPath,
        weightPath,
        1  # batch size
    )
    prev_time = time.time()
    image, detections = image_detection(
        imgpath, network, class_names, class_colors, 0.25  # threshold
        )
    darknet.print_detections(detections, True)
    end_time = time.time()
    fps = (1/(end_time - prev_time))
    print("FPS: {}".format(fps))
    print("inference time : {}".format(end_time - prev_time))
    os.chdir(path)
    return detections

def default_display():
    ans = default_yolo()
    replay = str()
    for label, confidence, bbox in ans:
        replay += "{} : {}%".format(label, confidence)
    return replay

if __name__ == "__main__":
    reply = default_display()
    @app.route("/")
    def temp():
        return reply
    
    @app.route('/index')
    def show_index():
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'dog.jpg')
        return render_template("index.html", user_image = full_filename)
    app.run(host = "192.168.0.103", port = 8080, debug = True, threaded = True)