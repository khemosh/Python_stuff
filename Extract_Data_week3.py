import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
""" note that you must include HTTP/1.0 at the end of the above
    or else the headers wont be returned """

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print data

mysock.close()
