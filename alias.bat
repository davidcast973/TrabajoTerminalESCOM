@ECHO OFF
doskey ls= dir /b
doskey irtt= cd E: ^& cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE

doskey vir= cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE\sastreenv ^&^& cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE ^&^& E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE\sastreenv\Scripts\activate
doskey correr= python manage.py runserver
doskey cambios= python manage.py makemigrations ^&^& python manage.py migrate
doskey run= python manage.gy runserver

E:
cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE
E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE\sastreenv\Scripts\activate