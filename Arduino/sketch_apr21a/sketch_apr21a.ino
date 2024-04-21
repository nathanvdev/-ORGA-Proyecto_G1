void setup() {
  Serial.begin(9600);
  delay(30);
}

String strInput, cordX, cordY, Fig;
int param;

void loop() {
  strInput = Serial.readString();
  Serial.println(strInput);

}
