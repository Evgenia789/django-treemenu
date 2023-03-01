# django-treemenu

Django app that implements a tree menu via template tag


## Technology stack

- Python
- Django
- SQLite
- git

## How to launch a project by Docker

Clone the repository and go to it on the command line

```bash
    git clone https://github.com/Evgenia789/django-treemenu.git
    cd tree_menu
```

Create and activate a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

In the project directory, create a .env file in which you write the following environment variables. (SECRET_KEY need to take from settings.py)

```python
SECRET_KEY=<SECRET_KEY>
```

Install dependencies from a file requirements.txt

```bash
 pip install -r requirements.txt 
```

Perform migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a Superuser

```bash
 python manage.py createsuperuser
```

Launch a project

```bash
python manage.py runserver
```

---

You can try to access the Django admin at

```bash
http://127.0.0.1:8000/admin
```

## License

This project is under the MIT License - see the LICENSE file for details.
