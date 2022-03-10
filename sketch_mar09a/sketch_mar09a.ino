// Potentiometer is connected to GPIO 2 
// joystick VRX is connected to GPIO 15
// joystick VRY is connected to GPIO 13
// joystick SW is connected to GPIO 12
const int potPin1 = 2;
const int joyPin1 = 15;
const int joyPin2 = 13;
const int joyPin3 = 12;

int potValue = 0;
int joyValX = 0;
int joyValY = 0;
int joyValSW = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  // Reading potentiometer value
  potValue = analogRead(potPin1);
  joyValX = analogRead(joyPin1);
  joyValY = analogRead(joyPin2);
  joyValSW = analogRead(joyPin3);
  
  Serial.println(potValue);
  Serial.println(joyValX);
  Serial.println(joyValY);
  Serial.println(joyValSW);
  
  delay(500);
}
