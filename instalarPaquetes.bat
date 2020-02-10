@ECHO OFF
REM Ir a carpeta SASTRE
@ECHO ON
cd SASTRE

@ECHO OFF
REM Crear el entorno virtual que GIT ignorara.
@ECHO ON
python -m venv sastreenv
CALL sastreenv\Scripts\activate.bat

@ECHO OFF
REM Copiar los comandos al Home del usuario.
@ECHO ON
ROBOCOPY ..\ %USERPROFILE% alias.bat

@ECHO OFF
REM Actualizar y mejorar el pip que este instalado.
@ECHO ON
python -m pip install --upgrade pip

@ECHO OFF
REM Instalar las paqueterias necesarias que vienen descritas en requirements.txt.
@ECHO ON
pip install -r requirements.txt

REM @ECHO OFF
REM REM Sirve para poder usar los comando y migrar despues la BD.
REM CALL alias.bat
REM @ECHO ON

@ECHO OFF
REM Crear la base de datos y el usuario de está base. Los borra si ya existen.
@ECHO ON
psql -U postgres postgres < "..\CREATE USER.sql"

@ECHO OFF
REM Migrar los datos de los modulos en la la base creada en el motor de base de datos.
@ECHO ON
python manage.py migrate

@ECHO OFF
REM Correr el servidor para probar su correcto funcionamiento. 
python manage.py runserver
@ECHO ON


PAUSE