cd SASTRE

python -m venv sastreenv
CALL sastreenv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install -r requirements.txt
psql -U postgres postgres < "..\CREATE USER.sql"
python manage.py migrate

SET /P opt= Deseas crear usuario y base de datos en postgres? (s/n)
IF "%opt%"=="n" GOTO continue


python manage.py runserver

ROBOCOPY ..\ %USERPROFILE% alias.bat