## About: A hands-on intro with protocol buffers (Python Usage)
## Build Docker Image
```
docker build -t py_protobuf .
```

## Run Docker Container
```
docker run -d --name py_protobuf -v $(pwd):/app py_protobuf
```

## Output W/ CLI Arguments
```
docker exec py_protobuf bash -c 'python protoWriterCLI.py Username 100 1234567890 10.5 1 CREDIT_CARD "Popcorn,Soda" protochild 30 "Action" 15 "Drama" 12 && python protoReader.py'
```

## Output W/O CLI Arguments
```
docker exec py_protobuf bash -c 'python protoWriter.py && python protoReader.py'
```
## Code Structure (After DOcker build)
```
 |- - - path_helpers.py
 |- - - protoCompile
 |          |-.keep
 |          |-proto_pb2.py
 |- - - protoWriterCLI.py
 - - - protoOutput
 |          |-protobuf_output
 |          |-.keep
 |- - - protoReader.py
 |- - - requirements.txt
 |- - - protoWriter.py
 |- - - Dockerfile
 |- - - protoDef
 |          |-proto.proto
 |- - - .gitignore
 |- - - README.md
 ```