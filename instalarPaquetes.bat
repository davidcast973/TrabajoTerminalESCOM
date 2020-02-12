cd SASTRE

python -m venv sastreenv
sastreenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
psql -U postgres postgres < "..\CREATE USER.sql"
django-admin.exe startproject prueba .
python manage.py runserver
python manage.py migrate

SET /P opt= Deseas crear usuario y base de datos en postgres? (s/n)
IF "%opt%"=="n" GOTO continue


python manage.py runserver

ROBOCOPY ..\ %USERPROFILE% alias.bat