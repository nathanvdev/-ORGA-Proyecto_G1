from flask import Flask, jsonify, request
from flask_cors import CORS
#from serial import Serial
from interprete.parser import grammar


# serialArduino = Serial("COM3",9600)

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
            print("codigo enviado: "+ str(tmp.encode('ascii')))

            # serialArduino.write(tmp.encode('ascii'))
            # print("codigo en consola serial de arduino: " + serialArduino.readline())


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
    






