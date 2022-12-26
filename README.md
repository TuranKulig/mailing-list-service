# Mailing List

# Getting Started
### Follow the instruction and enjoy API

#### 1. Clone the repository from Gitlab.
```
git clone https://gitlab.com/kulig.turan/mailing.git
```

#### 2. Create virtual environment.
```
python -m venv venv
```

#### 3. Activate environment.
```
source\venv\bin\activate
```

#### 4. Install requirements.
```
pip install -r requirements.txt
```

#### 5. Create and apply migrations database.
```
python manage.py makemigrations
python manage.py migrate
```

#### 6. Run server.
```
python manage.py runserver
```

#### URLS
```
http://0.0.0.0:8000/
```
```
http://0.0.0.0:8000/client/
```
```
http://0.0.0.0:8000/message/
```
```
http://0.0.0.0:8000/mailing/
```
```
http://0.0.0.0:8000/mailing/info/
```
```
http://0.0.0.0:8000/docs/
```
```
http://0.0.0.0:8000/refresh/
```
```
http://0.0.0.0:8000/obtain/
```
```
http://0.0.0.0:8000/admin/
```
