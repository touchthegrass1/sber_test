### Запуск
```
cat > env.sh << EOF
export DJANGO_SECRET_KEY='cyhl=4u*!$!0r@kn9g9767afnu6dppt5q#*@t)u_+h(gy9d_!j'
export DJANGO_DEBUG='True'
export DJANGO_ALLOWED_HOSTS='127.0.0.1,localhost,172.17.0.1'
export POSTGRES_DB_LOGIN='xops_db_user'
export POSTGRES_DB_PASSWORD='xops_db_password'
export POSTGRES_DB_HOST='db'
export POSTGRES_DB_PORT=5432
export POSTGRES_DB_NAME='xops_db'
EOF

source env.sh
docker-compose up
```
### Тестирование
```
python3.10 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py test
```