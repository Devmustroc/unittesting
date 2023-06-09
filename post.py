class Post:
    def __init__(self, title, content, author, new):
        self.title = title
        self.content = content
        self.author = author
        self.new = 'new'

    def __repr__(self):
        return f'{self.title}, {self.author}, {self.content}'

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'new': 'new'
        }
