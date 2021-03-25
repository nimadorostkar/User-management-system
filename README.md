# User-Management-System. (User interaction)

-User interaction django web application for send and receive text and file information with profile dashboard for users.


<hr>

## How to run this project


1. **Clone the project**

```sh
git clone https://github.com/nimadorostkar/User-management-system.git
```

2.  **Make sure you are in *User-management-system* folder**


3. **Active virtual environment (env)**
```sh
python3 -m venv env
source env/bin/activate
```

4. **install requirements**
```sh
pip install -r requirements.txt
```

5. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

```

6. **Run Server**

```sh
python manage.py runserver
```

7. **And Creating an admin user (superuser)**

```sh
python manage.py createsuperuser
```


<hr>


