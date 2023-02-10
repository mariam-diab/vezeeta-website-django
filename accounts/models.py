from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify


# Create your models here.
class Profile(models.Model):
    Doctor_IN={
        ("جلدية", "جلدية"),
        ("أسنان", "أسنان"),
        ("نفسي", "نفسي"),
        ("اطفال حديثي الولادة", "اطفال حديثي الولادة"),
        ("مخ وأعصاب", "مخ وأعصاب"),
        ("عظام", "عظام"),
        ("نساء وتوليد", "نساء وتوليد"),
        ("أنف وأذن  وحنجرة", "أنف وأذن  وحنجرة"),
        ("قلب و اوعيه دموية", "قلب و اوعيه دموية"),
        ("أمراض دم", "أمراض دم"),
        ("أورام", "أورام"),
    }
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(("الاسم: "), max_length=50)
    subtitle = models.CharField(("نبذة عنك"), max_length=50)
    address = models.CharField(("المحافظة"), max_length=50)
    address_details = models.CharField(("العنوان بالتفصيل"), max_length=100)
    phone_number = models.CharField(("الهاتف: "), max_length=12)
    working_hours = models.CharField(("ساعات العمل: "), max_length=50)
    waiting_time = models.DecimalField(("مدة الأنتظار بالدقيقة"), max_digits=2, decimal_places=0)
    doctor = models.CharField(("دكتور؟"),choices=Doctor_IN, max_length=50)
    specialist = models.CharField(("متخصص في: "), max_length=50)
    who_am_i = models.CharField(("من أنا: "), max_length=300)
    price = models.DecimalField(("سعر الكشف: "), max_digits=5, decimal_places=2)
    image = models.ImageField(("الصورة الشخصية: "), upload_to='profile', blank=True, null=True)
    slug = models.SlugField(("Slug"), blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return '%s' %(self.user.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
