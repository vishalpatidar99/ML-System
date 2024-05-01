from ml_system_client import client
from protos.compiled import ml_system_pb2, ml_system_pb2_grpc
import grpc

address = "172.17.0.1" # for docker
# address = "127.0.0.1" # for local
port = 50052

def job_execution_req(file_content):

    with grpc.insecure_channel(f'{address}:{port}') as channel:
        print(f"INFO: Calling GRPC server on {address}:{port}")
        file_load_params = ml_system_pb2.JobExecutionInput(
            model_content=file_content
        )
        stub = client.ml_system_grpc_client(channel)

        # gettign response from ml-system via gRPC
        res = stub.JobExecutionReq(file_load_params)
    return res
