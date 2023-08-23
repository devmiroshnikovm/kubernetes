#!/bin/bash

# Adding set -e to the top of your script will ensure that if any command fails (exits with a non-zero status),
# the script will exit immediately.

set -e

VERSION=1.100


docker build -t my-flask-app:$VERSION . 
docker tag my-flask-app:$VERSION miroshnikovm/my-flask-app:$VERSION
#docker login 
docker push miroshnikovm/my-flask-app:$VERSION
 