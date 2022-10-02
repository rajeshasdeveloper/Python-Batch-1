apt update;
apt install nginx;
pip install -r requirements.txt
apt install gunicorn;
gunicorn app:app;