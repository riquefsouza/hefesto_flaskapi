python3 -m venv venv
. venv/bin/activate
pip install -U pip setuptools

env | grep VIRTUAL_ENV

pip install Flask

pip install --upgrade pip

ls flaskapi-env/bin

touch .gitignore
__pycache__
flaskapi-env
.DS_Store

git clone https://github.com/riquefsouza/hefesto_flaskapi.git
git init
git add .
git commit -m "hefesto_flaskapi first commit"
git push

pip install SQLAlchemy
pip install flask-sqlalchemy
