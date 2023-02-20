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

**Run Python**
-Youll need to set up the environment variables , run python and append the url

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
- you should get back json

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

#python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]



```
