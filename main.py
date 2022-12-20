import os
from html_parser import HTML_file

files = [f for f in os.listdir('.') if os.path.isfile(f)] #makes a list of all files in the current directory
for f in files: 
    if ".html" not in f:
        files.remove(f)

files_dict = {str(i): f for i, f in enumerate(files)}


print("\nList of '.html' files in the current directory:")
for key, val in files_dict.items():
    print(f"\t{key}. {val}")

file_num = input("\nChoose a file(by the corresponding number): ")

file_content = HTML_file(files_dict[file_num])
print("\n\nOpened file:", files_dict[file_num])
file_content.extract_content()
print("\n\n=======================================")
print("Extracted list of html elements:\n")
print(file_content.file_content)
print("\n\n=======================================")
file_content.parse_html()
print("Parsed text:\n")
print(file_content.parsed_text)