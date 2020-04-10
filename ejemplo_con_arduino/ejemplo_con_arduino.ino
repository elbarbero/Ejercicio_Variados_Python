
int led1 = 9;
int analogica = 16;

void setup()
{
  Serial.begin(115200);
  pinMode(led1, OUTPUT);

  digitalWrite(led1, LOW);
}

void loop()
{

  if (Serial.available() > 0)
  {
    String orden = Serial.readStringUntil('\n');
    if ( orden.equals("1")) {
      //Serial.write("\n------------------LED ENCENDIDO----------------");
      digitalWrite(led1, HIGH);
    } else if ( orden.equals("0")) {
      //Serial.write("\n------------------LED APAGADO----------------");
      digitalWrite(led1, LOW);
    }
    while (Serial.available() > 0)
    {
      Serial.read();
    }
    Serial.println(digitalRead(led1));
  }
}
