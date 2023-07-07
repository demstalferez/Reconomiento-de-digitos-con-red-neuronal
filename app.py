import gradio as gr
import tensorflow as tf
import numpy as np

modelo = tf.keras.models.load_model('numeros.h5')

def clasificar_imagen(img):
    img = img.reshape(1, 28, 28, 1).astype('float32') / 255
    predicciones = modelo.predict(img)
    digito_predicho = np.argmax(predicciones)
    
    return str(digito_predicho)

interfaz = gr.Interface(fn=clasificar_imagen, inputs="sketchpad", outputs="label")
interfaz.launch()


