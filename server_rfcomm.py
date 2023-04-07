import bluetooth
from utils.consts import SERVICE_UUID

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port= bluetooth.PORT_ANY
server_sock.bind(('',port))
server_sock.listen(1)


bluetooth.advertise_service(server_sock,'Rasble Service',SERVICE_UUID,
                            service_classes=[bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])


print ("listening on port %d" % port)


client_sock,address = server_sock.accept()
print ("Accepted connection from ",address)

data = client_sock.recv(1024)
print ("received [%s]" % data)

client_sock.close()
server_sock.close()