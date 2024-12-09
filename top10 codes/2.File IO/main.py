# Question: Write a Python script to read a file, 
# count the number of lines, words, and characters, 
# and display the counts.


def count_file_details(file_path):
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        
        num_lines = len(lines)
        print(f"number of lines in the file is: {num_lines}")
        
        num_words = sum(len(line.split()) for line in lines)
        print(f"number of words in the file is: {num_words}")
        
        num_chars = sum(len(line) for line in lines)
        print(f"number of characters in the file is: {num_chars}")
        
        
count_file_details("sample.txt")

