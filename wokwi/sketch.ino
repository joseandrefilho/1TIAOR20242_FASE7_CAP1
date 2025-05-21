// ----------------------------------------------
// Bibliotecas para controle de hardware e rede
// ----------------------------------------------

// Comunicação I2C para controle do display LCD
#include <Wire.h>

// Biblioteca para manipular displays LCD com interface I2C
#include <LiquidCrystal_I2C.h>

// Biblioteca de conexão Wi-Fi do ESP32
#include <WiFi.h>

// Biblioteca de cliente MQTT (Publicação/Assinatura de tópicos)
#include <PubSubClient.h>

// Biblioteca para leitura de sensores DHT (Temperatura/Umidade)
#include <DHT.h>

// ----------------------------------------------
// Constantes de configuração geral do sistema
// ----------------------------------------------

// Credenciais da rede Wi-Fi (rede simulada no Wokwi)
static const char PROGMEM WIFI_SSID[] = "Wokwi-GUEST";
static const char PROGMEM WIFI_PASS[] = "";

// Endereço do broker MQTT público usado para testes
static const char PROGMEM MQTT_SERVER[] = "mqtt.eclipseprojects.io";

// Tópico utilizado para publicar os dados dos sensores
static const char PROGMEM MQTT_TOPIC[] = "farmtech/grupo18/data";

// ----------------------------------------------
// Pinos utilizados no ESP32
// ----------------------------------------------

// Sensor DHT22 de umidade/temperatura
static const uint8_t DHTPIN = 4;

// Sensor LDR para simular pH (entrada analógica)
static const uint8_t LDRPIN = 34;

// Botões para simular ativação de nutrientes
static const uint8_t BP_PIN_P = 12;
static const uint8_t BP_PIN_K = 14;

// LEDs para representar nutrientes ativados
static const uint8_t LED_P = 26;
static const uint8_t LED_K = 27;

// LED e pino de controle de irrigação
static const uint8_t LED_RELE = 19;
static const uint8_t RELE_PIN = 23;

// ----------------------------------------------
// Constantes para lógica de decisão
// ----------------------------------------------

static const uint8_t DHTTYPE = DHT22;

// Tempo entre atualizações de display/publicação (em ms)
static const uint16_t DISPLAY_INTERVAL = 2000;

// Faixas consideradas aceitáveis para os sensores
static const float UMIDADE_MIN = 50.0;  // mínimo de umidade para não irrigar
static const float TEMP_MAX = 30.0;     // temperatura máxima tolerada
static const float PH_MIN = 5.0;        // pH mínimo
static const float PH_MAX = 7.0;        // pH máximo

// ----------------------------------------------
// Estrutura para manter os dados do sistema
// ----------------------------------------------

// Agrupa todas as leituras e flags do sistema em uma struct otimizada
struct SystemData {
    float umidade;
    float temperatura;
    float pHLevel;

    // Flags com 1 bit cada para economizar memória
    struct {
        uint8_t led_P : 1;       // LED visual para nutriente P
        uint8_t led_K : 1;       // LED visual para nutriente K
        uint8_t nutrientP : 1;   // Flag de ativação manual do nutriente P
        uint8_t nutrientK : 1;   // Flag de ativação manual do nutriente K
        uint8_t releState : 1;   // Flag de ativação do sistema de irrigação
    } flags;
} sysData;

// ----------------------------------------------
// Instanciação dos objetos globais
// ----------------------------------------------

// Display LCD 16x2 no endereço I2C 0x27
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Cliente Wi-Fi e cliente MQTT
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

// Objeto do sensor DHT
DHT dht(DHTPIN, DHTTYPE);

// Controle de tempo para atualizações
unsigned long lastUpdate = 0;

// ----------------------------------------------
// Inicializa o LCD e exibe status
// ----------------------------------------------
void setupLCD() {
    Wire.begin();
    lcd.init();
    lcd.backlight();
    lcd.clear();
    lcd.print(F("Iniciando..."));
    delay(1000);
}

// ----------------------------------------------
// Conecta na rede Wi-Fi e exibe IP
// ----------------------------------------------
void setup_wifi() {
    lcd.clear();
    lcd.print(F("Conectando WiFi"));
    Serial.print(F("Conectando a "));
    Serial.println(WIFI_SSID);

    WiFi.begin(WIFI_SSID, WIFI_PASS);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
        lcd.print(".");
    }

    lcd.clear();
    lcd.print(F("WiFi Conectado!"));
    lcd.setCursor(0, 1);
    lcd.print(WiFi.localIP());
    Serial.println(F("\nWiFi conectado"));
    Serial.println(WiFi.localIP());
    delay(2000);
}

// ----------------------------------------------
// Tenta reconectar ao servidor MQTT
// ----------------------------------------------
void reconnect() {
    int tentativas = 0;
    while (!mqttClient.connected() && tentativas < 3) {
        Serial.print(F("Conectando MQTT..."));
        lcd.clear();
        lcd.print(F("Conectando MQTT"));
        
        if (mqttClient.connect("ESP32_FarmTech")) {
            Serial.println(F("Conectado"));
            lcd.clear();
            lcd.print(F("MQTT Conectado"));
            delay(1000);
        } else {
            tentativas++;
            Serial.print(F("Falha, rc="));
            Serial.print(mqttClient.state());
            Serial.println(F(" tentando novamente em 5s"));
            lcd.clear();
            lcd.print(F("Erro MQTT"));
            lcd.setCursor(0, 1);
            lcd.print(F("Tentativa: "));
            lcd.print(tentativas);
            delay(5000);
        }
    }
}

// ----------------------------------------------
// Publica os dados atuais no tópico MQTT
// ----------------------------------------------
void publishData() {
    if (!mqttClient.connected()) return;

    // Monta uma string JSON com os dados do sistema
    // Campos compatíveis com o backend Python
    static char message[128];
    snprintf(message, sizeof(message),
            "{\"Umidade do Solo\":%.1f,\"Temperatura\":%.1f,\"PH\":%.1f,\"Nutriente P\":%d,\"Nutriente K\":%d,\"Irrigacao\":%d}",
            sysData.umidade, sysData.temperatura, sysData.pHLevel,
            sysData.flags.nutrientP, sysData.flags.nutrientK, sysData.flags.releState);

    if (mqttClient.publish(MQTT_TOPIC, message)) {
        Serial.println(F("Dados publicados"));
    }
}

// ----------------------------------------------
// Atualiza o conteúdo exibido no display LCD
// ----------------------------------------------
void updateDisplay() {
    lcd.clear();
    
    // Linha 1: Umidade e temperatura
    lcd.setCursor(0, 0);
    lcd.print(F("U:"));
    lcd.print(sysData.umidade, 1);
    lcd.print(F("% T:"));
    lcd.print(sysData.temperatura, 1);
    lcd.print(F("C"));
    
    // Linha 2: pH e status de ativação
    lcd.setCursor(0, 1);
    lcd.print(F("pH:"));
    lcd.print(sysData.pHLevel, 1);
    lcd.print(F(" "));
    if (sysData.flags.nutrientP) lcd.print(F("P "));
    if (sysData.flags.nutrientK) lcd.print(F("K "));

    // Indica explicitamente se está irrigando ou não
    lcd.setCursor(12, 1);  // Posição final da linha 2
    if (sysData.flags.releState) {
        lcd.print("ON");  // Irrigação Ativa
    } else {
        lcd.print("OFF"); // Irrigação Inativa
    }
}

// ----------------------------------------------
// Envia dados para o Serial Plotter (debug visual)
// ----------------------------------------------
void updatePlotter() {
    Serial.print(F("Umidade:"));
    Serial.print(sysData.umidade);
    Serial.print(F(", Temperatura:"));
    Serial.print(sysData.temperatura);
    Serial.print(F(", pH:"));
    Serial.print(sysData.pHLevel);
    Serial.print(F(", Irrigação: "));
    Serial.println(sysData.flags.releState ? "ATIVA" : "INATIVA");
}


// ----------------------------------------------
// Lê sensores e executa a lógica de controle
// ----------------------------------------------
void readSensors() {
    sysData.umidade = dht.readHumidity();
    sysData.temperatura = dht.readTemperature();

    if (!isnan(sysData.umidade) && !isnan(sysData.temperatura)) {
        // Simulação de pH baseada em luminosidade:
        // Quanto mais claro (menor resistência), maior o valor lido → maior o pH simulado
        uint16_t ldrValue = analogRead(LDRPIN);
        sysData.pHLevel = (map(ldrValue, 4063, 32, 0, 1400) / 100.0); // pH entre 0.0 e 14.0

        // Lógica de ativação automática da irrigação
        // Irriga se qualquer uma das condições críticas for verdadeira
        sysData.flags.releState = (
            sysData.umidade < UMIDADE_MIN || 
            sysData.temperatura > TEMP_MAX || 
            sysData.pHLevel < PH_MIN || 
            sysData.pHLevel > PH_MAX || 
            sysData.flags.nutrientP || 
            sysData.flags.nutrientK
        );

        // Ativa ou desativa o relé (e o LED correspondente)
        digitalWrite(RELE_PIN, sysData.flags.releState);
        digitalWrite(LED_RELE, sysData.flags.releState);
    }
}

// ----------------------------------------------
// Detecta e alterna os estados dos botões
// ----------------------------------------------
void checkButtons() {
    if (digitalRead(BP_PIN_P) == LOW) {
        delay(50);  // debounce
        if (digitalRead(BP_PIN_P) == LOW) {
            sysData.flags.nutrientP = !sysData.flags.nutrientP;
            sysData.flags.led_P = sysData.flags.nutrientP;
            digitalWrite(LED_P, sysData.flags.led_P);
        }
    }

    if (digitalRead(BP_PIN_K) == LOW) {
        delay(50);
        if (digitalRead(BP_PIN_K) == LOW) {
            sysData.flags.nutrientK = !sysData.flags.nutrientK;
            sysData.flags.led_K = sysData.flags.nutrientK;
            digitalWrite(LED_K, sysData.flags.led_K);
        }
    }
}

// ----------------------------------------------
// Configuração inicial do sistema
// ----------------------------------------------
void setup() {
    Serial.begin(115200);

    // Configura os pinos como entrada ou saída
    pinMode(BP_PIN_P, INPUT_PULLUP);
    pinMode(BP_PIN_K, INPUT_PULLUP);
    pinMode(LED_P, OUTPUT);
    pinMode(LED_K, OUTPUT);
    pinMode(LED_RELE, OUTPUT);
    pinMode(RELE_PIN, OUTPUT);

    setupLCD();           // Inicia o display LCD
    dht.begin();          // Inicia o sensor DHT22
    setup_wifi();         // Conecta à rede Wi-Fi
    mqttClient.setServer(MQTT_SERVER, 1883);  // Configura o servidor MQTT

    // Inicializa LEDs apagados
    digitalWrite(LED_P, LOW);
    digitalWrite(LED_K, LOW);
    digitalWrite(LED_RELE, LOW);
    digitalWrite(RELE_PIN, LOW);
}

// ----------------------------------------------
// Loop principal do programa
// ----------------------------------------------
void loop() {
    // Reconecta ao MQTT caso necessário
    if (!mqttClient.connected()) {
        reconnect();
    }
    mqttClient.loop();

    // Verifica entrada dos botões e atualiza sensores
    checkButtons();
    readSensors();

    // Atualiza dados visuais e envia MQTT periodicamente
    unsigned long currentMillis = millis();
    if (currentMillis - lastUpdate >= DISPLAY_INTERVAL) {
        updateDisplay();
        updatePlotter();
        publishData();
        lastUpdate = currentMillis;
    }

    delay(1000);  // Reduz uso da CPU sem comprometer a fluidez
}
