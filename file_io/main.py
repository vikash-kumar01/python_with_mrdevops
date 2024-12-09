# with open("/filepath/abc.txt", r) --> Read
# with open("/filepath/abc.txt", w) --> Write


def update_server_config(file_path, key, value):
        with open("server.conf", "r") as file: 
            lines = file.readlines()
            
        with open("server.conf", "w") as file: 
            for line in lines:
                if key in line:
                    file.write(key + "=" + value+ "\n")
                else:
                    file.write(line)
                    
update_server_config("server.conf", "MAX_CONNECTIONS", "1000")


#############################################################


        
        
    
    