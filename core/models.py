"""
Database models
"""
import os
import unidecode
from solo.models import SingletonModel

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField


def generate_staff_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('staff/', unique_filename)


def generate_job_announcement_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('business_partners/', unique_filename)


class Staff(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (Armenian)'))
    position_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Position (English)'))
    position_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Position (Armenian)'))
    image = models.ImageField(upload_to=generate_staff_image, null=False, blank=False, verbose_name=_('Image'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff members')


def generate_business_partner_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('business_partners/', unique_filename)


def generate_banner_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('banners/', unique_filename)


def generate_open_competitions_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('open_competitions/', unique_filename)


def generate_program_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('program/', unique_filename)


def generate_report_file(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('report_file/', unique_filename)


def generate_report_image(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('report_image/', unique_filename)


def generate_program_photos(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('program_photos/', unique_filename)


def generate_product_images(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('product_images/', unique_filename)


def generate_product_files(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('product_files/', unique_filename)


def generate_open_competition_files(instance, filename):
    unique_filename = unidecode.unidecode(filename)
    return os.path.join('open_competition_files/', unique_filename)


class BusinessPartners(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Name (Armenian)'))
    image = models.ImageField(upload_to=generate_business_partner_image, null=False, blank=False,
                              verbose_name=_('Image'))
    duration = models.IntegerField(blank=False, null=False, verbose_name=_('Duration'),
                                   validators=[MinValueValidator(1)])
    projects_count = models.IntegerField(blank=False, null=False, verbose_name=_('Count of projects'),
                                         validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Business Partner')
        verbose_name_plural = _('Business Partners')


class JobAnnouncement(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Job name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('Job name (Armenian)'))
    image = models.ImageField(upload_to=generate_job_announcement_image, blank=False, null=False,
                              verbose_name=_('Image'))
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
        blank=True,
        null=True,
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


class OpenCompetition(models.Model):
    name_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title (English)'))
    name_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title (Armenian)'))
    description_eng = RichTextField(null=False, blank=False, verbose_name=_('Description (English)'))
    description_arm = RichTextField(null=False, blank=False, verbose_name=_('Description (Armenian)'))
    requirements_eng = RichTextField(null=False, blank=False,
                                     verbose_name=_('Requirements to the participant (English)'))
    requirements_arm = RichTextField(null=False, blank=False,
                                     verbose_name=_('Requirements to the participant(Armenian)'))
    article_eng = RichTextField(blank=False, null=False, verbose_name=_("Article (English)"))
    article_arm = RichTextField(blank=False, null=False, verbose_name=_("Article (Armenian)"))
    image = models.ImageField(upload_to=generate_open_competitions_image, blank=False, null=False,
                              verbose_name=_('Image'))
    created = models.DateTimeField(auto_now=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now_add=True, verbose_name=_('Updated'))
    active = models.BooleanField(default=True, verbose_name=_('Is Active?'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Open Competition')
        verbose_name_plural = _('Open Competitions')


class ProgramAbstract(models.Model):
    name_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name (Armenian)'))
    title_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title (English)'))
    title_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Title (Armenian)'))
    article_eng = RichTextField(blank=False, null=False, verbose_name=_("Article (English)"))
    article_arm = RichTextField(blank=False, null=False, verbose_name=_("Article (Armenian)"))
    image = models.ImageField(null=False, blank=False, upload_to='program/%Y/%m', verbose_name=_('Main image'))
    created = models.DateTimeField(auto_now=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now_add=True, verbose_name=_('Updated'))

    class Meta:
        abstract = True


class Program(ProgramAbstract):
    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

    def __str__(self):
        return f'{self.name_eng}'


class ArchiveProgram(ProgramAbstract):
    class Meta:
        verbose_name = _('Archive Program')
        verbose_name_plural = _('Archive Programs')

    def __str__(self):
        return f'{self.name_eng}'


class Report(models.Model):
    name_eng = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Name (Armenian)'))
    image = models.ImageField(null=False, blank=False, upload_to='report/%Y/%m', verbose_name=_('Image'))
    report_file = models.FileField(null=False, blank=False, upload_to=generate_report_file, verbose_name=_('File'))
    created = models.DateTimeField(auto_now=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now_add=True, verbose_name=_('Updated'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')


class ProgramsPhoto(models.Model):
    main_model = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_images')
    image = models.ImageField(upload_to=generate_program_photos, verbose_name=_('Image'))

    def __str__(self):
        return f"Photo {self.id}"

    class Meta:
        verbose_name = _('Programs Photo')
        verbose_name_plural = _('Programs Photos')


class ArchiveProgramPhoto(models.Model):
    main_model = models.ForeignKey(ArchiveProgram, on_delete=models.CASCADE, related_name='program_images')
    image = models.ImageField(upload_to=generate_program_photos, verbose_name=_('Image'))

    def __str__(self):
        return f"Photo {self.id}"

    class Meta:
        verbose_name = _('Programs Photo')
        verbose_name_plural = _('Programs Photos')


class OpenCompetitionFiles(models.Model):
    main_model = models.ForeignKey(OpenCompetition, on_delete=models.CASCADE, related_name='required_files')
    file = models.FileField(upload_to=generate_open_competition_files, verbose_name=_('File'))
    name_eng = models.CharField(max_length=255, null=True, blank=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, null=True, blank=False, verbose_name=_('Name (Armenian)'))

    def __str__(self):
        return f"{_('Open Competition File')} {self.id}"

    class Meta:
        verbose_name = _('Open Competition File')
        verbose_name_plural = _('Open Competition Files')


class Product(models.Model):
    name_eng = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Name (English)"))
    name_arm = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Name (Armenian)"))
    description_eng = models.TextField(null=False, blank=False, verbose_name=_("Description (English)"))
    description_arm = models.TextField(null=False, blank=False, verbose_name=_("Description (Armenian)"))
    created = models.DateTimeField(auto_now=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now_add=True, verbose_name=_('Updated'))

    def __str__(self):
        return f"{_(self.name_eng)}"

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductFiles(models.Model):
    file = models.FileField(null=False, blank=False, upload_to=generate_product_files, verbose_name=_('File'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_files')
    name_eng = models.CharField(max_length=255, blank=False, verbose_name=_('Name (English)'))
    name_arm = models.CharField(max_length=255, blank=False, verbose_name=_('Name (Armenian)'))

    class Meta:
        verbose_name = _('Product File')
        verbose_name_plural = _('Product Files')

    def __str__(self):
        return f"{self.name_eng}"


class ProductImages(models.Model):
    main_model = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to=generate_product_images, verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

    def __str__(self):
        return f"{_('Image')} {self.id}"


class ProductVideos(models.Model):
    main_model = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_videos')
    video_url = models.URLField(verbose_name=_("Video Url"))

    class Meta:
        verbose_name = _('Product Video')
        verbose_name_plural = _('Product Videos')

    def __str__(self):
        return f"{_('Video')} {self.id}"


class Banner(SingletonModel):
    def __str__(self):
        return f""

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')


class BannerImages(models.Model):
    main_model = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='banner_images')
    image = models.ImageField(upload_to=generate_banner_image, verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Banner Image')
        verbose_name_plural = _('Banner Images')

    def __str__(self):
        return f"{_('Image')} {self.id}"
