class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'new': 'new'
        }
