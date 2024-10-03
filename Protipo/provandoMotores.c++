int motorDerecho = 3; 
int motorIzquierdo = 4;


void setup() {


 pinMode(motorDerecho, OUTPUT);
 pinMode(motorIzquierdo, OUTPUT);
}


void loop() {
 analogWrite(motorDerecho, 255); 
 delay(1000);                   
 analogWrite(motorDerecho, 0);   
  // Control del motor izquierdo con velocidad reducida
 analogWrite(motorIzquierdo, 255);
 delay(1000);                     
 analogWrite(motorIzquierdo, 0);  
  // Espera entre ciclos
 delay(2000);
             
}








int motorDerecho = 3; 
int motorIzquierdo = 4;


void setup() {


 pinMode(motorDerecho, OUTPUT);
 pinMode(motorIzquierdo, OUTPUT);
}


void loop() {
 analogWrite(motorDerecho, 255);
 analogWrite(motorIzquierdo, 255);
 delay(3000);                
 analogWrite(motorDerecho, 0);
 analogWrite(motorIzquierdo, 0);
 delay(2000); 






t motorDerecho = 3; 
int motorIzquierdo = 4;


void setup() {


 pinMode(motorDerecho, OUTPUT);
 pinMode(motorIzquierdo, OUTPUT);
}


void loop() {
 digitalWrite(motorIzquierdo, LOW);
 digitalWrite(motorDerecho, LOW);
 analogWrite(motorDerecho, 255);
 analogWrite(motorIzquierdo, 255); 
 delay(3000);                
 analogWrite(motorDerecho, 0);
 analogWrite(motorIzquierdo, 0);
 delay(2000); 
// Dirección hacia atrás para los motores del lado derecho


 // Control del motor izquierdo con velocidad reducida
