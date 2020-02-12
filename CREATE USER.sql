DROP DATABASE IF EXISTS ttsastrePrueba;
DROP USER IF EXISTS susastrePrueba;
CREATE DATABASE ttsastrePrueba;
CREATE USER susastrePrueba WITH PASSWORD 'susastrePrueba';
GRANT ALL PRIVILEGES ON DATABASE ttsastrePrueba to susastrePrueba;
