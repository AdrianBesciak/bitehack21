#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

<<<<<<< HEAD
=======
#define DIST_TRIG 6
#define DIST_ECHO 7

>>>>>>> 425b0cebfc795fe3ec121dba4e799b94a8e672ca
#define RFID_TIMEOUT 1000
#define IR_THRESHOLD 512

MFRC522 mfrc(SS_PIN, RST_PIN);  // Create MFRC522 instance

void IRUpdate(uint16_t buffer[6]);
bool getID(uint8_t buffer[4]);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  SPI.begin();
  mfrc.PCD_Init();
  delay(5);
<<<<<<< HEAD
=======
  pinMode(DIST_TRIG, OUTPUT);
  pinMode(DIST_ECHO, INPUT);
  digitalWrite(DIST_TRIG, LOW);
>>>>>>> 425b0cebfc795fe3ec121dba4e799b94a8e672ca
}

String s;
uint8_t uid_buffer[4];
uint16_t ir_buffer[6];
<<<<<<< HEAD
=======
long distance;
>>>>>>> 425b0cebfc795fe3ec121dba4e799b94a8e672ca

void loop() {
  // put your main code here, to run repeatedly:
  IRUpdate(ir_buffer);
<<<<<<< HEAD
=======
  distance = getDist();
>>>>>>> 425b0cebfc795fe3ec121dba4e799b94a8e672ca
  if (Serial.available())
  {
    char c = Serial.read();
    if (isAlpha(c)) s += c;

    //Serial.println(c);
    //Serial.println(s);
    if (s == String("LINE"))
    {
      for (uint8_t i = 0; i < 6; i++)
      {
        Serial.print(ir_buffer[i]);
      }
      Serial.println("");
      s = "";
    }
    else if (s == String("RFID"))
    {
      if (getID(uid_buffer))
      {
        for (uint8_t i = 0; i < 4; i++)
        {
          if (uid_buffer[i] < 0x10) Serial.print('0');
          Serial.print(uid_buffer[i], HEX);
          if (i != 3) Serial.print(":");
        }
        Serial.println("");
      }
      else
      {
        //Serial.println("Failed to get UID");
      }
      s = "";
    }
<<<<<<< HEAD
=======
    else if (s == String("DIST"))
    {
      Serial.println(distance);
      s = "";
    }
>>>>>>> 425b0cebfc795fe3ec121dba4e799b94a8e672ca
    else if (s.length() >= 4)
      s = "";
  }
}


bool getID(uint8_t buffer[4])
{
  auto start = millis();
  while (millis() - start < RFID_TIMEOUT)
  {
    if (mfrc.PICC_IsNewCardPresent())
    {
      if (mfrc.PICC_ReadCardSerial())
      {
        for (uint8_t i = 0; i < 4; ++i)
        {
          buffer[i] = mfrc.uid.uidByte[i];
        }
        mfrc.PICC_HaltA();
        return true;
      }
    }
  }
  return false;
}

void getIRData(uint16_t buffer[6])
{
  for (uint8_t i = 14; i <= 19; ++i)
  {
    buffer[i - 14] = analogRead(i);
  }
}

void processIRData(uint16_t buffer[6])
{
  for (uint8_t i = 0; i < 6; i++)
  {
    buffer[i] = (buffer[i] > IR_THRESHOLD) ? 1 : 0;
  }
}

void IRUpdate(uint16_t buffer[6])
{
  getIRData(buffer);
  processIRData(buffer);
}
<<<<<<< HEAD
=======


long getDist()
{
  digitalWrite(DIST_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(DIST_TRIG, LOW);
  long duration = pulseIn(DIST_ECHO, HIGH);
  return duration * 0.034 / 2;

}
>>>>>>> 425b0cebfc795fe3ec121dba4e799b94a8e672ca
