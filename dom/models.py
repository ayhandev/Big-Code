from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class infa(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    date = models.DateTimeField('Date and Time', auto_now_add=True)

    def __str__(self):
        return self.name


class PublishedCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code by {self.user.username} published on {self.date_published}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_code = models.ForeignKey(PublishedCode, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.published_code}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_code = models.ForeignKey(PublishedCode, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"Like by {self.user.username} on {self.published_code}"
    


class Messenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def encrypt_content(self, content, shift=11):
        encrypted_content = ''
        for char in content:
            char_code = ord(char)
            if 1040 <= char_code <= 1103: 
                new_char_code = ((char_code - 1040 + shift) % 32) + 1040
                encrypted_content += chr(new_char_code)
            elif 97 <= char_code <= 122:  
                new_char_code = ((char_code - 97 + shift) % 26) + 97
                encrypted_content += chr(new_char_code)
            else:
                encrypted_content += char
        return encrypted_content

    def decrypt_content(self, content, shift=11):
        decrypted_content = ''
        for char in content:
            char_code = ord(char)
            if 1040 <= char_code <= 1103:
                new_char_code = ((char_code - 1040 - shift) % 32) + 1040
                decrypted_content += chr(new_char_code)
            elif 97 <= char_code <= 122:
                new_char_code = ((char_code - 97 - shift) % 26) + 97
                decrypted_content += chr(new_char_code)
            else:
                decrypted_content += char
        return decrypted_content

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.content = self.encrypt_content(self.content)
        super().save(*args, **kwargs)

    def get_content(self):
        return self.decrypt_content(self.content)
@receiver(post_save, sender=Messenger)
def delete_message(sender, instance, **kwargs):
    if instance.date_sent + timezone.timedelta(hours=48) <= timezone.now():
        instance.delete()