from django.db import models
from django.shortcuts import reverse


class Poem(models.Model):
    title = models.CharField(max_length=63)
    author = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='A label for URL config',
        unique=True)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    def __str__(self):
        return '{} by {}'.format(
            self.title,
            self.author
        )

    def get_absolute_url(self):
        return reverse('poem_detail',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('poem_update',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('poem_delete',
                       kwargs={'slug': self.slug})
