# lindy.ai CLI (scroll down for Russian README)

To run from source code:

1. Download the source code archive


2. Create a venv:

```bash
python -m venv venv
```

3. Activate the venv:

* For Windows (PowerShell):

```powershell
venv/bin/Activate.ps1
```

* For Linux/macOS (Bash):

```bash
source venv/bin/activate
```

4. Install requirements:

```bash
pip install -r requirements.txt
```

5. Add the HTTP Requests integration and enter the system prompt in lindy.ai:

```bash
"you'll figure it out, it's easy"
```

```bash
You are a local AI developer agent. Use the HTTP Request tool to interact with the system:
- Create file: action="create_file", params={"filename": "...", "content": "..."}
- Patch file: action="patch_file", params={"filename": "...", "find": "...", "replace": "..."}
- Read file: action="read_file", params={"filename": "..."}
- Run command: action="execute_command", params={"command": "..."}
```

6. Install the localtunnel package via npm:

```bash
sudo npm install -g localtunnel
```

7. Start the tunnel on port 5000 (or the port of your flask server from lindy_server):

```bash
npx localtunnel --port 5000
```

8. Run lindy_server:

```bash
python lindy_server.py
```

9. Run the CLI code editor:

```bash
python cli.py
```

#Russian README

Для запуска из source кода:
1. Скачайте архив кода
2. Создайте venv:
```bash
python -m venv venv

```

3. Активируйте venv:

* Для Windows (PowerShell):

```powershell
venv/bin/Activate.ps1
```

* Для Linux/macOS (Bash):

```bash
source venv/bin/activate
```

4. Установите зависимости:

```bash
pip install -r requirements.txt
```

5. Добавьте интеграцию HTTP Requests и впишите системный промт в lindy.ai:
```bash
"разберетесь сами, это легко."
```
```bash
You are a local AI developer agent. Use the HTTP Request tool to interact with the system:
- Create file: action="create_file", params={"filename": "...", "content": "..."}
- Patch file: action="patch_file", params={"filename": "...", "find": "...", "replace": "..."}
- Read file: action="read_file", params={"filename": "..."}
- Run command: action="execute_command", params={"command": "..."}
```

6. Установите пакет localtunnel через npm
```bash
sudo npm install -g localtunnel
```
7. Запустите туннель на порт 5000(или же порт вашего flask-сервера из lindy_server)
```bash
npx localtunnel --port 5000
```
8. Запустите lindy_server
```bash
python lindy_server.py
```
9. Запустите CLI редактор кода
```bash
python cli.py
```


#LICENSE
GPL v3.0