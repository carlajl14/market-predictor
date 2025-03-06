# Market Predictor

Este proyecto es una aplicación Flask que utiliza un modelo de TensorFlow para predecir recomendaciones de compra, venta o mantenimiento de activos financieros basados en datos obtenidos de Yahoo Finance.

## Estructura del Proyecto

- `app.py`: Archivo principal que contiene la aplicación Flask y los endpoints para predicciones y obtención de datos.
- `data_sources.py`: Contiene las funciones para obtener datos de activos desde Yahoo Finance.
- `Dockerfile`: Archivo para construir la imagen Docker de la aplicación.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.
- `README.md`: Este archivo, que contiene información sobre el proyecto.

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/carlajl14/market-predictor.git
    cd market-predictor
    ```

2. Construye la imagen Docker:
    ```sh
    docker build -t market-predictor .
    ```

3. Ejecuta el contenedor Docker:
    ```sh
    docker run -p 8080:8080 market-predictor
    ```

## Instalación de Dependencias

Después de clonar el repositorio, instala las dependencias necesarias ejecutando el siguiente comando:

```sh
pip install -r requirements.txt
```

## Uso

### Endpoint para predicciones de un activo

- **URL:** `/predict/<activo>`
- **Método:** `GET`
- **Descripción:** Realiza una predicción basada en los datos del activo especificado.
- **Ejemplo de respuesta:**
    ```json
    {
        "activo": "AAPL",
        "recomendacion": "Comprar",
        "probabilidades": [[0.1, 0.2, 0.7]]
    }
    ```

### Endpoint para predicciones de múltiples activos

- **URL:** `/predict_multiple`
- **Método:** `POST`
- **Descripción:** Realiza predicciones basadas en los datos de una lista de activos especificados.
- **Ejemplo de solicitud:**
    ```json
    {
        "activos": ["AAPL", "GOOGL", "BTC-USD", "ETH-USD"]
    }
    ```
- **Ejemplo de respuesta:**
    ```json
    [
        {
            "activo": "AAPL",
            "recomendacion": "Comprar",
            "probabilidades": [[0.1, 0.2, 0.7]]
        },
        {
            "activo": "GOOGL",
            "recomendacion": "Mantener",
            "probabilidades": [[0.3, 0.5, 0.2]]
        },
        {
            "activo": "BTC-USD",
            "recomendacion": "Vender",
            "probabilidades": [[0.6, 0.3, 0.1]]
        },
        {
            "activo": "ETH-USD",
            "recomendacion": "Comprar",
            "probabilidades": [[0.2, 0.1, 0.7]]
        }
    ]
    ```

### Endpoint para obtener datos de activos

- **URL:** `/get_stock_data/<activo>`
- **Método:** `GET`
- **Descripción:** Obtiene los datos del activo especificado desde Yahoo Finance.
- **Ejemplo de respuesta:**
    ```json
    {
        "activo": "AAPL",
        "datos": [150.0, 155.0, 148.0, 152.0]
    }
    ```

## Dependencias

- Flask
- TensorFlow
- NumPy
- yfinance

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

Proyecto creado por Carla Jiménez