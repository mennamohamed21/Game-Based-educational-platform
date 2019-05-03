#!/bin/sh
docker login --username $DOCKER_USER --password $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t mennamohamed21/game-based-educational-platform:$TAG .
docker tag mennamohamed21/game-based-educational-platform $DOCKER_REPO
docker push $DOCKER_REPO