dir=protos/compiled

python -m grpc_tools.protoc \
-Iprotos/spec \
--python_out=protos/compiled \
--pyi_out=protos/compiled \
--grpc_python_out=protos/compiled protos/spec/ml_system.proto
 
# Fix protoc-gRPC compile bug (see more on README.md)
sed 's/^import _pb2 as ml_system__pb2/from \. import ml_system_pb2 as ml_system__pb2/' protos/compiled/ml_system_pb2_grpc.py > /tmp/workaround.py && cat /tmp/workaround.py > protos/compiled/ml_system_pb2_grpc.py
