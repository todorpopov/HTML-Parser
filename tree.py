class Node():
    def __init__(self, tag, content):
        self.tag = tag
        self.content = content
        

# Will try using a tree to store the parsed 
# html tags, and the content inside them.
# By doing this, the dysplaying method, as well as the
# CRUD operations, will be much easier to implement.