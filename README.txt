# Aplicativo gerado para o teste técnico da empresa studio sol.
##O que é esse aplicativo?
Esse aplicativo é uma API de GraphQL em Python, que utiliza diversos recursos como uma DB, que pode ser feita com PostgreSQL ou utilizado uma URI de uma DB cloud (em nuvem), uma palataforma IDE Apollo, a web-framework Flask e a biblioteca SQLAlchemy.  

## Para que serve esse aplicativo?
A GraphQL recebe uma entrada no formato de texto, que contém dois algarismos romanos, os compara e retorna qual dos dois algarismos possui maior valor. Indicando o algarismo e seu respectivo valor.

## Como utilizar o aplicativo?
Para utilizar esse aplicativo é necessário ter Python instalado.
Siga os seguintes passos:
1) Baixe o arquivo zip disponibilizado no link: https://drive.google.com/drive/folders/1gctB_B9yrESfbccf4wSXoNx2s_YCFWJo?usp=sharing
2) Escolha o diretório que você deseja para o aplicativo e descompacte o arquivo zip nesse local.
3) Com o windows, abra a linha de comando do prompt Windows (tecla Windows + R, depois digite cmd e pressione enter) e vá até o diretório selecionado.
(Dica: use o comando "cd nome_da_pasta" para abrir a pasta desejada e o comando "cd.." para retornar a pasta anterior)
4) Entre na pasta inicial "SOLQL", depois na pasta "SOLQLapp".
6) Execute os comandos: "pip install -r requirements.txt" e "pip install psycopg2".
7) Conectando à um Banco de Dados (DB) local. Caso queira utilizar uma URI de uma DB cloud, leia o tópico seguinte.
8) Para criar e conectar sua DB, baixe e instale o aplicativo PostgreSQL (https://www.postgresql.org/). Durante a instalação, essolha a senha "Post!23!". Caso queira usar outra senha, altere o texto em api/__init__.py, no trecho da URI que está escrito o "Post!23". Você também pode seguir as instruções nesse vídeo para baixar, instalar e criar a DB (https://www.youtube.com/watch?v=qw--VYLpxG4&t=1966s).
9) Com o PostgreSQL instalado, abra o SQL Shell (psql). Aperte enter quatro vezes, criando os servidores, DB e ports padrões (observação, caso você altere algum desses parâmetros, será necessário alterar também as informações em "api/__init__.py") e chegando à linha que pede o password/senha que foi escolhida durante a instalção. Informe-a e pressione enter.
10) Retorne ao prompt do windows e abra o python com o comando "python" e depois execute as seguintes linhas:
>>> from app import db
>>> db.create_all()
>>> from api import app
>>> quit()
11) Após dar o comando "quit()" e encerrar o python, execute: "python -m flask run" no seu terminal.
11) Para conectarmos à IDE, vá ao site studio.apollographql.com/dev e crie uma conta gratuita (pode usar GitHub ou e-mail)
12) Assim que você conectar à sua conta, abrirá a janela para fazer o set up da graph, mas você também pode clicar no botão "+ New Graph". Selecione o Graph Type "Development" e informe o endpoint "http://localhost:5000/graphql"
13) Pronto, agora você está no ambiente do GraphQL. Para realizar as operações, escreva o seguinte texto em "Operation":
mutation {
    search(text: "AXXBLX") {
        number
        value
    }
}
14) Caso queira experimentar novos valores, basta alterar o conteúdo do text "AXXBLX", mantendo o mesmo padrão, iniciando com a letra A para indicar onde inicia o primeiro algarismo e utilizando a letra B para indicar o segundo algarismo. Exemplo: aXIVbCXXV ou ACCbXXII

## Como conectar a uma DB cloud ou outras DBs locais (alternativa à DB local com postrgreSQL)
Atencão: recomendamos utilizar a DB local com postgreSQL pois algumas DB clouds, como a elephantSQL, não são compatíveis.
Se ainda assim quiser tentar conectar à cloud, abra o arquivo "__init__.py" com um editor de texto e altere a URI na linha "app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:Post!23@localhost:5432/postgres"" e insira a URI do seu DB, coforme a seguir: app.config["SQLALCHEMY_DATABASE_URI"] = "SUA_URI_CLOUD_AQUI" 

