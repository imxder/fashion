import grpc
import fashion_pb2
import fashion_pb2_grpc

def list_customers(stub):
    print("Listando clientes:")
    response = stub.ListCustomers(fashion_pb2.Empty())
    for customer in response:
        print(customer)

def create_customer(stub, id, name, email, phone):
    print(f"Criando cliente {id}: {name}")
    customer = fashion_pb2.Customer(
        id=id,
        name=name,
        email=email,
        phone=phone,
    )
    response = stub.CreateCustomer(customer)
    print(f"Cliente criado com sucesso: {response}")

def read_customer(stub, id):
    print(f"Lendo cliente {id}")
    response = stub.ReadCustomer(fashion_pb2.CustomerId(id=id))
    print(response)

def update_customer(stub, id, name, email, phone):
    print(f"Atualizando cliente {id}: {name}")
    customer = fashion_pb2.Customer(
        id=id,
        name=name,
        email=email,
        phone=phone,
    )
    response = stub.UpdateCustomer(customer)
    print(f"Cliente atualizado com sucesso: {response}")

def delete_customer(stub):
    while True:
        id = input("Digite o ID do cliente que deseja excluir (ou 'exit' para sair): ")
        if id == 'exit':
            break
        try:
            id = int(id)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
        response = stub.DeleteCustomer(fashion_pb2.CustomerId(id=id))
        print(f"Cliente excluído com sucesso: {response}")

def add_customers(stub):
    while True:
        id = input("Digite o ID do cliente (ou 'exit' para sair): ")
        if id == 'exit':
            break
        name = input("Digite o nome do cliente: ")
        email = input("Digite o email do cliente: ")
        phone = input("Digite o telefone do cliente: ")
        create_customer(stub, int(id), name, email, phone)

def run():
    channel = grpc.insecure_channel('localhost:50056')
    stub = fashion_pb2_grpc.CustomerServiceStub(channel)

    list_customers(stub)
    add_customers(stub)
    list_customers(stub)
    delete_customer(stub)

if __name__ == '__main__':
    run()
