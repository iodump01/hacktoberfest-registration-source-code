
from django.urls import reverse
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class QrCode(models.Model):
    text = models.CharField(max_length=500, default=None)
    ticketId = models.CharField(max_length=10,
                                blank=True,
                                editable=False,
                                unique=True,)
    image = models.ImageField(
        upload_to='./qrcode', blank=True)

    def __str__(self):
        return self.ticketId

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.text)
        qr_offset = Image.new('RGB', (400, 400), 'white')
        qr_offset.paste(qr_image)
        file_name = f'{self.ticketId}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.image.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)


class Ticket(models.Model):
    ticketId = models.CharField(
        max_length=10,
        blank=True,
        editable=False,
        unique=True,
    )

    Name = models.CharField(max_length=300)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=300, unique=True)
    College = models.CharField(max_length=300, blank=True, null=True)
    Department = models.CharField(max_length=300, blank=True, null=True)
    Semester = models.CharField(max_length=300, blank=True, null=True)
    Address = models.CharField(max_length=300, blank=True, null=True)
    Promo = models.CharField(max_length=300, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.ticketId])

    class Meta:
        ordering = ['-created_on']

        def __unicode__(self):
            return "{0} {1} {2} {3} {4}".format(
                self, self.ticketId, self.Name, self.created_on)


class Message(models.Model):
    Name = models.CharField(max_length=300)
    Email = models.EmailField(max_length=300, unique=True)
    Subject = models.CharField(max_length=300)
    Message = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.Subject

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.Subject])

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return "{0} {1} {2} {3} {4}".format(
                self, self.Name, self.created_on)
