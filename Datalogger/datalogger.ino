#include <DHT.h>
#include <ESP8266WiFi.h>
String apiKey = "MR8ZOJ0PVCD7YV99";
const char *ssid = "SSID";                 //put here your home/work network's SSID
const char *pass = "PSWD";                 //put here your home/work network's password
const char* server = "api.thingspeak.com";
#define DHTPIN 0

DHT dht(DHTPIN, DHT11);
WiFiClient client;
void setup()
{
Serial.begin(115200);
delay(10);
dht.begin();

Serial.println("Connecting to ");
Serial.println(ssid);

WiFi.begin(ssid, pass);

while (WiFi.status() != WL_CONNECTED)
{
delay(500);
Serial.print(".");
}
Serial.println("");
Serial.println("WiFi connected");

}

void loop()
{
float h = dht.readHumidity();
float t = dht.readTemperature();
float temp = analogRead(A0);
temp=1024-temp;

if (isnan(h) || isnan(t))
{
Serial.println("Failed to read from DHT sensor!");
return;
}

if (client.connect(server,80))
{

String postStr = apiKey;
postStr +="&field1=";
postStr += String(t);
postStr +="&field2=";
postStr += String(h);
postStr +="&field3=";
postStr += String(temp);
postStr += "\r\n\r\n";

client.print("POST /update HTTP/1.1\n");
client.print("Host: api.thingspeak.com\n");
client.print("Connection: close\n");
client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n");

client.print("Content-Type: application/x-www-form-
urlencoded\n");

client.print("Content-Length: ");
client.print(postStr.length());
client.print("\n\n");
client.print(postStr);
Serial.print("Temperature: ");
Serial.print(t);
Serial.print(" degrees Celcius, Humidity: ");
Serial.print(h);
Serial.print("%, Moisture Sensor Value: ");
Serial.print(temp);
Serial.println(". Send to Thingspeak.");
}
client.stop();

Serial.println("Waiting...");
delay(1);
}
