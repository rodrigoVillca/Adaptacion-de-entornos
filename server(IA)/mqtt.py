import paho.mqtt.client as mqtt

# Configuración del broker Mosquitto (localhost es donde corre Mosquitto)
broker_address = "localhost"  # Usa la IP de tu broker si no es local
client = mqtt.Client("FastAPI_server")  # El nombre del cliente es arbitrario
client.connect(broker_address)

def mover_carrito():
    """
    Endpoint para enviar el comando 'movete 1 metro' al carrito.
    """
    topic = "carrito"
    mensaje = "movete 1 metro"
    
    # Publicar el mensaje en el topic 'carrito'
    client.publish(topic, mensaje)
    
    return {"mensaje": "Comando enviado", "topic": topic, "mensaje_enviado": mensaje}
