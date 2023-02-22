# Week 1 — App Containerization

**WHy do we need containers?**
- Containers make the appps more portable   
- it reuces time spent on configuration
ease on deployment (you can easily kill and start up again)
- it allows you to be closer to the end environment you plan on deploying when testing applications 
- it prevents you from destroing things that could cause that could cause misconfiguration.
- without containerization you get exposed to variants on your system or different versions of a particular package (modules) with containers it simply fies everything by having that baswline to worrkwith which others can adopt and test that it works with that environment.  

VSCode Docker Extension
Docker for VSCode makes it easy to work with Docker

![Docker](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/docker.PNG)

https://code.visualstudio.com/docs/containers/overview

Gitpod is preinstalled with theis extension  


# Containerize Backend

**Create a Dokerfile**
- Go the the backend folder and create a nefile name (Dockerfile)

```dockerfile
#This downloads python version fron dockerhub
FROM python:3.10-slim-buster

#This acts like change directory inside the container side
#this contaiins libaries we want to install to run the app
#make a new folder inside the container
WORKDIR /backend-flask

#Outside container -> Inside container
COPY requirements.txt requirements.txt

#Inside the container
#Install the python libraries used to run the app
RUN pip3 install -r requirements.txt

#Outside container -> Inside container
# (.) Everything in that current directory
#First (.) means everything /backend-flask outside the container
#Second (.) means everything /backend-flask inside the container
COPY . .

#Set Environment variable
#it remains set inside the container
ENV FLASK_ENV=development

EXPOSE ${PORT}

#This starts up the container
#python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

**Run Python**
- After youve create your dockerfile
- Youll need to set up the environment variables , run python(container) and append the url

```
cd backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
python3 -m flask run --host=0.0.0.0 --port=4567
cd ..
```
![pythonrun](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/python.PNG)

- make sure to unlock the port on the port tab
- open the link for 4567 in your browser
- append to the url to /api/activities/home
- you should get back json data

**Build Container image**
docker build -t  backend-flask ./backend-flask

![dockerimages](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/dockerimages.PNG)

**Run Container**
```
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```
To get into your container 
- click on the docker imaage on 
- the tool bar and rignt click on the container 
- click attach shell
or use this command
```
CONTAINER_ID=$(docker run --rm -p 4567:4567 -d backend-flask)
docker exec CONTAINER_ID -it /bin/bash
```

**Delete an Image**
```
docker image rm backend-flask --force
```
docker rmi backend-flask is the legacy syntax, you might see this is old docker tutorials and articles.

There are some cases where you need to use the --force

**Overriding Ports**
```
FLASK_ENV=production PORT=8080 docker run -p 4567:4567 -it backend-flask
```
Look at Dockerfile to see how ${PORT} is interpolated

# Containerize Frontend

**Run NPM Install**
We have to run NPM Install before building the container since it needs to copy the contents of node_modules
```
cd frontend-react-js
npm i
```

**Create Docker File**
- Create a file here: frontend-react-js/Dockerfile
```dockerfile
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```
![npminstall](https://github.com/Elochike/aws-bootcamp-cruddur-2023/blob/main/images/npminstall.PNG)

**Build Container**
```
docker build -t frontend-react-js ./frontend-react-js
```
**Run Container**
```
docker run -p 3000:3000 -d frontend-react-js
```

**Multiple Containers**
- Create a docker-compose file
- Create docker-compose.yml at the root of your project.
```docker-compose
version: "3.8"
services:
  backend-flask:
    environment:
      FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
      BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./backend-flask
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/backend-flask
  frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js

# the name flag is a hack to change the default prepend folder
# name when outputting the image names
networks: 
  internal-network:
    driver: bridge
    name: cruddur
```

# Adding DynamoDB Local and Postgres
We are going to use Postgres and DynamoDB local in future labs We can bring them in as containers and reference them externally

Lets integrate the following into our existing docker compose file:

**Postgres**
```
services:
  db:
    image: postgres:13-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - '5432:5432'
    volumes: 
      - db:/var/lib/postgresql/data
volumes:
  db:
    driver: local
```

To install the postgres client into Gitpod
```
- name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
 ```
         
**DynamoDB Local**
```
services:
  dynamodb-local:
    # https://stackoverflow.com/questions/67533058/persist-local-dynamodb-data-in-volumes-lack-permission-unable-to-open-databa
    # We needed to add user:root to get this working.
    user: root
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
 ```
 
Example of using DynamoDB local https://github.com/100DaysOfCloud/challenge-dynamodb-local

# Volumes

directory volume mapping

volumes: 
- "./docker/dynamodb:/home/dynamodblocal/data"
named volume mapping

volumes: 
  - db:/var/lib/postgresql/data

volumes:
  db:
    driver: local







# Homework challenges
***Research on the best practises of writing a dockerfile***

- Avoid installing unnecessary packages -If you install unnecessary packages in your dockerfile, it will increase the build time and the size of the image. Also, each time you make changes in the dockerfile, you will have to go through all the steps to build that same large image again and again. This creates a cascading downward effect on the performance. To avoid this, it’s always advised that only include those packages that are of utmost importance and try avoiding installing the same packages again and again. 

```
RUN pip3 install -r requirements.txt
```
- Chain all RUN commands
Each RUN command creates a cacheable unit and builds a new intermediate image layer every time. You can avoid this by chaining all your RUN commands into a single RUN command. Also, try to avoid chaining too much cacheable RUN commands because it would then lead to the creation of a large cache and would ultimately lead to cache burst.`

```
RUN apt-get -y install firefox
RUN apt-get -y install vim
RUN apt-get -y update
```
The above commands can be chained into a single RUN command.

```
RUN apt-get -y install firefox \
   && apt-get -y install vim \
   && apt-get -y update
```

- you don’t want to store in the image or in source control, such as:
Usernames and passwords
TLS certificates and keys
SSH keys
Other important data such as the name of a database or internal server.

- Use a .dockerignore file:
Similar to .gitignore file, you can specify files and directories inside .dockerignore file which you would like to exclude from your Docker build context. This would result in removing unnecessary files from your Docker Container, reduce the size of the Docker Image, and boost up the build performance.

- Using a minimal base image:
Using a larger base image with more packages and libraries installed can increase the size of the final Docker image and potentially decrease performance. It is generally recommended to use a minimal base image, such as Alpine Linux, as a starting point for building a Docker image. This can help to reduce the size and complexity of the final image, leading to better performance and faster build times. Additionally, using a minimal base image can also improve security by reducing the number of potential vulnerabilities that may be present in the final image.

