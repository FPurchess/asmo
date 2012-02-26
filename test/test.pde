// basic mirroring of serial signal

void setup() {
  Serial.begin(9600);
}

String value = "";

void loop() {
  while(Serial.available() > 0) {
    value += (char) Serial.read();
    delay(10);
  }

  if (value != "") {
    Serial.println(value);
    value = "";
  }
}
