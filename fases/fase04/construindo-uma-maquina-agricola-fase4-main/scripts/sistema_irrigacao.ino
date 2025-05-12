#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN 15         // GPIO para o sensor DHT22
#define DHTTYPE DHT22     // Tipo do sensor DHT
#define PIR_PIN 18        // GPIO para o sensor PIR
#define LDR_PIN 32        // GPIO para o sensor LDR
#define RELAY_PIN 19      // GPIO para o relé da bomba de água
#define BUZZER_PIN 22     // GPIO para o buzzer
#define TRIG_PIN 4        // GPIO para o Trig do HC-SR04
#define ECHO_PIN 5        // GPIO para o Echo do HC-SR04

// Inicialização do DHT e do display LCD
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2); // Endereço I2C do LCD (0x27 pode variar)

float temperatura, umidade;
int luminosidade;
bool movimentoDetectado = false;
long duracao;
int distancia;

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Configuração de pinos
  pinMode(PIR_PIN, INPUT);
  pinMode(LDR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Inicialização do LCD
  lcd.init();
  lcd.backlight();

  // Estado inicial dos atuadores
  digitalWrite(RELAY_PIN, LOW);  
  digitalWrite(BUZZER_PIN, LOW); 

  // Mensagem de inicialização
  lcd.setCursor(0, 0);
  lcd.print("Sistema Iniciado");
  delay(1000);
  lcd.clear();
}

void loop() {
  // Leitura do sensor DHT22
  temperatura = dht.readTemperature();
  umidade = dht.readHumidity();

  // Leitura do sensor LDR
  luminosidade = analogRead(LDR_PIN);

  // Leitura do sensor ultrassônico HC-SR04 para medir o nível de água
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duracao = pulseIn(ECHO_PIN, HIGH);
  distancia = duracao * 0.034 / 2;

  // Detecção de movimento com o PIR
  movimentoDetectado = digitalRead(PIR_PIN);
  if (movimentoDetectado) {
    // Atualização no LCD
    lcd.setCursor(0, 0);
    lcd.print("Mov detectado!");
    digitalWrite(BUZZER_PIN, HIGH);
    delay(1000);  
    digitalWrite(BUZZER_PIN, LOW);
  }

  // Lógica de controle da irrigação
  if (umidade < 50 && temperatura > 25 && distancia < 20) { // Se a distância da água está abaixo de 20 cm, permite irrigação
      digitalWrite(RELAY_PIN, HIGH);        
      Serial.print("Irrig:ON ");
      // Atualização no LCD
      lcd.setCursor(8, 1);
      lcd.print("Irrig:ON ");
  } else {
    digitalWrite(RELAY_PIN, LOW);      
    Serial.print("Irrig:OFF");
    // Atualização no LCD
    lcd.setCursor(7, 1);
    lcd.print("Irrig:OFF");
  }

  // Atualização no Serial Monitor
  Serial.print("Temperatura: "); Serial.print(temperatura); Serial.print(" °C");
  Serial.print(" - Umidade: "); Serial.print(umidade); Serial.println(" %");
  Serial.print("Luminosidade: "); Serial.println(luminosidade);
  Serial.print("Distância do nível de água: "); Serial.print(distancia); Serial.println(" cm");  

  // Atualização no LCD
  lcd.setCursor(0, 0);
  lcd.print("T:"); lcd.print(temperatura); lcd.print("C ");
  lcd.print("U:"); lcd.print(umidade); lcd.print("%");

  lcd.setCursor(0, 1);
  lcd.print("N:"); lcd.print(distancia); lcd.print("cm");

  delay(2000);
}