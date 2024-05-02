#include <Separador.h>
#define P0 22
#define P1 24
#define N0 26
#define N1 28
#define RW 30
#define P0L 23
#define P1L 25
#define N0L 27
#define N1L 29
int valorP0 = digitalRead(P0);
    int valorP1= digitalRead(P1);
    int RN0=digitalRead(N0L);
    int RN1= digitalRead(N1L);

Separador s;

void setup() {
 Serial.begin(9600);
 
  pinMode(P0, OUTPUT);	
  pinMode(P1, OUTPUT);
  pinMode(N0, OUTPUT);	
  pinMode(N1, OUTPUT);	
  pinMode(RW, OUTPUT);	
  pinMode(P0L, INPUT);	
  pinMode(P1L, INPUT);
  pinMode(N0L, INPUT);	
  pinMode(N1L, INPUT);	
 Serial.println("recibio");
 


}

void loop() {
  while(Serial.available())
  {
    serialEvent();

  }
  
  
}
void serialEvent(){
  String datosrecibidos = Serial.readStringUntil('\n');


  String figura= s.separa(datosrecibidos,';',0);
  String posx=s.separa(datosrecibidos,';',1);
  String posy=s.separa(datosrecibidos,';',2);
  String color=s.separa(datosrecibidos,';',3);

 
  
  setfig(figura);
  setcolor(color);
  Posx(posx);
  Posy(posy);
  
  

  String fig  = lecturafig(RN0,RN1);
  String color_recibido= lecturacolor(RN0,RN1);
  String posx_recibido=lecturax(RN0,RN1);
  String posy_recibido=lecturay(RN0,RN1);

Imprimir(fig, posx_recibido, posy_recibido, color_recibido);


  }
  void setfig(String fig){
    digitalWrite(P0,LOW);
    digitalWrite(P1,LOW);
    
    

   if(fig=="O"){
    digitalWrite(N0,LOW);
    digitalWrite(N1,LOW);
    Serial.println("La figura recibida en ard es O");
   }
   else if(fig=="X"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,LOW);
    Serial.println("La figura recibida en ard es X");
   }
   else if(fig=="estrella"){
    digitalWrite(N0,LOW);
    digitalWrite(N1,HIGH);
    Serial.println("La figura recibida en ard es estrella");
   }
   else if(fig=="triangulo"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,HIGH);
    Serial.println("La figura recibida en ard es triangulo");
   }
    digitalWrite(RW,HIGH);
    digitalWrite(RW,LOW);
}
  void setcolor(String colour){
   digitalWrite(P0,HIGH);
    digitalWrite(P1,HIGH);
     

    
   if(colour=="magenta"){
    digitalWrite(N0,LOW);
    digitalWrite(N1,LOW);
    Serial.println("El color recibida en ard magenta ");
   }
   else if(colour=="amarillo"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,LOW);
    
    Serial.println("El color recibida en ard amrll ");
   }
    else if(colour=="negro"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,LOW);
    
    Serial.println("El color recibida en ard negro");
    
   }
    else if(colour=="cyan"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,HIGH);
    
    Serial.println("El color recibida en ard cyan");
    
   }
  digitalWrite(RW,HIGH);
  digitalWrite(RW,LOW);
   
  }
  void Posx(String x){
     digitalWrite(P0,HIGH);
     digitalWrite(P1,LOW);
   if(x=="1"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,LOW);
    
    Serial.println("La pos x recibida en ard 1 ");
   }
   else if(x=="2"){
    digitalWrite(N0,LOW);
    digitalWrite(N1,HIGH);
    Serial.println("La pos x recibida en ard 2 ");
   }
   else if(x=="3"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,HIGH);
    Serial.println("La pos x recibida en ard 3 ");
   }
     digitalWrite(RW,HIGH);
  digitalWrite(RW,LOW);
   
  }
  void Posy(String y){
    
    digitalWrite(P0,LOW);
    digitalWrite(P1,HIGH);
   
   if(y=="1"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,HIGH);
    Serial.println("La pos y recibida en ard 1 ");
   }
   else if(y=="2"){
    digitalWrite(N0,LOW);
    digitalWrite(N1,HIGH);
    Serial.println("La pos y recibida en ard 2");
   }
   else if(y=="3"){
    digitalWrite(N0,HIGH);
    digitalWrite(N1,HIGH);
    Serial.println("La pos y recibida en ard 3 ");
   }
     digitalWrite(RW,HIGH);
  digitalWrite(RW,LOW);
  }
 String  lecturafig(int valorN0, int valorN1)
  { valorP0 = 0;
   valorP1 = 0;
    

       ///reconoción figura
            Serial.println("se leyo: figura");
            if (valorN0==0 && valorN1==0){
              Serial.println("La figura es un circulo");

            }
            else if (valorN0==1 && valorN1==0 ){
              Serial.println("La figura es una X");
            }
             else if (valorN0==0 && valorN1==1 ){
              Serial.println("La figura es una estrella");
            }
            else if (valorN0==1 && valorN1==1 ){
              Serial.println("La figura es un triangulo");
            }

          
  }
  String lecturax(int valorN0, int valorN1){
  valorP0 = 1;
   valorP1 = 0;

          // reconocio x
          Serial.println("Se leyo: posicion en X");
            if (valorN0==1 && valorN1==0){
              Serial.println("La pos en x es 1");

            }
            else if (valorN0==0 && valorP1==1 ){
              Serial.println("La pos en x es 2");
            }
             else if (valorN0==1 && valorP1==1 ){
              Serial.println("La pos en x es 3");
            }
    }
    String lecturay(int valorN0, int valorN1)
    {// reconocio y
     valorP0 = 0;
     valorP1 = 1;
          Serial.println("Se leyo: posicion en Y");
            if (valorN0==1 && valorN1==0){
              Serial.println("La pos en y es 1");

            }
            else if (valorN0==0 && valorN1==1 ){
              Serial.println("La pos en y es 2");
            }
             else if (valorN0==1 && valorN1==1 ){
              Serial.println("La pos en y es 3");
            }
             }
    String lecturacolor(int valorN0, int valorN1)
    {
         valorP0 = 1;
          valorP1 = 1; // reconoce color
          Serial.println("Se leyo : Color");
            if (valorN0==0 && valorN1==0){
              Serial.println("El color es magenta");

            }
            else if (valorN0==0 && valorP1==1 ){
              Serial.println("El color amarillo");
            }
             else if (valorN0==1 && valorP1==0 ){
              Serial.println("El color negro");
            }
            else if (valorN0==1 && valorP1==1 ){
              Serial.println("El color Cyan");
            }
             }


             ////////////////////////////
  void  Imprimir(String fig,  String ejex, String ejey,String colour){
                if(fig=="O"){////figura
              Serial.println("La figura recibida en ard es O");
            }
            else if(fig=="X"){
              Serial.println("La figura recibida en ard es X");
            }
            else if(fig=="estrella"){
              Serial.println("La figura recibida en ard es estrella");
            }
            else if(fig=="triangulo"){
              Serial.println("La figura recibida en ard es triangulo");
            }
            ////////////////////
                if(ejex=="1"){//eje x
                
                Serial.println("La pos x recibida en ard 1 ");
              }
              else if(ejex=="2"){
                Serial.println("La pos x recibida en ard 2 ");
              }
              else if(ejex=="3"){
                Serial.println("La pos x recibida en ard 3 ");
              }
            //////////////////////
            if(ejey=="1"){
              Serial.println("La pos y recibida en ard 1 ");
            }
            else if(ejey=="2"){
              Serial.println("La pos y recibida en ard 2");
            }
            else if(ejey=="3"){
              Serial.println("La pos y recibida en ard 3 ");
            }
            ////////////////
            if(colour=="magenta"){
             
              Serial.println("El color recibida en ard magenta ");
            }
            else if(colour=="amarillo"){
              digitalWrite(N0,HIGH);
              digitalWrite(N1,LOW);
              
              Serial.println("El color recibida en ard amrll ");
            }
              else if(colour=="negro"){
              digitalWrite(N0,HIGH);
              digitalWrite(N1,LOW);
              
              Serial.println("El color recibida en ard negro");
              
            }
              else if(colour=="cyan"){
              digitalWrite(N0,HIGH);
              digitalWrite(N1,HIGH);
              
              Serial.println("El color recibida en ard cyan");
              
            }

    
  }
   

    

        
  


  
