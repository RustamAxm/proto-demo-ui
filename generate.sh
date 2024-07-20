#!/bin/bash -ex

mkdir -p ./generation/py_gen
mkdir -p ./generation/cpp_gen

protoc -I./proto --python_out=./generation/py_gen ./proto/proto_app.proto
protoc -I./proto --cpp_out=./generation/cpp_gen ./proto/proto_app.proto