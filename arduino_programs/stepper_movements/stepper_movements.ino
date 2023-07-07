#include <Stepper.h>

Stepper motor1(2048,3,5,4,6);



float angulo;
String valor;


void setup() {

  motor1.setSpeed(3);

  Serial.begin(115200);
  while(!Serial){}

    digitalWrite(3,LOW);
    digitalWrite(5,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);


    

}

void loop() {
  
  if(Serial.available()){
    valor = Serial.readStringUntil('\n');

    if(valor == "g"){
      //angulo = 1;

      for(int j = 0; j<1; j++){
        
        for(int i=1;i<=1024;i++){
          
          motor1.step(-1);
          Serial.println(i);
          delay(10);

        }

        for(int i=1;i<=1024;i++){
          
          motor1.step(1);
          Serial.println(i);
          delay(10);

        }


      }
      
      
      digitalWrite(3,LOW);
      digitalWrite(5,LOW);
      digitalWrite(4,LOW);
      digitalWrite(6,LOW);



    }
  

 }

}
