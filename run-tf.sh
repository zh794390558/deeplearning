#!/usr/bin/env bash

docker run -it -p 8888:8888 -p 6006:6006 -v /tmp/notebootk:/notebootk tensorflow:v0.1
