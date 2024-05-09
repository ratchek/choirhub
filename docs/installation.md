# Getting started
## Project Setup
```
git clone git@github.com:ratchek/choirs.git
cd choirs/
python3 -m venv --prompt choirs env
source env/bin/activate
pip install -r requirements/local.txt
./manage.py collectstatic
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
The site should be running on http://localhost:8000/
