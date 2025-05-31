# import re
# import ipaddress

# test = input("Enter the file path: ")
# reg = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# t = []

# try:
    
#     with open(test, 'r') as fh:
#         for line in fh:
#             match = reg.findall(line)
#             for ip in match:
#                 try:
#                     ipaddress.IPv4Address(ip)
#                     if ip not in t:
#                         t.append(ip)
#                 except ValueError:
#                     continue  
# except Exception as e:
#     print(f"Error {e}")                
# print(t)
import ipaddress

# Get file path
try:
    file_path = input("Enter the file path: ")
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
    exit(1)

# Lists to store valid IPs
valid_ipv4 = []
valid_ipv6 = []

# Read file and process each word
try:
    with open(file_path, 'r') as fh:
        for line in fh:
            # Split the line into words (using whitespace as delimiter)
            words = line.split()
            for word in words:
                # Clean up common surrounding characters (e.g., commas, brackets)
                word = word.strip('[],()":;')
                try:
                    # Try to parse the word as an IP address
                    ip_obj = ipaddress.ip_address(word)
                    if ip_obj.version == 4 and word not in valid_ipv4:
                        valid_ipv4.append(word)
                    elif ip_obj.version == 6 and word not in valid_ipv6:
                        valid_ipv6.append(word)
                except ValueError:
                    continue
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit(1)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Print results
if valid_ipv4 or valid_ipv6:
    print("Valid IPv4 addresses:")
    print("\n".join(valid_ipv4) if valid_ipv4 else "None")
    print("\nValid IPv6 addresses:")
    print("\n".join(valid_ipv6) if valid_ipv6 else "None")
else:
    print("No valid IP addresses found.")