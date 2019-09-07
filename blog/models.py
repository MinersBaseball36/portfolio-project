from django.db import models

# Create A Blog Model
# Should have title
# publication date pub_date
# body of text
# Image connected with this

# Add Blog app to settings

# Create migration

# Migrate

# Add to the admin


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %d, %Y')
