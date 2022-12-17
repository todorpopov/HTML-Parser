open_tags = ["<html>", "<body>", "<p>", "<div>", 
        "<table>", "<tr>", "<td>"]

close_tags = ["</html>", "</body>", "</p>", "</div>", "</table>", 
        "</tr>", "</td>"]

def contains(text, list_of_substr): 
    #checks if the given text contains any of the 
    #substrings in the given list of substrings
    for i in list_of_substr:
        if i in text:
            return True
    return False

# def find_parent(index, list): 


class html_file():
    def __init__(self, filename):
        self.filename = filename

    def extract_content(self):
        self.file_content = []
        with open(self.filename, 'r') as f:
            temp = f.read().split("<")
            for i in temp:
                if i != "":
                    i = "<" + i
                    self.file_content.append(i.replace("\t", "").strip())

    def parse_html(self):
        self.parsed_text = []
        for i in range(len(self.file_content)):

            #body/html cases
            if self.file_content[i] == "<html>" or self.file_content[i] == \
                "<head>" or self.file_content[i] == "<body>":
                current_case = {}
                current_case["type"] = self.file_content[i].strip("<>")
                if self.file_content[i] == "<html>":
                    current_case["parent"] = "none"
                else:
                    current_case["parent"] = "<html>"
                self.parsed_text.append(current_case)

            #one-liner, ordinary, tags
            if contains(self.file_content[i], open_tags) and \
                contains(self.file_content[i+1], close_tags):
                tag = self.file_content[i][0:(self.file_content[i].find(">"))+1]
                content = self.file_content[i][self.file_content[i].find(">")+1:]
                type = "nested"
                content_dict = {}
                content_dict = {"tag": tag, "content": content, "type": type}
                self.parsed_text.append(content_dict)
            
            

    def display_html(self):
        indentation_level = 0