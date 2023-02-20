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

https://code.visualstudio.com/docs/containers/overview

Gitpod is preinstalled with theis extension  


#Containerize Backend

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
- make sure to unlock the port on the port tab
- open the link for 4567 in your browser
- append to the url to /api/activities/home
- you should get back json data

**Build Container image**
docker build -t  backend-flask ./backend-flask


Run Container
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

#Containerize Frontend

**Run NPM Install**
We have to run NPM Install before building the container since it needs to copy the contents of node_modules
```
cd frontend-react-js
npm i
```

**Create Docker File**
- Create a file here: frontend-react-js/Dockerfile
```
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```

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
```
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





