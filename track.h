/***************************************************************************/
// File			  [track.h]
// Author		  [Erik Kuo]
// Synopsis		[Code used for tracking]
// Functions  [MotorWriting, tracking]
// Modify		  [2020/03/27 Erik Kuo]
/***************************************************************************/

#include <SoftwareSerial.h>
#include <Wire.h>
int old_err = 0;
int P_err;
int I_err = 0;
int D_err = 0;
double Kd = 1;
double Ki = 1;
double Kp = 80;
void rightForward()
{
  digitalWrite(MotorR_I1,LOW);
  digitalWrite(MotorR_I2,HIGH);
  //Serial.println("Right forward");
}

void leftForward()
{
  digitalWrite(MotorL_I3,LOW);
  digitalWrite(MotorL_I4,HIGH);
  //Serial.println("Left forward");
}

void rightBackward()
{
  digitalWrite(MotorR_I1,HIGH);
  digitalWrite(MotorR_I2,LOW);
  //Serial.println("Right backward");
}

void leftBackward()
{
  digitalWrite(MotorL_I3,HIGH);
  digitalWrite(MotorL_I4,LOW);
  //Serial.println("Left backward");
}

void moveForward()
{
  analogWrite(MotorR_PWMR,100);
  analogWrite(MotorL_PWML,100);
  leftForward();
  rightForward();
}


void moveBackward()
{
  analogWrite(MotorR_PWMR,100);
  analogWrite(MotorL_PWML,98);
  leftBackward();
  rightBackward();
}

void turnLeftCenter()
{
  analogWrite(MotorR_PWMR,100);
  analogWrite(MotorL_PWML,100);
  leftBackward();
  rightForward();
}

void turnRightCenter()
{
  analogWrite(MotorR_PWMR,100);
  analogWrite(MotorL_PWML,100);
  leftForward();
  rightBackward();
}

void stopCar()
{
  analogWrite(MotorR_PWMR,0);
  analogWrite(MotorL_PWML,0);
  leftForward();
  rightForward();
}
/*if you have no idea how to start*/
/*check out what you have learned from week 1 & 6*/
/*feel free to add your own function for convenience*/

/*===========================import variable===========================*/
int extern _Tp;
/*===========================import variable===========================*/

// Write the voltage to motor.
void MotorWriting(double vL, double vR) {
  // TODO: use L298N to control motor voltage & direction

 /* if(error==666) //check if encounter node
    {
      stopCar;
      //TODO:read RFID
    
    }*/
    
    if( vR >= 0 )
        rightForward();
    else
    {
        rightBackward();
        vR = -vR;
    }

    if( vL >= 0 )
        leftForward();
    else
    {
        leftBackward();
        vL = -vL;
    }


  if(vR > 255)
    {
    vR = 255;
    }
  if(vL > 255)
    {
    vL = 255;
    }

  //Serial.print("vRAdj: ");
  //Serial.println(vRAdj);
  //Serial.print("vLAdj: ");
  //Serial.println(vLAdj);

  analogWrite(MotorR_PWMR,vR);
  analogWrite(MotorL_PWML, vL);

  //delay(2000);

}

// compute the error
int error(){

  int L3;
  int L2;
  int L1;
  int R3;
  int R2;
  int R1;


  int L3A = analogRead(A0);
  int L2A = analogRead(A1);
  int L1A = analogRead(A2);
  int R1A = analogRead(A3);
  int R2A = analogRead(A4);

  int R3A = analogRead(A5);


  if(L3A > 70){
    L3 = 1;
  }
  else{
    L3 = 0;
  }
  if(L2A > 70){
    L2 = 1;
  }
  else{
    L2 = 0;
  }
  if(L1A > 70){
    L1 = 1;
  }
  else{
    L1 = 0;
  }
  if(R1A > 70){
    R1 = 1;
  }
  else{
    R1 = 0;
  }
  if(R2A > 70){
    R2 = 1;
  }
  else{
    R2 = 0;
  }
  if(R3A > 70){
    R3 = 1;
  }
  else{
    R3 = 0;
  }
  //int counter = L3 + L2 + L1 + R1 + R2 + R3;
  P_err = L3 * (-2) + L2 * (-1) + R2 * 1 + R3 * 2;
  //I_err = I_err + P_err;
  //D_err = P_err - old_err;

  old_err = P_err;

  //double power = Kp*P_err + Ki*I_err + Kd*D_err;
  double power = Kp*P_err;
  if(R1+R2+R3+L1+L2+L3>=5)
    power=666;
  return power;
  /*
  if( counter == 0 )
  {
    return 0;
  }
  else
    return sum / counter;
  */
}// MotorWriting

// P/PID control Trackingbj
void tracking(int L1,int L2,int L3,int R3,int R2,int R1){
  //TODO: complete your P/PID tracking code
    
    int vRAdj = 0;
    int vLAdj = 0;
    int vR=100;
    int vL=100;
    int Error=error;

    vRAdj = vR - Error;
    vLAdj = vL + Error;
    MotorWriting(vLAdj,vRAdj);
}// tracking
