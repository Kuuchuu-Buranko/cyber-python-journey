ip = input("Enter IPv4 addres: ")
parts = ip.split(".")
if len(parts) != 4:
    print("Invalid IP: must have 4 octets")
else:
    oct1 = int(parts[0])
    oct2 = int(parts[1])
    if oct1 == 10:
        print(f"{ip} is a Private IP (Class A)")
    elif oct1 == 172 and (16 <= oct2 <= 31):
        print(f"{ip} is a Private Ip (Class A)")
    elif oct1 == 192 and oct2 == 168:
        print(f"{ip} is a Private IP (Class C)")
    else:
        print(f"{ip} is a Public IP")
