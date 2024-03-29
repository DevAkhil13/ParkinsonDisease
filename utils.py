from tensorflow import keras
import numpy as np
import os


  
def spiral_predict(filename):
  MODEL_PATH = 'parkinson_spherical.h5'
  model = keras.models.load_model(MODEL_PATH)
  # Preprocess image 
  img_path = filename
  img = keras.preprocessing.image.load_img(img_path, target_size=(299, 299))
  img_array =  keras.preprocessing.image.img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)
  img_array /= 255.0
  # Make predictions
  predictions = model.predict(img_array)
  if predictions[0, 0] > 0.5:
    return 1
  else:
    return 0


def wave_predict(filename):
  MODEL_PATH = 'parkinson_modified_wave.h5'
  model = keras.models.load_model(MODEL_PATH)
  # Preprocess image 
  img_path = filename
  img = keras.preprocessing.image.load_img(img_path, target_size=(299, 299))
  img_array =  keras.preprocessing.image.img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)
  img_array /= 255.0
  # Make predictions
  predictions = model.predict(img_array)
  if predictions[0, 0] > 0.5:
    return 1
  else:
    return 0


# Clean up temporary image 
def cleanup_image(filename):
  os.remove(os.path.join('uploads', filename))