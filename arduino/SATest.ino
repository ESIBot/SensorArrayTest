// ESIBot

//Parametros
#define velocidad 115200
#define numSensors 8

unsigned int analogPins[] = {A0,A1,A2,A3,A4,A5,A6,A7};

void setup() {
  Serial.begin(velocidad);
}

void loop() {
  for(int i=0;i<numSensors;i++)
  {
    unsigned int sensorValue = map(analogRead(analogPins[i]),0,1023,0,255);
    Serial.print(sensorValue);
    Serial.print(",");
  }
  Serial.println();
  delay(10);        // delay in between reads for stability
}
