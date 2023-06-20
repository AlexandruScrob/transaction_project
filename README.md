### Pași Environment

1.  Crearea unui virtual environment:

        python -m venv venv

2. Activare virtual environment:

Windows:

        venv\Scripts\activate.bat


Linux/MacOS

        source venv/bin/activate


3.  Instalare dependințe:


Manual:

        pip install [librărie]


Din fișier de requirements

        pip install -r requirements.txt


### Rulare

Rulare aplicație din directorul de bază (root), cu reload la modificări:

        uvicorn main:app --reload

Rulare aplicație când se află în subdirector (ex. app)

        PYTHONPATH=app uvicorn app.main:app --reload

**NB:** Să activați env-ul înainte să rulați aplicația


### Rulare în debug mode
Pentru rulare în mod debugging va trebui să modificați fișierul de launch.json

{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "envFile": "${workspaceFolder}/.env",
      "env": {
        "PYTHONPATH": "app",
      },
      "args": ["app.main:app", "--reload"],
      "jinja": true,
      "justMyCode": false
    },
    {
      "name": "Debug Unit Test",
      "type": "python",
      "request": "test",
      "justMyCode": false
    }
  ]
}


### Exemplu .env

DB_PATH="sqlite:///app/sql_transactions.db"
AUTH_USERNAME="username"
AUTH_PASSWORD="password"
