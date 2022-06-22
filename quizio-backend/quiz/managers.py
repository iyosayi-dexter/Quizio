from django.db.models import Manager
import random

class QuestionsManager(Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_random(self, mode, course, nques):
        filtered = self.get_queryset().filter(mode=mode, course__title=course)

        if nques > len(filtered):
            return filtered

        random = random.sample(list(filtered), nques)

        return random

    def mark(self, users_answers, mode, course):
        filtered = self.get_queryset().filter(mode=mode, course__title=course)
        result = []
        return result