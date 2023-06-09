from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"s" if len(self.posts) != 1 else ""})'

    def create_post(self, title, content):
        self.posts.append(Post(title, content, self.author))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [p.json() for p in self.posts],
        }