class CreatePostRequest:
    def __init__(self, user_id, title, body):
        self.userId = user_id
        self.title = title
        self.body = body
