#include <max6675.h>

int SOpin  = 22;
int SCKpin = 24;

int CSpin1 = 14;
int CSpin2 = 15;
int CSpin3 = 16;
int CSpin4 = 17;
int CSpin5 = 18;
int CSpin6 = 19;
int CSpin7 = 20;
int CSpin8 = 21;

MAX6675 Module1(SCKpin, CSpin1, SOpin);
MAX6675 Module2(SCKpin, CSpin2, SOpin);
MAX6675 Module3(SCKpin, CSpin3, SOpin);
MAX6675 Module4(SCKpin, CSpin4, SOpin);
MAX6675 Module5(SCKpin, CSpin5, SOpin);
MAX6675 Module6(SCKpin, CSpin6, SOpin);
MAX6675 Module7(SCKpin, CSpin7, SOpin);
MAX6675 Module8(SCKpin, CSpin8, SOpin);

void setup() {
    Serial.begin(9600);
    Serial.println("MAX6675");
    delay(1000);
}

void loop() {
    Serial.print(",");
    Serial.print(Module1.readCelsius());
    Serial.print(",");
    Serial.print(Module2.readCelsius());
    Serial.print(",");
    Serial.print(Module3.readCelsius());
    Serial.print(",");
    Serial.print(Module4.readCelsius());
    Serial.print(",");
    Serial.print(Module5.readCelsius());
    Serial.print(",");
    Serial.print(Module6.readCelsius());
    Serial.print(",");
    Serial.print(Module7.readCelsius());
    Serial.print(",");
    Serial.print(Module8.readCelsius());
    Serial.println();
    delay(500);
}
