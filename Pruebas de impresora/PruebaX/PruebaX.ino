#include <Servo.h>
#include <AFMotor.h>

AF_Stepper motor1(20, 2);
AF_Stepper motor2(20, 1);
Servo myservo; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");
  myservo.attach(10); 
  myservo.write(0);
  motor1.setSpeed(300);  // 10 rpm  
  motor2.setSpeed(300); 
}

void loop() {
  reiniciarServo();
}

void escribirX(){
  myservo.write(0);
  delay(300);
  for(int i = 0; i < 155; i++){
    motor1.step(1, FORWARD, SINGLE);
    motor2.step(1, FORWARD, SINGLE);
  }
    delay(300);
    myservo.write(30);
    delay(300);
    motor2.step(155, BACKWARD, SINGLE);
    delay(300);
    myservo.write(0);
    delay(300);
  for(int i = 0; i < 155; i++){
    motor1.step(1, BACKWARD, SINGLE);
    motor2.step(1, FORWARD, SINGLE);
  }
  delay(10000);
}

void reiniciarServo(){
  myservo.write(30);
}
