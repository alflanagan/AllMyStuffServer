from django.db import models

# Create your models here.
class TextNote(models.Model):
    title = models.CharField(max_length=80, help_text='This is a short descriptive title for the note.')
    text = models.TextField(help_text='This is the contents of the note', blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', models.PROTECT, null=True)
    class Meta:
        indexes = [
            models.Index(fields=['category'])
        ]
        unique_together = ('title', 'createdOn')

    def __str__(self):
        return "Text Note: {}".format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=60, help_text='A short keyword for classifying things.', unique=True, null=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True)
    class Meta:
        indexes = [
            models.Index(fields=['parent'])
        ]

    def __str__(self):
        return self.name

