import sys

from html_parser import html_file

argument = sys.argv[1]

try:
    file_name = str(argument)
except:
    print("Incorrect filename!")

file_content = html_file(file_name)
file_content.extract_content()
print("=======================================")
print("Extracted list of html elements:\n")
print(file_content.file_content)
print("\n\n=======================================")
file_content.parse_html()
print("Parsed text:\n")
print(file_content.parsed_text)