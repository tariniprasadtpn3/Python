import socket

s = socket.socket()

s.bind(('localhost',9999))

s.listen(3)
print("Connecting to............")

while True:
    c,addr = s.accept()
    print("Connected to ",addr)

    c.send(bytes("Welcome",'utf-8'))

    c.close()
