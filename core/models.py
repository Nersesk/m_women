"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Staff(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name in English'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name in Armenian'))
    position_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Position in English'))
    position_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Position in Armenian'))
    image = models.ImageField(upload_to='staff/', null=False, blank=False, verbose_name=_('Image'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')


class BusinessPartners(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name in English'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name in Armenian'))
    image = models.ImageField(upload_to='business_partners/', null=False, blank=False, verbose_name=_('Image'))
    duration = models.IntegerField(blank=False, null=False, verbose_name=_('Duration'))
    projects_count = models.IntegerField(blank=False, null=False, verbose_name=_('Count of projects'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Business Partner')
        verbose_name_plural = _('Business Partners')


class JobAnnouncement(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Job name in English'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Job name in Armenian'))
    image = models.ImageField(upload_to='Jobs/', blank=False, null=False, verbose_name=_('Image'))
    description_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Job description in English')
    )
    description_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Job description in Armenian')
    )
    company_name_eng = models.CharField(max_length=255,
                                        blank=False,
                                        null=False,
                                        verbose_name=_('Company name in English')
                                        )
    company_name_arm = models.CharField(max_length=255,
                                        blank=False,
                                        null=False,
                                        verbose_name=_('Company name in Armenian')
                                        )
    duration_eng = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Job duration in English')
    )

    duration_arm = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Job duration in Armenian')
    )
    assessment_desc_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Assessment Service Description in English')
    )
    assessment_desc_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Assessment Service Description in Armenian')
    )

    appraiser_requirements_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Requirements to the appraiser in English')
    )
    appraiser_requirements_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Requirements to the appraiser in Armenian')
    )
    application_procedure_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Application Procedure in English')
    )

    application_procedure_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Application Procedure in Armenian')
    )
    about_company_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('About the company in English')
    )
    about_company_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('About the company in Armenian')
    )
    contacts = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Contacts')
    )
    created = models.DateTimeField(auto_now=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now_add=True, verbose_name=_('Updated'))
    active = models.BooleanField(default=True, verbose_name=_('Is Active?'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Job Announcement')
        verbose_name_plural = _('Job Announcements')


class Programs(models.Model):
    name_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name in English'))
    name_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name in Armenian'))
    title_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title in English'))
    title_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title in Armenian'))
    article_eng = RichTextField(blank=False, null=False, verbose_name=_("Article in English"))
    article_arm = RichTextField(blank=False, null=False, verbose_name=_("Article in Armenian"))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class Report(models.Model):
    name_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name in English'))
    name_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name in Armenian'))
    image = models.ImageField(null=False, blank=False, upload_to='report/', verbose_name=_('Image'))
    report_file = models.FileField(null=False, blank=False, upload_to='report_file/', verbose_name=_('File'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')


class ProgramsPhoto(models.Model):
    main_model = models.ForeignKey(Programs, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='program_photos/', verbose_name=_('Image'))

    def __str__(self):
        return f"Photo {self.id}"

    class Meta:
        verbose_name = _('Programs Photo')
        verbose_name_plural = _('Programs Photos')


class ProgramFiles(models.Model):
    main_model = models.ForeignKey(Programs, on_delete=models.CASCADE)
    file = models.FileField(upload_to='program_files/', verbose_name=_('Image'))

    def __str__(self):
        return f"Photo {self.id}"

    class Meta:
        verbose_name = _('Program File')
        verbose_name_plural = _('Program Files')


class Product(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Name in English"))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Name in Armenian"))
    description_eng = models.TextField(null=False, blank=False, verbose_name=_("Description in English"))
    description_arm = models.TextField(null=False, blank=False, verbose_name=_("Description in Armenian"))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductFiles(models.Model):
    file = models.FileField(null=False, blank=False, verbose_name=_('File'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Product File')
        verbose_name_plural = _('Product Files')


# user Models

class UserManager(BaseUserManager):
    """Manager for user"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return new user"""
        if not email:
            raise ValueError("User must have an email!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create, save and return new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in system"""
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()
