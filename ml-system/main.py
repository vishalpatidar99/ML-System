import os, sys
from concurrent import futures
import logging
import grpc

# appenidng protos files path in system for importing them
sys.path.append(os.getcwd() + "/protos/compiled")

from protos.compiled import ml_system_pb2, ml_system_pb2_grpc
from src import ml

address = "0.0.0.0"
port = 50052


class MlSystemServicer(ml_system_pb2_grpc.MlSystemServicer):

    def JobExecutionReq(self, request, context):
        try:
            logging.info("ML job recieved for execution")
            result = ml.job_executor_handler(request.model_content)
            logging.info("Ml job executed")
            return ml_system_pb2.JobExecutionOutput(result=result)
        except Exception as e:
            error_message = f"Error on executing ML job: {e}"
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_code(error_message)
            logging.error(error_message)
            return ml_system_pb2.JobExecutionOutput()


def run_grpc_server(address, port):

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         maximum_concurrent_rpcs=50)
    ml_system_pb2_grpc.add_MlSystemServicer_to_server(MlSystemServicer(), server)
    server.add_insecure_port(f'{address}:{port}')
    server.start()
    logging.info(f"GRPC Server is up and running on port {port}")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    run_grpc_server(address=address, port=port)