import hvac

def init_server():
    client=hvac.Client(url='http://localhost:8200')
    print(f'client authenticated:{client.is_authenticated()}')

init_server()