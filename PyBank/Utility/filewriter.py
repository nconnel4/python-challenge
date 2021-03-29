def write_file(file_path, content_string):
    # writes a string to a file
    
    with open(file_path, 'w') as file:
        file.write(content_string)