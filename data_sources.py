import yfinance as yf

# Función para obtener los datos de los activos
def obtener_datos_activos(activo):
    # Conectar con Yahoo Finance
    stock = yf.Ticker(activo)
    historial = stock.history(period="1d")  # Datos del último día

    # Extraer las características necesarias
    precios = historial[['Open', 'High', 'Low', 'Close']].values[-1]  # Últimos valores
    return precios  # Devuelve los datos en un formato adecuado (array numérico)
