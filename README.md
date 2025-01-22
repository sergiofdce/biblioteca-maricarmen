# Biblioteca MariCarmen Brito

Software per a gestió de biblioteques.

En record de Mari Carmen Brito de l'Institut Esteve Terradas i Illa de Cornellà de Llobregat.

## Instal·lació

Instal·leu git, Python3 i l'entorn de treball virtualenv:

    sudo apt update
    sudo apt install python3-venv git

Cloneu el repositori:

    git clone https://github.com/AWS2/biblioteca-maricarmen
    cd biblioteca-maricarmen

Creem el virtualenv i carreguem les biblioteques:

    python3 -m venv env
    source env/bin/activate

Creem la base de dades de desenvolupament i afegim un superusuari:

    (env) $ cp .env.example .env
    (env) $ ./manage.py migrate
    (env) $ ./manage.py createsuperuser

Posem en marxa el servidor de desenvolupament:

    (env) $ ./manage.py runserver

