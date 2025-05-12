// Configurações de pinos
const int umidadePin = 34;    // Pino para o potenciômetro (umidade do solo)
const int nutrienteP_Pin = 32; // Pino para o botão do nutriente P
const int nutrienteK_Pin = 33; // Pino para o botão do nutriente K
const int phPin = 35;         // Pino para o LDR (pH do solo)
const int relePin = 26;       // Pino para o relé (bomba de água)

// Variáveis para armazenar o estado dos sensores
int umidadeSolo = 0;
bool nutrienteP = false;
bool nutrienteK = false;
int phSolo = 0;
bool irrigacaoAtiva = false;

// Limite de umidade para ativação da bomba
const int LIMITE_UMIDADE = 2000;  // Ajuste este valor conforme necessário

void setup() {
  Serial.begin(115200);
  
  // Configura os pinos dos botões e do relé
  pinMode(nutrienteP_Pin, INPUT_PULLUP); // Botão de nutriente P
  pinMode(nutrienteK_Pin, INPUT_PULLUP); // Botão de nutriente K
  pinMode(relePin, OUTPUT);              // Relé para a bomba de água

  // Inicialmente desativa a bomba de água
  digitalWrite(relePin, LOW);
}

void loop() {
  // Leitura da umidade do solo
  umidadeSolo = analogRead(umidadePin);
  
  // Leitura dos botões de nutrientes
  nutrienteP = !digitalRead(nutrienteP_Pin); // Botão pressionado = true
  nutrienteK = !digitalRead(nutrienteK_Pin); // Botão pressionado = true
  
  // Leitura do pH do solo usando LDR
  phSolo = analogRead(phPin);

  // Lógica para controle da bomba de água
  if (umidadeSolo < LIMITE_UMIDADE && (nutrienteP || nutrienteK)) {
    digitalWrite(relePin, HIGH); // Liga a bomba
    irrigacaoAtiva = true;
  } else {
    digitalWrite(relePin, LOW);  // Desliga a bomba
    irrigacaoAtiva = false;
  }

  // Exibe os dados no Monitor Serial
  Serial.print("Umidade do Solo: ");
  Serial.println(umidadeSolo);

  Serial.print("Nutriente P (Presença): ");
  Serial.println(nutrienteP ? "Sim" : "Não");

  Serial.print("Nutriente K (Presença): ");
  Serial.println(nutrienteK ? "Sim" : "Não");

  Serial.print("Nível de pH (LDR): ");
  Serial.println(phSolo);

  Serial.print("Irrigação Ativa: ");
  Serial.println(irrigacaoAtiva ? "Sim" : "Não");

  Serial.println("-----------------------");
  
  delay(2000);  // Atraso de 2 segundos entre as leituras
}
