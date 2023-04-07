
import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port= bluetooth.PORT_ANY
server_sock.bind(('AC:82:47:4D:A7:BE',3))
server_sock.listen(1)

print ("listening on port %d" % port)



client_sock,address = server_sock.accept()
print ("Accepted connection from ",address)

data = client_sock.recv(1024)
print ("received [%s]" % data)

client_sock.close()
server_sock.close()