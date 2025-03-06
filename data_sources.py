import yfinance as yf

# Función para obtener los datos de los activos
def obtener_datos_activos(activo):
    # Conectar con Yahoo Finance
    stock = yf.Ticker(activo)
    historial = stock.history(period="60d")  # Datos del último día

    # Extraer las características necesarias
    precios = historial[['Open', 'High', 'Low', 'Close']].values[-1]  # Últimos valores
    return precios  # Devuelve los datos en un formato adecuado (array numérico)

# Función para obtener los datos de múltiples activos
def obtener_datos_multiples_activos(activos):
    datos_activos = {}
    for activo in activos:
        try:
            datos_activos[activo] = obtener_datos_activos(activo)
        except Exception as e:
            datos_activos[activo] = {"error": str(e)}
    return datos_activos