with open("ips.txt", "r") as infile, open("result.txt", "w") as outfile:
    for line in infile:
        ip = line.strip()
        if ip == "":
            continue
        parts = ip.split(".")
        if len(parts) != 4:
            outfile.write(f"⚠️ Skipping invalid IP: {ip}")
            continue

        oct1 = int(parts[0])
        oct2 = int(parts[1])

        if oct1 == 10:
            outfile.write(f"{ip} -> Private (Class A)\n")
        elif oct1 == 172 and (16 <= oct2 <= 31):
            outfile.write(f"{ip} -> Private (Class B)\n")
        elif oct1 == 192 and oct2 == 168:
            outfile.write(f"{ip} -> Private (Class C)\n")
        else:
            outfile.write(f"{ip} -> Public\n")


    print("Analysis complete. Results saved to result.txt")
