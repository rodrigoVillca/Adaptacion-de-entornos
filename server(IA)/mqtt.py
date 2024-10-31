import paho.mqtt.client as mqtt

# Configuración del broker Mosquitto (localhost es donde corre Mosquitto)
broker_address = "localhost"  # dirección del broker
client = mqtt.Client()  # Nombre del cliente

def on_connect(client, userdata, flags, rc):
    print(f"Conectado con el código de resultado {rc}")

client.on_connect = on_connect
client.connect(broker_address)
client.loop_start()  # Comienza el buckle

def mover_carrito():
    """
    Función para enviar el comando 'movete 1 metro' al carrito.
    """
    topic = "carrito"
    mensaje = "movete 1 metro"
    
    # Publicar el mensaje en el topic 'carrito'
    client.publish(topic, mensaje)
    
    return {"mensaje": "Comando enviado", "topic": topic, "mensaje_enviado": mensaje}