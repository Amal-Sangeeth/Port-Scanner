import socket

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

target = input("Enter target IP or domain: ")

print(f"\nScanning target: {target}")
print("=================================")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    s.close()