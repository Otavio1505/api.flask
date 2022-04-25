from flask import Flask, request, Response
empregados = [
    {"nome": "Marcela", "cargo": "Analista", "salario": "5000", "sexo": "Feminino"},
    {"nome": "Diego", "cargo": "Analista", "salario": "4000", "sexo": "Masculino"},
    {"nome": "Maria", "cargo": "Desenvolvedor", "salario": "5000", "sexo": "Feminino"},
    {"nome": "Pedro", "cargo": "Supervisor", "salario": "6000", "sexo": "Masculino"},
    {"nome": "Gabriel", "cargo": "Gerente", "salario": "8500", "sexo": "Masculino"},
    {"nome": "Renata", "cargo": "Desenvolvedor", "salario": "5000", "sexo": "Feminino"}
             ]

users = [
    {"username": "Otavio", "secret": "@admin"}
        ]

def check_users(username, secret):
    for user in users:
        if (user["username"] == username) and (user["secret"] == secret):
            return True
    return False
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Olá mundo, esta é a home page</h1>"

@app.route("/empregados")
def get_empregados():
    return {"empregados": empregados}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in empregados:
        if cargo == empregado['cargo']:
            out_empregados.append(empregado)
    return {"empregados": out_empregados}

@app.route("/empregados/<info>/<value>")
def get_empregados_info(info, value):
    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado:
                    out_empregados.append(empregado)
                if type(value_empregado) == int:
                    if int(value) == value_empregado:
                        out_empregados.append(empregado)
    return {"empregados": out_empregados}


@app.route("/informations", methods=['POST'])
def get_empregados_post():

    username = request.form["username"]
    secret = request.form["secret"]

    if not check_users(username, secret):
        return Response("Unauthorized", status=401)

    info = request.form['info']
    value = request.form['value']

    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado:
                    out_empregados.append(empregado)
                if type(value_empregado) == int:
                    if int(value) == value_empregado:
                        out_empregados.append(empregado)
    return {"empregados": out_empregados}


if __name__ == "__main__":
    app.run(debug=True)