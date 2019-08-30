```
FROM python:3.7-slim

## make a local directory
RUN mkdir /opt/hello_app

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/hello_app

# copy requirements.txt to /app
ADD requirements.txt .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# now copy all the files in this directory to /code
ADD . .

# Listen to port 80 at runtime
EXPOSE 5000

ENV FLASK_APP=app
ENV FLASK_ENV=development

# Define our command to be run when launching the container
CMD ["flask", "run", "--host", "0.0.0.0"]
```
