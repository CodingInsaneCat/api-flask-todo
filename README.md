# Api Flask #

API ToDo list apenas testando o código em python 


## Requisitos para executar ##
- python==3.13
- bcrypt==4.3.0
- blinker==1.9.0
- click==8.2.1
- Flask==3.1.1
- Flask-Bcrypt==1.0.1
- Flask-JWT-Extended==4.7.1
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.2
- PyJWT==2.10.1
- Werkzeug==3.1.3

## Como instalar os módulos? ##

- Baixe o python na versão 3.13
- Utilize o venv( ambiente virtual) para instalar os módulos necessários, se não tiver instalado execute o comando abaixo via Pip: 
````
python -m pip install --user virtualenv
````
Criar o ambiente virtual 
````
python -m venv venv
````
Utilizar o ambiente, configuração para Linux/Mac: 
````
source venv/bin/activate
````
Utilizar o ambiente, configuração para Windows: 
````
venv\Scripts\activate
````

## Como executar?##
Utilize o venv( ambiente virtual) para instalar os módulos necessários, descrito nos passos anteriores

- Instale as depedencias que estão descritas dentro do requeriments.txt com seguinte comando: 
````
pip install -r requeriments.txt
````
- Abra o arquivo app.py e execute-o, se estiver utilizando o VSCode, utilize o runner integrado.
- Caso não esteja execute o comando no terminal do Windows/Linux e ou Mac
````
python app.py
````


