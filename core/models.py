"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Staff(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (Armenian)'))
    position_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Position (English)'))
    position_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Position (Armenian)'))
    image = models.ImageField(upload_to='staff/', null=False, blank=False, verbose_name=_('Image'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')


class BusinessPartners(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (Armenian)'))
    image = models.ImageField(upload_to='business_partners/', null=False, blank=False, verbose_name=_('Image'))
    duration = models.IntegerField(blank=False, null=False, verbose_name=_('Duration'))
    projects_count = models.IntegerField(blank=False, null=False, verbose_name=_('Count of projects'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Business Partner')
        verbose_name_plural = _('Business Partners')


class JobAnnouncement(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Job name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Job name (Armenian)'))
    image = models.ImageField(upload_to='Jobs/', blank=False, null=False, verbose_name=_('Image'))
    description_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Job description (English)')
    )
    description_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Job description (Armenian)')
    )
    duration_eng = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Job duration (English)')
    )

    duration_arm = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Job duration in (Armenian)')
    )
    assessment_desc_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Assessment Service Description (English)')
    )
    assessment_desc_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Assessment Service Description (Armenian)')
    )

    appraiser_requirements_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Requirements to the appraiser in (English)')
    )
    appraiser_requirements_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Requirements to the appraiser (Armenian)')
    )
    application_procedure_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Application Procedure (English)')
    )

    application_procedure_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('Application Procedure (Armenian)')
    )
    about_company_eng = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('About the company (English)')
    )
    about_company_arm = RichTextField(
        blank=False,
        null=False,
        verbose_name=_('About the company (Armenian)')
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
    title_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title (English)'))
    title_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title (Armenian)'))
    prologue_eng = RichTextField(null=False, blank=False, verbose_name=_('Prologue (English)'))
    prologue_arm = RichTextField(null=False, blank=False, verbose_name=_('Prologue (Armenian)'))
    requirements_eng = RichTextField(null=False, blank=False,
                                     verbose_name=_('Requirements to the participant (English)'))
    requirements_arm = RichTextField(null=False, blank=False,
                                     verbose_name=_('Requirements to the participant(Armenian)'))
    article_eng = RichTextField(blank=False, null=False, verbose_name=_("Article (English)"))
    article_arm = RichTextField(blank=False, null=False, verbose_name=_("Article (Armenian)"))

    def __str__(self):
        return f"{_(self.title_eng)}"

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class Report(models.Model):
    name_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name (Armenian)'))
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
    file = models.FileField(upload_to='program_files/', verbose_name=_('File'))

    def __str__(self):
        return f"Photo {self.id}"

    class Meta:
        verbose_name = _('Program File')
        verbose_name_plural = _('Program Files')


class Product(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Name (English)"))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Name (Armenian)"))
    description_eng = models.TextField(null=False, blank=False, verbose_name=_("Description (English)"))
    description_arm = models.TextField(null=False, blank=False, verbose_name=_("Description (Armenian)"))

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


class ProductImages(models.Model):
    main_model = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='program_photos/', verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')


class ProductVideos(models.Model):
    main_model = models.ForeignKey(Product, on_delete=models.CASCADE)

    video_description_eng = models.TextField(verbose_name=_('Video description (English)'))
    video_description_arm = models.TextField(verbose_name=_('Video description (Armenian)'))
    video_url = models.URLField(verbose_name=_("Video Url"))

    class Meta:
        verbose_name = _('Product Video')
        verbose_name_plural = _('Product Videos')
