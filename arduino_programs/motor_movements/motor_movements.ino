// Pines para el set de motores 1
const int IN1_1 = 44;
const int IN2_1 = 45;
const int IN3_1 = 46;
const int IN4_1 = 47;

// Pines para el set de motores 2
const int IN1_2 = 50;
const int IN2_2 = 51;
const int IN3_2 = 52;
const int IN4_2 = 53;

const int ENA_1 = 6;
const int ENB_1 = 7;
const int ENA_2 = 2;
const int ENB_2 = 3;

const int velocidadMaxima = 200;
const int velocidadMedia = 100;

String valor;

void setup() {
  pinMode(IN1_1, OUTPUT);
  pinMode(IN2_1, OUTPUT);
  pinMode(IN3_1, OUTPUT);
  pinMode(IN4_1, OUTPUT);
  pinMode(IN1_2, OUTPUT);
  pinMode(IN2_2, OUTPUT);
  pinMode(IN3_2, OUTPUT);
  pinMode(IN4_2, OUTPUT);
  pinMode(ENA_1, OUTPUT);
  pinMode(ENB_1, OUTPUT);
  pinMode(ENA_2, OUTPUT);
  pinMode(ENB_2, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    valor = Serial.readStringUntil('\n');
    switch (valor[0]) {
      case 'a':
        setVelocidadMotores(velocidadMaxima);
        girar_izq();
        break;
      case 'd':
        setVelocidadMotores(velocidadMaxima);
        girar_der();
        break;
      case 's':
        setVelocidadMotores(velocidadMedia);
        atras();
        break;
      case 'w':
        setVelocidadMotores(velocidadMedia);
        adelante();
        break;
      case ' ':
        detener();
        break;
    }
  }
}

void detener() {
  digitalWrite(IN1_1, LOW);
  digitalWrite(IN2_1, LOW);
  digitalWrite(IN3_1, LOW);
  digitalWrite(IN4_1, LOW);
  digitalWrite(IN1_2, LOW);
  digitalWrite(IN2_2, LOW);
  digitalWrite(IN3_2, LOW);
  digitalWrite(IN4_2, LOW);
  Serial.println("detener");
}

void girar_der() {
  digitalWrite(IN1_1, LOW);
  digitalWrite(IN2_1, HIGH);
  digitalWrite(IN3_1, HIGH);
  digitalWrite(IN4_1, LOW);
  digitalWrite(IN1_2, LOW);
  digitalWrite(IN2_2, HIGH);
  digitalWrite(IN3_2, HIGH);
  digitalWrite(IN4_2, LOW);
  Serial.println("derecha");
}

void girar_izq() {
  digitalWrite(IN1_1, HIGH);
  digitalWrite(IN2_1, LOW);
  digitalWrite(IN3_1, LOW);
  digitalWrite(IN4_1, HIGH);
  digitalWrite(IN1_2, HIGH);
  digitalWrite(IN2_2, LOW);
  digitalWrite(IN3_2, LOW);
  digitalWrite(IN4_2, HIGH);
  Serial.println("izquierda");
}

void atras() {
  digitalWrite(IN1_1, HIGH);
  digitalWrite(IN2_1, LOW);
  digitalWrite(IN3_1, HIGH);
  digitalWrite(IN4_1, LOW);
  digitalWrite(IN1_2, HIGH);
  digitalWrite(IN2_2, LOW);
  digitalWrite(IN3_2, HIGH);
  digitalWrite(IN4_2, LOW);
  Serial.println("atras");
}

void adelante() {
  digitalWrite(IN1_1, LOW);
  digitalWrite(IN2_1, HIGH);
  digitalWrite(IN3_1, LOW);
  digitalWrite(IN4_1, HIGH);
  digitalWrite(IN1_2, LOW);
  digitalWrite(IN2_2, HIGH);
  digitalWrite(IN3_2, LOW);
  digitalWrite(IN4_2, HIGH);
  Serial.println("adelante");
}

void setVelocidadMotores(int velocidad) {
  analogWrite(ENA_1, velocidad);
  analogWrite(ENB_1, velocidad);
  analogWrite(ENA_2, velocidad);
  analogWrite(ENB_2, velocidad);
  delay(10); // Añadir una pequeña pausa para permitir que los motores ajusten su velocidad
}
