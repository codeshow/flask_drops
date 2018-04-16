# Flask Drops parte 3
## Roteamento de URLS no Flask

VIDEO: https://youtu.be/wD_Qu6qtx1g

Neste vídeo apresento alguns detalhes sobre os elementos que formam uma URL e como representamos esses elementos como objetos no Flask. Também mostro 2 maneiras para registrar URLs e um exemplo real do uso do terminal interativo do Flask.

Colabore:
Patreon(U$)
https://www.patreon.com/cursodepython

Padrim(R$)
https://www.padrim.com.br/cursodepython

Apoia-se(R$)
https://apoia.se/cursodepython

Links:
Bruno Rocha: http://brunorocha.org
Twitter: http://twitter.com/rochacbruno 
Tutorial de Flask: http://flask.wtf
Github do CursoDePython: http://github.com/cursodepythonoficial
Grupo da comunidade Flask no Telegram: http://t.me/flaskbrasil

Mencionado:

Flask Shell Ipython
https://github.com/ei-grad/flask-shell-ipython


Toda semana tem video novo com dicas de Python e Flask!

Inscreva-se no canal do curso de Python: https://www.youtube.com/c/CursoDePython?sub_confirmation=1 

Inscreva-se no Castálio Podcast: https://www.youtube.com/c/castaliopodcast?sub_confirmation=1


# Descrição:

O roteamento de URLS é a parte principal de qualquer aplicação web, URL é o nome dado ao endereço de um recurso ou página na internet e a URL é formada por alguns elementos sendo o primeiro deles o protocolo.

## http://

No nosso caso iremos utilizar o protocolo http para transferir texto da app flask para o navegador então nossas urls sempre começarão com este protocolo, mas no decorrer desta séries ainda veremos o https:// e o ws://

## site.com

O endereço do servidor ou “host” é a segunda parte e determina em qual servidor o recurso está localizado, quando executamos a aplicação em nosso computador local utilizamos “localhost”

## Porta TCP 

A Porta TCP utilizada por padrão é a porta 80 mas se quisermos especificar uma porta diferente fazemos logo após o endereço do servidor, no caso do flask durante o desenvolvimento usaremos a porta :5000

## Rota

A partir daqui temos os elementos que identificam o recurso ou página que queremos carregar, essa parte pode ser chamada de “path”, “caminho” ou “rota” e na maioria das vezes será chamada de rota!

Por exemplo em um site como o Youtube podemos ter uma rota `/user` que define uma funcionalidade do site e esta rota pode ainda receber o username `/user/brunorocha/` sendo que neste exemplo `/user` é uma rota fixa e o nome do usuário é a parte dinâmica que pode ser alterada a cada requisição.


# Route 

Para informar ao Flask as regras de URL precisamos criar objetos Python que também chamamos de rotas.

As rotas no Flask são formadas por alguns elementos:

## Regra (ou rule) 

o caminho da rota fixa ‘/user/brunorocha’ ou um padrão ‘/user/<username>’ que será usado para uma busca por similaridade

## View 

Além da regra precisamos informar uma view, que é uma função ou classe python que será invocada quando aquela URL for requisitada

## Methods

Também informamos uma lista de métodos (verbos) HTTP que a rota pode processar, por padrão o flask já coloca o método [‘GET’] portanto podemos omitir esse valor por enquanto

## Endpoint

Um valor muito importante a ser definido é o endpoint, que é um nome unico que pode ser usado para referenciar esta URL dentro da aplicação.

Além disso uma série de chaves de configuração como redirect, defaults e outras coisas que caso vc tenha curiosidade poderá verificar na documentação no link que estará na descrição do video.

# Processo de roteamento na prática


```bash
pip install flask ipython flask-shell-ipython
export FLASK_APP=app.py
flask shell
```

Quando o cliente requisita uma URL o servidor web consulta uma lista localizada em `flask.url_map`.

Ex: `/user/<username>/`

Existem 2 maneiras de adicionarmos novas regras de URL a esta lista:

## Decorator:

```python
@route….
def foo():
```

## Metodo

```python
def bar():
app.add_url…
```

Quando o client requisitar a url, será feita uma busca na lista de regras, e a que tiver maior match será invocada.

## Para testar:

```python
app.test_client().get('/user/bruno').status
app.test_client().get('/user/bruno').headers
app.test_client().get('/user/david/).data
app.test_client().get('/user/michael/').data
```
