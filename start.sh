apt update;
apt install nginx;
apt install gunicorn;
gunicorn app:app;