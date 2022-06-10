from threading import Thread

class MessageCreationThread(Thread):

    def __init__(self, message):
        self.message = message
        Thread.__init__(self)

    def run(self):
        self.message.save()


class MessageSetSeenThread(Thread):
    def __init__(self, message):
        self.message = message
        Thread.__init__(self)

    def run(self):
        if not self.message.seen:
            self.message.seen = True
            self.message.save()

class CreateMessageThread(Thread):
    def __init__(self, message):
        self.message = message
        self.message_id = None
        Thread.__init__(self)

    def run(self):
        self.message.save()
        self.message_id = self.message.id

    def join(self):
        Thread.join(self)
        return self.message_id