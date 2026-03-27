def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])

    if 1 <= first_octet <= 126:
        return "Class A", "255.0.0.0"
    elif 128 <= first_octet <= 191:
        return "Class B", "255.255.0.0"
    elif 192 <= first_octet <= 223:
        return "Class C", "255.255.255.0"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)", "N/A"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)", "N/A"
    else:
        return "Invalid", "N/A"


def is_private(ip):
    octets = list(map(int, ip.split('.')))

    if octets[0] == 10:
        return True
    elif octets[0] == 172 and 16 <= octets[1] <= 31:
        return True
    elif octets[0] == 192 and octets[1] == 168:
        return True
    else:
        return False


def is_usable(ip):
    octets = list(map(int, ip.split('.')))

    # 0.0.0.0
    if ip == "0.0.0.0":
        return False, "Invalid (default route)"

    # Loopback
    if octets[0] == 127:
        return False, "Loopback address"

    # Broadcast (simple check)
    if octets[3] == 255:
        return False, "Broadcast address"

    return True, "Usable"


def analyze_ip(ip):
    print("\n?? IP Analysis Result")
    print("-" * 30)

    ip_class, subnet = get_ip_class(ip)
    print(f"IP Address: {ip}")
    print(f"Class: {ip_class}")
    print(f"Default Subnet Mask: {subnet}")

    if is_private(ip):
        print("Type: Private IP")
    else:
        print("Type: Public IP")

    usable, message = is_usable(ip)
    print(f"Usability: {message}")


# Run program
ip = input("Enter an IP address: ")
analyze_ip(ip)