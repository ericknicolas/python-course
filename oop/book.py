class Book():

    def __init__(self, title, author, pages, format):
        
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format

    def num_pages(self):
        return (self.pages)

    def get_title(self):
        return(self.title)

    def __str__(self):
        return (f"{self.title} by {self.author}")
    
    def __len__(self):
        return (self.pages)
    
    def __del__(self):
        print("object is deleted")