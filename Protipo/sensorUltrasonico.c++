int u_distancia(int TriggerPin, int EchoPin) {
   long duration, distanceCm;


   // Preparar el Trigger
   digitalWrite(TriggerPin, LOW); // Asegurarse de que el Trigger está en LOW
   delayMicroseconds(2); // Esperar 2 microsegundos
   digitalWrite(TriggerPin, HIGH); // Enviar un pulso de disparo
   delayMicroseconds(10); // Mantener el pulso por 10 microsegundos
   digitalWrite(TriggerPin, LOW); // Terminar el pulso


   // Leer el tiempo del pulso de eco
   duration = pulseIn(EchoPin, HIGH); // Medir el tiempo que tarda en volver el pulso


   // Calcular la distancia en centímetros
   distanceCm = duration * 0.0343 / 2; // Velocidad del sonido: 0.0343 cm/microsegundo


   return distanceCm; // Devolver la distancia en centímetros
}


void setup() {
   // Configurar los pines del sensor ultrasónico
   pinMode(6, OUTPUT); // Pin Trigger
   pinMode(7, INPUT);  // Pin Echo


   Serial.begin(9600); // Inicializar la comunicación serial
}


void loop() {
   // Obtener y mostrar la distancia
   int distancia = u_distancia(6, 7); // Medir la distancia
   Serial.print("Distancia: "); // Imprimir el mensaje
   Serial.print(distancia); // Imprimir la distancia
   Serial.println(" cm"); // Imprimir las unidades
   delay(5000); // Esperar 1 segundo antes de la próxima medición
}
