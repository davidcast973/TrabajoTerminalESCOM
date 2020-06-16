@ECHO OFF
doskey ls= dir /b
doskey irtt= C: ^& cd C:\TrabajoTerminalESCOM\SASTRE

doskey vir= cd C:\TrabajoTerminalESCOM\SASTRE\sastreenv ^&^& cd C:\TrabajoTerminalESCOM\SASTRE ^&^& C:\TrabajoTerminalESCOM\SASTRE\sastreenv\Scripts\activate
doskey correr= python manage.py runserver
doskey cambios= python manage.py makemigrations ^&^& python manage.py migrate
doskey run= python manage.gy runserver

C:
cd C:\TrabajoTerminalESCOM\SASTRE
C:\TrabajoTerminalESCOM\SASTRE\sastreenv\Scripts\activate