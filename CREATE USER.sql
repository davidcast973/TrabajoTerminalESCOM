DROP DATABASE IF EXISTS ttsastre;
DROP USER IF EXISTS susastre;
CREATE DATABASE ttsastre;
CREATE USER susastre WITH PASSWORD 'susastre';
GRANT ALL PRIVILEGES ON DATABASE "ttsastre" to susastre;