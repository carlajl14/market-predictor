from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from data_sources import obtener_datos_activos  # Importar la función para obtener datos

app = Flask(__name__)

# Cargar el modelo del TensorFlow Model Garden ajustado
model = tf.keras.models.load_model("best_model_90_2.keras")

# Endpoint para predicciones automatizadas (basadas en un activo)
@app.route('/predict/<activo>', methods=['GET'])
def predict(activo):
    try:
        # Paso 1: Obtener los datos del activo automáticamente
        datos = obtener_datos_acciones(activo)  # Recuperar datos desde Yahoo Finance

        # Paso 2: Formatear los datos para el modelo
        inputs = np.array(datos).reshape(1, -1)  # Ajusta al formato esperado por el modelo

        # Paso 3: Realizar predicción usando el modelo
        prediction = model.predict(inputs)
        recomendacion = np.argmax(prediction, axis=1)  # 0: Vender, 1: Mantener, 2: Comprar

        # Paso 4: Preparar la respuesta
        opciones = {0: "Vender", 1: "Mantener", 2: "Comprar"}
        return jsonify({
            "activo": activo,
            "recomendacion": opciones[recomendacion[0]],
            "probabilidades": prediction.tolist()
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# Endpoint: Obtener datos de los activos desde Yahoo Finance
@app.route('/get_stock_data/<activo>', methods=['GET'])
def get_stock_data(activo):
    try:
        # Usar la función de data_sources.py para obtener datos del activo
        datos = obtener_datos_activo(activo)
        return jsonify({"activo": activo, "datos": datos.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)