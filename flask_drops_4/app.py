import db
from converters import RegexConverter, ListConverter
from flask import Flask, abort, url_for

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
app.url_map.converters['list'] = ListConverter


@app.route('/')
def index():
    """Recebe http://localhost:5000/
    Responde com a lista de usuários com links"""
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f"""
                <li>
                    <a href='{url_for('user', usernames=[username])}'>
                        {user['name']}
                    </a>
                </li>
            """
        )
    html.append('</ul>')
    return '\n'.join(html)


@app.route('/user/<list:usernames>/', endpoint='user')
def profile(usernames):
    """Recebe http://localhost:5000/michael+david+john
    Responde com o perfil do usuário contendo nome, foto e telefone
    e um link para voltar"""
    html = ""
    for username in set(usernames):
        user = db.users.get(username)

        if user:
            html += f"""
                <h1>{user['name']}</h1>
                <img src="{user['image']}"/><br/>
                telefone: {user['tel']} <br/>
                <a href="{url_for('index')}">Voltar</a>
                <hr />
            """

    return html or abort(404, "Users not found")


@app.route('/user/<string:username>/<int:quote_id>/')
def quote(username, quote_id):
    """Recebe http://localhost:5000/michael/2
    Responde com a frase solicitada da lista de quotes do usuário"""
    # Se o user não for encontrado retorna um dict vazio {}
    user = db.users.get(username, {})
    quote = user.get('quotes', {}).get(quote_id)

    if user and quote:
        return f"""
            <h1>{user['name']}</h1>
            <img src="{user['image']}"/><br/>
            <p><q>{quote}</q></p>
            <hr />
        """
    else:
        return abort(404, "User or quote not found")


@app.route('/file/<path:filename>/')
def filepath(filename):
    """Recebe http://localhost:5000/file/diretory/sub/other/path.ext
    Responde com o caminho completo em forma de string"""
    return f"Argumento recebido: {filename}"


@app.route('/reg/<regex("[abc0-9]{1,3}"):value>')
def abcd(value):
    """Recebe http://localhost:5000/reg/ab4
    Responde com o valor recebido"""
    return f"{value}"


@app.route('/reg/<regex("a.*"):name>/')
def reg(name):
    """Recebe http://localhost:5000/reg/aisthestart
    Responde com o valor recebido"""
    return f"Argumento iniciado com a letra a: {name}"


@app.route('/reg/<regex("b.*"):name>/')
def reg_b(name):
    """Recebe http://localhost:5000/reg/bronx
    Responde com o valor recebido"""
    return f"Argumento iniciado com a letra b: {name}"


@app.route('/list/<list:names>')
def a_list(names):
    """Recebe http://localhost:5000/list/michael+david+john
    Responde com o valor recebido convertido em lista"""
    return f"{names}"
