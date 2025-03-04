from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Cargar el modelo del TensorFlow Model Garden ajustado
model = tf.keras.models.load_model("")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Datos enviados por el cliente
        inputs = np.array(data['inputs']).reshape(1, -1)  # Ajusta según el modelo

        # Realizar predicción
        prediction = model.predict(inputs)
        recomendacion = np.argmax(prediction, axis=1)  # Comprar/Mantener/Vender

        opciones = {0: "Vender", 1: "Mantener", 2: "Comprar"}
        return jsonify({"recomendacion": opciones[recomendacion[0]]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)