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


**Create a Dokerfile**
Go the the backend folder and create a nefile name (Dockerfile)

```dockerfile
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```
