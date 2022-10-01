
## To run this project, you need to have python installed properly and then install django framework and necessary libraries for django gis extensions:
`
pip install django 
sudo apt-get install binutils libproj-dev gdal-bin
pip install psycopg2-binary
`

## To setup the database system properly, you need to have docker set up properly. The following command will download the docker image of kartoza/postgis and run a container for that image
`
sudo docker run --name=postgisKartozaTestContainer -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 1111:5432 kartoza/postgis
`

## To stop the container then start it again, you can use the following 2 commands:
`
sudo docker container stop postgisKartozaTestContainer
sudo docker container start postgisKartozaTestContainer
`

## When the docker container is setup correctly and all the requirements are satisfied, you can create superuser for the website with the command
`
python manage.py createsuperuser
`

## Run the following commands to setup the database properly
`
python manage.py makemigrations
python manage.py migrate
`

## To run the server, execute:
`
python manage.py runserver
`
## To visit the website, go to http://127.0.0.1:8000/ 

