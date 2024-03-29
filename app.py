from flask import Flask, render_template, request, redirect
import utils  # Import helper functions

app = Flask(__name__)

# Configure allowed extensions for uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/wave')
def wave_form():
  return render_template('wave.html')

@app.route('/wave', methods=['POST'])
def wave_image():
  if 'file' not in request.files:
    return redirect(request.url)
  file = request.files['file']
  if file.filename == '':
    return redirect(request.url)
  if file and allowed_file(file.filename):
    filename = "uploads/"+file.filename
    file.save("static/"+filename)  # Save image locally (temporary)
    prediction = utils.wave_predict("static/"+filename)  # Call prediction function
    return render_template('wave.html', filename=filename, prediction=prediction)
  else:
    return redirect(request.url)


@app.route('/mri')
def mri_form():
  return render_template('mri.html')


@app.route('/spiral')
def spiral_form():
  return render_template('spiral.html')

@app.route('/spiral', methods=['POST'])
def spiral_image():
  if 'file' not in request.files:
    return redirect(request.url)
  file = request.files['file']
  if file.filename == '':
    return redirect(request.url)
  if file and allowed_file(file.filename):
    filename = "uploads/"+file.filename
    file.save("static/"+filename)  # Save image locally (temporary)
    prediction = utils.spiral_predict("static/"+filename)  # Call prediction function
    return render_template('spiral.html', filename=filename, prediction=prediction)
  else:
    return redirect(request.url)
  
  

if __name__ == '__main__':
  app.run(debug=True)