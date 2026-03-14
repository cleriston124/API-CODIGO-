from flask import Flask , jsonify , request

api=Flask(__name__)

# rota para colocar na url do navegador
@api.route("/calcular")
def calcular():
    # numeros e a operação que vc vai escolher para colocar no url
    n1 = int(request.args.get("n1"))
    n2 = int(request.args.get("n2"))
    operacao = request.args.get("op")

    n1=int(n1)
    n2=int(n2)

    if operacao == "soma":
        resultado = n1 + n2

    elif operacao == "subtracao":
        resultado = n1 - n2

    elif operacao == "multiplicacao":
        resultado = n1 * n2

    elif operacao == "divisao":
        resultado = n1 / n2

    else:
        return jsonify({"erro": "operação inválida"})

    return jsonify({
        "numero1": n1,
        "numero2": n2,
        "operacao": operacao,
        "resultado": resultado
    })

#forma como vai rodar nossa API
api.run(port=5000,host="localhost",debug=True)

