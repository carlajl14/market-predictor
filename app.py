import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suprimir los registros de TensorFlow

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from data_sources import obtener_datos_activos, obtener_datos_multiples_activos  # Importar las funciones para obtener datos

app = Flask(__name__)

# Cargar el modelo LSTM
model = tf.keras.models.load_model("lstm_model.h5")

# Compilar el modelo para eliminar la advertencia
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Endpoint para predicciones automatizadas (basadas en un activo)
@app.route('/predict/<activo>', methods=['GET'])
def predict(activo):
    try:
        # Paso 1: Obtener los datos del activo automáticamente
        datos = obtener_datos_activos(activo)  # Recuperar datos desde Yahoo Finance

        # Paso 2: Formatear los datos para el modelo
        inputs = np.array(datos).reshape(1, -1, 1)  # Ajusta al formato esperado por el modelo LSTM

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

# Endpoint para realizar predicciones de una lista de activos
@app.route('/predict_multiple', methods=['POST'])
def predict_multiple():
    try:
        # Obtener la lista de activos desde el cuerpo de la solicitud
        activos = request.json.get('activos', [])
        resultados = []

        # Filtrar los activos para incluir solo las criptomonedas que contengan "EUR"
        activos_filtrados = [activo for activo in activos if "EUR" in activo]

        # Obtener los datos de múltiples activos
        datos_activos = obtener_datos_multiples_activos(activos_filtrados)

        for activo, datos in datos_activos.items():
            if "error" in datos:
                resultados.append({"activo": activo, "error": datos["error"]})
            else:
                try:
                    inputs = np.array(datos).reshape(1, -1, 1)  # Ajusta al formato esperado por el modelo LSTM
                    prediction = model.predict(inputs)
                    recomendacion = np.argmax(prediction, axis=1)  # 0: Vender, 1: Mantener, 2: Comprar
                    opciones = {0: "Vender", 1: "Mantener", 2: "Comprar"}
                    resultados.append({
                        "activo": activo,
                        "recomendacion": opciones[recomendacion[0]],
                        "probabilidades": prediction.tolist()
                    })
                except Exception as e:
                    resultados.append({"activo": activo, "error": str(e)})

        return jsonify(resultados)
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
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=False)