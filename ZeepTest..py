from zeep import Client
client = Client(
    'http://lax.lax.ei:8121/jsb/web-services/JsbImportTestService?wsdl')
print(client.service.echoMessage(r'Hello JSB'))

