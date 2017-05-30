# -*- coding: utf-8 -*-
import socket

'''
bind() - инициализирует ip-адрес и порт. Проверяется, не занят ли порт другой программой.
listen() – устанавливает количество клиентских соединений, которые будет обслуживать операционная система.
accept() – блокирует приложение до тех пор, пока не придет сообщение от клиента.
recv() – читает данные из сокета. Аргумент устанавливает максимальное количество байтов в сообщении.
send() – отсылает данные клиенту.
close() – закрывает сокет.
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.bind((host, port))
s.listen(2)
board = []
start = True
conn1, addr1 = s.accept()
conn2, addr2 = s.accept()
board = [[96.0, 32.0], [416.0, 32.0], [96.0, 96.0], [416.0, 96.0], [96.0, 160.0], [416.0, 160.0], [96.0, 224.0],
         [416.0, 224.0], [96.0, 288.0], [416.0, 288.0], [96.0, 352.0], [416.0, 352.0], [96.0, 416.0], [416.0, 416.0],
         [96.0, 480.0], [416.0, 480.0], [32.0, 32.0], [32.0, 480.0], [480.0, 32.0], [480.0, 480.0], [32.0, 96.0],
         [32.0, 416.0], [480.0, 96.0], [480.0, 416.0], [32.0, 160.0], [32.0, 352.0], [480.0, 160.0], [480.0, 352.0],
         [32.0, 224.0], [32.0, 288.0], [480.0, 224.0], [480.0, 288.0]]

while True:
    step1 = 0
    step2 = 0


    # 1 client

    data1 = conn1.recv(10000)
    print 'received', len(data1), 'bytes'
    dataa1 = data1.split(' ')
    for i in range(0, len(dataa1), 1):
        dataa1[i] = dataa1[i].split(',')
    del dataa1[len(dataa1) - 1]

    for i in range(0, len(dataa1), 1):
        for j in range(0, len(dataa1[i]), 1):
            dataa1[i][j] = float(dataa1[i][j])
    changes = []
    for i in range(0, len(board), 1):
        if board[i] != dataa1[i]:
            board[i] = dataa1[i]
            changes.append(i)

    full3 = ''
    for i in range(0, len(board), 1):
         buf = ','.join(str(v) for v in board[i])
         buf += ' '
         full3 += buf
    if board[29] == [-100, -100]:
        full3 = '0'
        conn2.send(full3)
        conn1.send(full3)
        s.close()
        exit()
    if board[31] == [-100, -100]:
        full3 = '1'
        conn2.send(full3)
        conn1.send(full3)
        s.close()
        exit()

    print 'sent', len(full3), 'bytes'
    conn2.send(full3)

   # 2 client

    data2 = conn2.recv(10000)
    print 'received', len(data2), 'bytes'
    dataa2 = data2.split(' ')
    for i in range(0, len(dataa2), 1):
        dataa2[i] = dataa2[i].split(',')
    del dataa2[len(dataa2) - 1]

    for i in range(0, len(dataa2), 1):
        for j in range(0, len(dataa2[i]), 1):
            dataa2[i][j] = float(dataa2[i][j])

    for i in range(0, len(board), 1):
        if (board[i] != dataa2[i]) and (i not in changes):
            board[i] = dataa2[i]


    full3 = ''
    for i in range(0, len(board), 1):
        buf = ','.join(str(v) for v in board[i])
        buf += ' '
        full3 += buf

    # response

    if board[29] == [-100, -100]:
        full3 = '0'
        conn2.send(full3)
        conn1.send(full3)
        s.close()
        break
    if board[31] == [-100, -100]:
        full3 = '1'
        conn2.send(full3)
        conn1.send(full3)
        s.close()
        break
    conn1.send(full3)
    print 'sent', len(full3), 'bytes'

conn2.close()
conn1.close()
