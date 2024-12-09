# How the Code Works:
# The search_logs function opens the app.log file in read mode.
# It iterates over each line in the file.
# For each line, it checks if the specified keyword (in this case, "ERROR") is present.
# If the keyword is found, the line is printed after stripping any leading or trailing whitespace with .strip().


def search_logs(file_path, keyword):
    with open(file_path, "r") as file:
        for line in file:
            if keyword in line:
                print(line.strip())
            
            
search_logs("app.log", "ERROR")
    

