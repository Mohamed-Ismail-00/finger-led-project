int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;  
int led5 = 6;  

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int count = Serial.parseInt();
    Serial.print("Received: ");
    Serial.println(count);

    digitalWrite(led1, count >= 1 ? HIGH : LOW);
    digitalWrite(led2, count >= 2 ? HIGH : LOW);
    digitalWrite(led3, count >= 3 ? HIGH : LOW);
    digitalWrite(led4, count >= 4 ? HIGH : LOW);
    digitalWrite(led5, count >= 5 ? HIGH : LOW);
  }
}
