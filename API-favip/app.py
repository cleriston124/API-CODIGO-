from flask import Flask, jsonify,request

app=Flask(__name__)

numero=[
    {
        "n1":3,
        "n2":4
    }
]

def somar_numero():
     for resultado in numero:
          if resultado.get("n1") and resultado.get("n2"):
            soma=resultado["n1"]+resultado["n2"]
            return soma
     

@app.route("/soma") 
def soma():
     resultado=somar_numero()
     return jsonify({
          "resultado":resultado,
          "n1":3,
          "n2":4,
          'operação':"soma"
             
        })

app.run(port=5000,host="localhost",debug=True)