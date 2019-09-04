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
