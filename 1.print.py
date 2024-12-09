server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000


print(f"Server Name: {server_name}")
print(f"Server port: {port}")
print(f"Server is_https_enabled: {is_https_enabled}")
print(f"Server max_connections: {max_connections}")

print("-----------------------------------------------------------------------")
# Update configuration values
port = 443
is_https_enabled = False

print(f"Updated Server port: {port}")
print(f"Updated Server is_https_enabled: {is_https_enabled}")