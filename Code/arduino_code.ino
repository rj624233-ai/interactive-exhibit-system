#define IR1 2
#define IR2 3

void setup() {
  pinMode(IR1, INPUT);
  pinMode(IR2, INPUT);
  Serial.begin(9600);
}

void loop() {
  int s1 = digitalRead(IR1);
  int s2 = digitalRead(IR2);

  if (s1 == LOW && s2 == LOW) {
    Serial.println("BOTH");
    delay(500);  // avoid spam
  }
}
