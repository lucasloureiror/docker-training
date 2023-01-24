docker build -t mysql .

docker run mysql -p 3030:3306

docker run mysql -v ./docker/data/mysql:/var/lib/mysql --env=MYSQL_ROOT_PASSWORD=root --env="MYSQL_PASSWORD=root" --env="MYSQL_DATABASE=test"