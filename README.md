(PORTUGUESE (BR) BELOW)
# romAnPyI
## What is this program?
API with GraphQL. The use of the API is to annalyze the biggest roman numeral in a string of text, which was a challenge of a selection proccess. This application is a GraphQL API in Python, which uses several resources such as a DB, which can be made with PostgreSQL or using a URI of a cloud DB, an Apollo IDE platform, the Flask web-framework and the library SQLAlchemy.

## What is this app for?
GraphQL takes an input in text format, which contains two Roman numerals, compares them and returns which of the two numerals has the greater value. Returning the numeral and its respective value.

## How to use the application?
To use this application you must have Python installed.
Follow the steps below:
1) Download the zip file available at: https://github.com/Float-in-tec/romAnPyI
2) Choose the directory you want for the application and unzip the zip file there.
3) With windows, open the Windows prompt command line (Windows key + R, then type cmd and press enter) and open the app folder at the selected directory.
(Hint: use the command "cd folder_name" to open the desired folder and the command "cd.." to return to the previous folder)
4) Run the commands: "pip install -r requirements.txt" and "pip install psycopg2".
5) Connecting to a local Database (DB). If you want to use a URI from a DB cloud, read the next topic.
6) To create and connect your DB, download and install the PostgreSQL application (https://www.postgresql.org/). During installation, choose the password "Post!23!". If you want to use another password, change the text in api/__init__.py, in the part of the URI that says "Post!23". You can also follow the instructions in this video to download, install and build the DB (https://www.youtube.com/watch?v=qw--VYLpxG4&t=1966s).
7) With PostgreSQL installed, open the SQL Shell (psql). Press enter four times, creating the default servers, DB and ports (note, if you change any of these parameters, you will also need to change the information in "api/__init__.py") and reaching the line that asks for the password that was chosen during installation. Inform the password and press enter.
8) Return to the windows prompt and open python with the command "python" and then run the following commands:
- ">>> from app import db"
- ">>> db.create_all()"
- ">>> from api import app"
- ">>> quit()"
9) Run: "python -m flask run" in your terminal.
10) To connect to the IDE, go to studio.apollographql.com/dev and create a free account (you can use GitHub or email)
11) As soon as you connect to your account, the window to set up the graph will open, but you can also click the "+ New Graph" button. Select the Graph Type "Development" and enter the endpoint "http://localhost:5000/graphql"
12) Now you are in the GraphQL environment. To perform the operations, write the following text in "Operation":
- mutation {
-     search(text: "AXXBLX") {
-         number
-         value
-     }
- }
13) If you want to try new values, just change the content of the text "AXXBLX", keeping the same pattern, starting with the letter A to indicate where the first digit starts and using the letter B to indicate the second digit. Example: aXIVbCXXV or ACCbXXII

#### (Optional) How to connect to a cloud DB or other local DBs (alternative to local DB with postrgreSQL)
Attention: we recommend using local DB with postgreSQL as some DB clouds, like elephantSQL, are not supported.
If you still want to try to connect to the cloud, open the file "__init__.py" with a text editor and change the URI in the line "app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:Post!23 @localhost:5432/postgres"" and enter your DB URI as follows: app.config["SQLALCHEMY_DATABASE_URI"] = "YOUR_URI_CLOUD_HERE"

# (PT/BR) romAnPyI
## O que é esse aplicativo?
Esse aplicativo é uma API de GraphQL em Python, que utiliza diversos recursos como uma DB, que pode ser feita com PostgreSQL ou utilizado uma URI de uma DB cloud (em nuvem), uma palataforma IDE Apollo, a web-framework Flask e a biblioteca SQLAlchemy.  

## Para que serve esse aplicativo?
A GraphQL recebe uma entrada no formato de texto, que contém dois algarismos romanos, os compara e retorna qual dos dois algarismos possui maior valor. Retornando o algarismo e seu respectivo valor.

## Como utilizar o aplicativo?
Para utilizar esse aplicativo é necessário ter Python instalado.
Siga os seguintes passos:
1) Baixe o arquivo zip disponibilizado em: https://github.com/Float-in-tec/romAnPyI
2) Escolha o diretório que você deseja para o aplicativo e descompacte o arquivo zip nesse local.
3) Com o windows, abra a linha de comando do prompt Windows (tecla Windows + R, depois digite cmd e pressione enter) e abra a pasta do aplicativo no diretório selecionado.
(Dica: use o comando "cd nome_da_pasta" para abrir a pasta desejada e o comando "cd.." para retornar a pasta anterior)
4) Execute os comandos: "pip install -r requirements.txt" e "pip install psycopg2".
5) Conectando à um Banco de Dados (DB) local. Caso queira utilizar uma URI de uma DB cloud, leia o tópico seguinte.
6) Para criar e conectar sua DB, baixe e instale o aplicativo PostgreSQL (https://www.postgresql.org/). Durante a instalação, essolha a senha "Post!23!". Caso queira usar outra senha, altere o texto em api/__init__.py, no trecho da URI que está escrito o "Post!23". Você também pode seguir as instruções nesse vídeo para baixar, instalar e criar a DB (https://www.youtube.com/watch?v=qw--VYLpxG4&t=1966s).
7) Com o PostgreSQL instalado, abra o SQL Shell (psql). Aperte enter quatro vezes, criando os servidores, DB e ports padrões (observação, caso você altere algum desses parâmetros, será necessário alterar também as informações em "api/__init__.py") e chegando à linha que pede o password/senha que foi escolhida durante a instalção. Informe-a e pressione enter.
8) Retorne ao prompt do windows e abra o python com o comando "python" e depois execute os seguintes comandos:
- ">>> from app import db"
- ">>> db.create_all()"
- ">>> from api import app"
- ">>> quit()"
9) Execute: "python -m flask run" no seu terminal.
10) Para conectarmos à IDE, vá ao site studio.apollographql.com/dev e crie uma conta gratuita (pode usar GitHub ou e-mail)
11) Assim que você conectar à sua conta, abrirá a janela para fazer o set up da graph, mas você também pode clicar no botão "+ New Graph". Selecione o Graph Type "Development" e informe o endpoint "http://localhost:5000/graphql"
12) Pronto, agora você está no ambiente do GraphQL. Para realizar as operações, escreva o seguinte texto em "Operation":
- mutation {
-     search(text: "AXXBLX") {
-         number
-         value
-     }
- }
13) Caso queira experimentar novos valores, basta alterar o conteúdo do text "AXXBLX", mantendo o mesmo padrão, iniciando com a letra A para indicar onde inicia o primeiro algarismo e utilizando a letra B para indicar o segundo algarismo. Exemplo: aXIVbCXXV ou ACCbXXII

### (Opcional) Como conectar a uma DB cloud ou outras DBs locais (alternativa à DB local com postrgreSQL)
Atencão: recomendamos utilizar a DB local com postgreSQL pois algumas DB clouds, como a elephantSQL, não são compatíveis.
Se ainda assim quiser tentar conectar à cloud, abra o arquivo "__init__.py" com um editor de texto e altere a URI na linha "app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:Post!23@localhost:5432/postgres"" e insira a URI do seu DB, coforme a seguir: app.config["SQLALCHEMY_DATABASE_URI"] = "SUA_URI_CLOUD_AQUI" 

