from django.db import models


class Search(models.Model):
    result = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result + ' - ' + self.date.__str__()
