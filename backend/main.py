from flask import Flask, jsonify, request
from flask_cors import CORS
import serial 
import sys
import os
import time
#from serial import Serial
from interprete.parser import grammar


arduino =serial.Serial('COM10',baudrate=9600,timeout=.1)
arduino_leido= arduino.readline()
#time.sleep(2)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 200, 'message': 'Hello, world!'})


@app.route('/sendData', methods=['POST'])
def sendData():
    if not request.json or 'code_in' not in request.json:
        return jsonify({"error": "La solicitud debe ser un JSON y contener el campo 'code_in'"}), 400

    code_in = request.json['code_in']
    print(code_in)

    ast = grammar.parse(code_in)

    try:
        print("\nformato de instrucciones:  Figura;Fila;Columna;Color")
        for instruction in ast:
            tmp = instruction.execute()
            print("codigo enviado: "+ str(tmp.encode('utf-8')))
            cadena=tmp+"\n"
            bytes_cadena=cadena.encode('utf-8')
            arduino.write(bytes_cadena)
            
            print("---------------------")
            #print("codigo recibido arduino: "+ str(arduino_leido))
            arduino_leido=arduino.readline()
            print(arduino_leido)
            arduino_leido=arduino.readline()
            print(arduino_leido)
            arduino_leido=arduino.readline()
            print(arduino_leido)
            arduino_leido=arduino.readline()
            print(arduino_leido)
            arduino_leido=arduino.readline()
            print(arduino_leido)
           
            print("**")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        return jsonify({"error": "Ocurrió un error al ejecutar el código"}), 500
    
    result = {
        "status": 200,
        "message": "Código ejecutado correctamente",
    }
    return jsonify(result)
    


if __name__ == '__main__':
    app.run(port=5000)

if __name__ == "__main__":
    app.run(debug=True)






















# while True:

#     cordX = input('Ingrese la coordenada X: ')
#     cordY = input('Ingrese la coordenada Y: ')
#     Fig = input('Ingrese la figura: ').upper()
    
#     strOutput = str(Fig) + ";"+ str(cordX) + ";" + str(cordY)
#     print("codigo enviado: "+ str(strOutput.encode('ascii')))
#     serialArduino.write(strOutput.encode('ascii'))
    






