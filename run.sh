docker run \
    --name fogbed \
    -it \
    --rm \
    --privileged \
    --pid='host' \
    -v $(pwd):/fogbed \
    -v /var/run/docker.sock:/var/run/docker.sock fogbed /bin/bash
    #-e USER=$USER  -e USERID=$UID fogbed bash

#   