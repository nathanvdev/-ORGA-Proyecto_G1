# RAMA DEVELOP 👀

## Proyecto - Plotter Serial 

### PRIMER SEMESTRE 2024

|     | Nombre                            | Carnet    |
| --- | --------------------------------- | --------- |
| 1   | Bismarck Estuardo Romero Lemus    | 201708880 |
| 2   | Josué Nabí Hurtarte Pinto         | 202202481 |
| 3   | Naomi Rashel Yos Cujcuj           | 202001814 |
| 4   | Angela Paulina Rodriguez López    | 201503569 |
| 5   | Rodrigo Alejandro Tahuite Soria   | 202202854 |
| 6   | Nathan Antonio Valdez Valdez      | 202001568 |
| 7   | Gonzalo Fernando Pérez Cazún      | 202211515 |
| 8   | Rony Omar Miguel López            | 201905750 |
| 9   | Kevin Eduardo Castañeda Hernández | 201901801 |

## Correr el proyecto

- Dirigirse a la carpeta frontend.
- Usar el comando "npm start".
- Correr el backend "main.py".
- ...



## Comunicación Serial

El puerto serial es una interfaz de comunicación que permite la transferencia de datos de manera serial, es decir, un bit a la vez, entre dos dispositivos. En el caso de Arduino, el puerto serial se utiliza para la comunicación entre la placa Arduino y otros dispositivos, como una computadora.

En este proyecto se utilizó la comunicación serial con 9600 baudios, el backend envia y recibe información del arduino gracias a esto, desde el backed se envía la información como figura, color,posicion en X, posicion en Y de cada coordenada como una cadena de texto, esta es recibida por el arduino, decodificada y procesada para su escritura en la ram, luego su lectura y ejecución, luego de completar este ciclo el arduino envia una señal utilizando la comunicación serial al computador para indicar que está listo para reicibir una nueva coordena y repetir este ciclo. 

