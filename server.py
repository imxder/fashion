import grpc
from concurrent import futures
import fashion_pb2
import fashion_pb2_grpc

class CustomerService(fashion_pb2_grpc.CustomerServiceServicer):
    def __init__(self):
        self.customers = []

    def CreateCustomer(self, request, context):
        customer = fashion_pb2.Customer(
            id=request.id,
            name=request.name,
            email=request.email,
            phone=request.phone,
        )
        self.customers.append(customer)
        return customer

    def ReadCustomer(self, request, context):
        for customer in self.customers:
            if customer.id == request.id:
                return customer
        context.set_details(f'Customer with id {request.id} not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return fashion_pb2.Customer()

    def UpdateCustomer(self, request, context):
        for customer in self.customers:
            if customer.id == request.id:
                customer.name = request.name
                customer.email = request.email
                customer.phone = request.phone
                return customer
        context.set_details(f'Customer with id {request.id} not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return fashion_pb2.Customer()

    def DeleteCustomer(self, request, context):
        for i, customer in enumerate(self.customers):
            if customer.id == request.id:
                del self.customers[i]
                return fashion_pb2.Empty()
        context.set_details(f'Customer with id {request.id} not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return fashion_pb2.Empty()

    def ListCustomers(self, request, context):
        for customer in self.customers:
            yield customer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fashion_pb2_grpc.add_CustomerServiceServicer_to_server(CustomerService(), server)
    server.add_insecure_port('[::]:50056')
    server.start()
    print("Servidor iniciado na porta [::]:50056")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
