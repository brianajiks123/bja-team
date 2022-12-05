import os, glob2, cv2, numpy as ny, requests, time, json, pdfkit, subprocess
from flask import Flask, render_template, url_for, request, session, flash, redirect, make_response
from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from lnp.lnp import valDetect
from PIL import Image
from datetime import datetime
from datetime import date
from pdfkit.api import configuration

# Setting Upload
up_dir = os.path.join('static', 'uploads')
os.makedirs(up_dir, exist_ok=True)
acc_ext = set(['png', 'jpg', 'jpeg'])
uploaded = False

# Setting API Theos
url_theos = 'https://inf-ec5ba874-ad3b-422f-a3c2-2f3c1251dbfd-no4xvrhsfq-uc.a.run.app/detect'
ocr_model = 'large'
ocr_class = 'license-plate'

# Setting Flask
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "BJA_Team"
app.config['UPLOAD_IMG'] = up_dir

# Setting wkhtmlpdf
if 'DYNO' in os.environ:
    app.config['WKHTMLTOPDF_CMD'] = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], stdout=subprocess.PIPE).communicate()[0].strip()
else:
    app.config['MYDIR'] = os.path.dirname(__file__)    
    app.config['WKHTMLTOPDF_CMD'] = os.path.join(app.config['MYDIR'] + "/static/executables/bin/", "wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=app.config['WKHTMLTOPDF_CMD'])

# Class Form
class Form(FlaskForm):
    img_input = FileField(name="file")
    send_btn = SubmitField('KIRIM')
    process_btn = SubmitField('DETEKSI')
    save_btn = SubmitField('SIMPAN PDF', name="save")

# Function File Extension
def allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in acc_ext

# Function License Number Plate Detection
def detect_object(img_bytes, url, ocr_model, ocr_classes, fallback_url=None, conf_thres=0.25, iou_thres=0.45, retries=10, delay=0):
    response = requests.post(url, data={'conf_thres':conf_thres, 'iou_thres':iou_thres, 'ocr_model':ocr_model, 'ocr_classes':ocr_classes}, files={'image':img_bytes})
    if response.status_code in [200, 500]:
        data = response.json()
        if 'error' in data:
            print('[!]', data['message'])
        else:
            return data
    elif response.status_code == 403:
        print('[!] you reached your monthly requests limit. Upgrade your plan to unlock unlimited requests.')
    elif retries > 0:
        if delay > 0:
            time.sleep(delay)
        return detect_object(img_bytes, url=fallback_url if fallback_url else url, retries=retries-1, delay=2)
    return []

# Function Crop Image
def crop(image, detection):
    x = detection['x']
    y = detection['y']
    width = detection['width']
    height = detection['height']

    return image[y:y+height, x:x+width]

# Route /
@app.route('/')
def home():
    title = 'BERANDA'
    form = Form()

    if os.listdir(up_dir):
        files = glob2.glob('static\\uploads\\*')

        for f in files:
            os.remove(f)

    return render_template('home.html', title=title, form=form, image="")

@app.route('/', methods=["POST"])
def read():
    title = 'BERANDA'
    form = Form()

    if form.validate_on_submit():
        up_img = request.files['file']

        if up_img.filename == '':
            flash('Failed to send file.')

            return redirect('/')

        if up_img and allowedFile(up_img.filename):
            img_name = secure_filename(up_img.filename)
            up_img.save(os.path.join(app.config['UPLOAD_IMG'], img_name))
            uploaded = True
            session['UPLOAD_IMG_PATH'] = os.path.join(app.config['UPLOAD_IMG'], img_name)
        else:
            flash('Only accepts png, jpg, jpeg, gif files.')

            return redirect('/')
    
    if session['UPLOAD_IMG_PATH'] != '':
        img_path = session.get('UPLOAD_IMG_PATH', None)

        return render_template('home.html', title=title, form=form, image=img_path, info=uploaded)
    else:
        return redirect('/')

# Route Detect
@app.route('/detect', methods=["POST"])
def process():
    title = 'DETEKSI'
    form = Form()

    if form.validate_on_submit():
        img_path = session.get('UPLOAD_IMG_PATH', None)
        img_read = cv2.imread(img_path)
            
        with open(img_path, 'rb') as img:
            img_bytes = img.read()

        detections = detect_object(img_bytes, url=url_theos, ocr_model=ocr_model, ocr_classes=ocr_class)

        if len(detections):
            if len(detections) > 1:
                flash("Failed to detection a license plate.")
                return redirect('/')
            else:
                for detection in detections:
                    lnp = detection['text'].split(" ")

                    if len(lnp) == 3:
                        crop_img = crop(img_read, detection)
                        img_array = Image.fromarray(crop_img)
                        now = str(datetime.now())
                        img_name = now + ".jpg"
                        img_name = img_name.replace(":", "_")
                        img_array.save(os.path.join(app.config['UPLOAD_IMG'], img_name))
                        session['UPLOAD_IMG_PATH'] = os.path.join(app.config['UPLOAD_IMG'], img_name)
                        img_path = session.get('UPLOAD_IMG_PATH', None)
                        country, region, number = valDetect(detection['text'])

                        return render_template('detect.html', title=title, form=form, image=img_path, result=[detection['text'], country, region, number])
                    else:
                        flash("The image isn't clear.")

                        return redirect('/')
        else:
            flash("The image doesn't contain a license plate or isn't clear.")

            return redirect('/')

# Route Save PDF
@app.route('/result', methods=["POST"])
def savepdf():
    title = 'PDF'
    form = Form()

    if form.validate_on_submit():
        todays_date = date.today()
        year = todays_date.year
        code_plate = request.form.get("code_plate")
        country = request.form.get("country")
        city = request.form.get("city")
        number_plate = request.form.get("number_plate")
        data_lnp = [code_plate, country, city, number_plate]
        rendered_html = render_template("generate_pdf.html", title=title, data=data_lnp, year=year)

        #Setting PDF
        options = {
            "enable-local-file-access": "",
            "orientation": "landscape",
            "page-size": "A4",
            "encoding": "UTF-8",
            'no-outline': None
        }
        pdf = pdfkit.from_string(input=rendered_html, options=options, configuration=config, verbose=False)
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "inline; filename=result.pdf"

        return response
    return render_template("detect.html")

if __name__ == "__main__":
    app.run()