import paho.mqtt.client as mqtt

# Configuración del broker Mosquitto (localhost es donde corre Mosquitto)
broker_address = "localhost"  # Dirección del broker
client = mqtt.Client()  # Nombre del cliente

# Callback cuando el cliente se conecta al broker
def on_connect(client,userdata,flags, rc):#investigando un poco el "rc" mediante numeros me cuenta
# como esta la conexion con el borker y el cliente pero se maneja con muchos numeros asi q en resumen
 print(f"Conectado con el código de resultado {rc}")#  si el numero q sale es 0 todo esta bien

# Asignamos el callback
client.on_connect = on_connect

def conectar_mqtt():
    """Función para establecer la conexión con el broker y mantener el loop"""
    # Conectar al broker
    client.connect(broker_address)
    # Iniciar el bucle de MQTT (en el hilo principal)
    client.loop_start()

def mover_carrito():#Función para enviar el comando 'movete 1 metro' al carrito.
                     
    topic = "carrito"
    mensaje = "movete 1 metro"
    
    
    if client.is_connected(): # aca me aseguro de que el cliente esté conectado antes de publicar
        client.publish(topic, mensaje)
        return {"mensaje": "Comando enviado", "topic": topic, "mensaje_enviado": mensaje}
    else:
        return {"error": "No se pudo conectar al broker", "broker": broker_address}

# Conectar al broker MQTT
conectar_mqtt()