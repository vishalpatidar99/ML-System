from protos.compiled import ml_system_pb2, ml_system_pb2_grpc

def ml_system_grpc_client(channel):
    return ml_system_pb2_grpc.MlSystemStub(channel)