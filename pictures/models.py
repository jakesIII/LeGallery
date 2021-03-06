from django.db import models

# Create your models here.
class pin (models.Model):
    pin_name = models.CharField(max_length = 30, null=True, default=0)

    def __str__(self):
        return self.pin_name

    def save_pin(self):
        self.save()

    @classmethod
    def filter_by_pin(cls):
        return cls.objects.all()

class Section(models.Model):
    section_name = models.CharField(max_length = 30, null=True, default=0)

    def __str__(self):
        return self.section_name

    def save_section(self):
        self.save()

    @classmethod
    def get_all_sections(cls):
        return cls.objects.all()

class Upload(models.Model):
    title = models.CharField(max_length = 30)
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey('pin', default=0)
    category = models.ForeignKey('Section', default=0)
    mboto = models.ImageField(upload_to='upload_storage/', blank=True)

    def __str__(self):
        return self.title

    def save_upload(self):
        self.save()

    @classmethod
    def delete_upload(cls, id):
        return cls.objects.filter(id = id).delete()

    @classmethod
    def get_all_upload(cls):
        return cls.objects.all()

    @classmethod
    def locate_image(cls, search_term):
        return cls.objects.filter(category__section_name__icontains=search_term)
