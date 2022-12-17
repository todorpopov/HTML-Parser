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

def find_parent(index, list): 
    for i in range(1, len(list)):
        closing_tag = list[index - i][:1] + "/" + list[index - i][1:]
        if contains(list[index - i], open_tags) and closing_tag in list[index:]:
            return list[index - i]
    else:
        return "none"
class HTML_file():
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
            content_dict = {}
            closing_tag = self.file_content[i][:1] + "/" + self.file_content[i][1:]

            #body/html cases
            if self.file_content[i] in ["<html>", "</html>"] or \
                self.file_content[i] in ["<head>", "</head>"] \
                or self.file_content[i] in ["<body>", "</body>"]:

                content_dict["tag"] = self.file_content[i]
                if self.file_content[i] == "<html>":
                    content_dict["parent"] = "none"
                else:
                    content_dict["parent"] = "<html>"
                self.parsed_text.append(content_dict)

            #one-liners - ordinary tags
            elif contains(self.file_content[i], open_tags) and \
                contains(self.file_content[i+1], close_tags):

                tag = self.file_content[i][0:(self.file_content[i].find(">"))+1]
                content = self.file_content[i][self.file_content[i].find(">")+1:]
                parent = find_parent(i, self.file_content)
                content_dict = {"tag": tag, "content": content, "parent": parent}
                self.parsed_text.append(content_dict)
            
            #todo: tags spanning multiple lines, other tags
            elif contains(self.file_content[i], open_tags) and \
                self.file_content[i+1] != closing_tag:

                tag = self.file_content[i]
                parent = find_parent(i, self.file_content)
                content_dict = {"tag": tag, "parent": parent}
                self.parsed_text.append(content_dict)
            
            else:
                tag = self.file_content[i]
                parent = find_parent(i, self.file_content)
                content_dict = {"tag": tag, "parent": parent}
                self.parsed_text.append(content_dict)


    #def display_html(self):