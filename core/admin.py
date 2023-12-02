from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import (Staff,
                     JobAnnouncement,
                     BusinessPartners,
                     Program,
                     ProgramsPhoto,
                     OpenCompetitionFiles,
                     OpenCompetition,
                     Product,
                     ProductFiles,
                     Report,
                     ProductVideos,
                     ProductImages,
                     ArchiveProgram,
                     Banner, BannerImages
                     )
from django.contrib import admin
from django.contrib.auth.models import Group, User

from image_uploader_widget.admin import ImageUploaderInline
from solo.admin import SingletonModelAdmin

admin.site.site_title = _("Martuni Women's Community Council Administration")
admin.site.index_title = _("Martuni Women's Community Council Administration")
admin.site.site_header = _('Site Administration')


def custom_list_display(instance, request):
    lang = request.LANGUAGE_CODE
    list_display = ['id', ]
    if lang == 'en':
        list_display.append('name_eng')
    elif lang == 'hy':
        list_display.append('name_arm')

    list_display.append('admin_image')
    return list_display


def custom_list_display_links(instance, request, list_display):
    lang = request.LANGUAGE_CODE
    list_display_links = ['id']
    if lang == 'en':
        list_display_links.append('name_eng')
        list_display_links.append('position_eng')
    elif lang == 'hy':
        list_display_links.append('name_arm')
        list_display_links.append('position_arm')
    list_display_links.append('admin_image')

    return list_display_links


def admin_image(instance, other):
    if other.image:
        return mark_safe(f"<img src='{other.image.url} 'width='100'")
    else:
        return None


class StaffAdmin(admin.ModelAdmin):
    search_fields = ('name_eng', 'name_arm', 'position_eng', 'position_arm')
    view_on_site = False

    admin_image = admin_image
    admin_image.short_description = _('Image')

    def get_list_display(self, request):
        lang = request.LANGUAGE_CODE  # Adjust this based on how you store the language
        list_display = ['id', ]
        if lang == 'en':
            list_display.append('name_eng')
            list_display.append('position_eng')
        elif lang == 'hy':
            list_display.append('name_arm')
            list_display.append('position_arm')

        list_display.append('admin_image')
        return list_display

    def get_list_display_links(self, request, list_display):
        lang = request.LANGUAGE_CODE
        list_display_links = ['id']
        if lang == 'en':
            list_display_links.append('name_eng')
            list_display_links.append('position_eng')
        elif lang == 'hy':
            list_display_links.append('name_arm')
            list_display_links.append('position_arm')
        list_display_links.append('admin_image')

        return list_display_links

    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "position_eng", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "position_arm"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", ],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]


class JobAnnouncementAdmin(admin.ModelAdmin):
    search_fields = ('name_eng', 'name_arm',)

    get_list_display = custom_list_display
    get_list_display_links = custom_list_display_links

    admin_image = admin_image
    admin_image.short_description = _('Image')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "description_eng", 'duration_eng',
                           'assessment_desc_eng', 'appraiser_requirements_eng', 'application_procedure_eng',
                           'about_company_eng', ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "description_arm", 'duration_arm',
                           'assessment_desc_arm', 'appraiser_requirements_arm', 'application_procedure_arm',
                           'about_company_arm', ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ['image', 'created', 'updated', 'active'],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]
    readonly_fields = ('created', 'updated')


class BusinessPartnersAdmin(admin.ModelAdmin):
    search_fields = ('name_eng', 'name_arm',)
    view_on_site = False

    get_list_display = custom_list_display
    get_list_display_links = custom_list_display_links

    admin_image = admin_image
    admin_image.short_description = _('Image')

    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", 'duration', 'projects_count'],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]


class PhotoInline(ImageUploaderInline):
    model = ProgramsPhoto
    add_image_text = _("add_image_text")


class FileInline(admin.TabularInline):
    model = OpenCompetitionFiles
    max_num = 10


class ProgramModelAdmin(admin.ModelAdmin):
    get_list_display = custom_list_display
    get_list_display_links = custom_list_display_links

    admin_image = admin_image
    admin_image.short_description = _('Image')
    search_fields = ('title_eng', 'title_arm', 'name_eng', 'name_arm')
    view_on_site = True
    inlines = [PhotoInline]
    readonly_fields = ('created', 'updated')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["title_eng", "name_eng", "article_eng"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "title_arm", "article_arm"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", 'created', 'updated'],
                "classes": ["wide", "extrapretty"],
            }

        ),

    ]


class OpenCompetitionAdmin(admin.ModelAdmin):
    get_list_display = custom_list_display
    get_list_display_links = custom_list_display_links

    admin_image = admin_image
    admin_image.short_description = _('Image')
    search_fields = ('name_eng', 'name_arm',)
    view_on_site = False
    inlines = [FileInline]
    readonly_fields = ('created', 'updated')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "description_eng", "requirements_eng", "article_eng"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "description_arm", "requirements_arm", "article_arm"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", 'created', 'updated', 'active'],
                "classes": ["wide", "extrapretty"],
            }

        ),

    ]


class PhotoProductInline(ImageUploaderInline):
    model = ProductImages
    add_image_text = _("add_image_text")


class ProductFilesInline(admin.StackedInline):
    model = ProductFiles


class ProductVideosAdmin(admin.StackedInline):
    model = ProductVideos


class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_list_display(self, request):
        lang = request.LANGUAGE_CODE
        list_display = ['id', ]
        if lang == 'en':
            list_display.append('name_eng')
        elif lang == 'hy':
            list_display.append('name_arm')
        return list_display

    def get_list_display_links(self, request, list_display):
        lang = request.LANGUAGE_CODE
        list_display_links = ['id']
        if lang == 'en':
            list_display_links.append('name_eng')
        elif lang == 'hy':
            list_display_links.append('name_arm')
        return list_display_links

    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "description_eng"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "description_arm"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["created", 'updated', ],
                "classes": ["wide", "extrapretty"],
            }

        ),

    ]
    inlines = [ProductFilesInline, PhotoProductInline, ProductVideosAdmin]


class ReportAdmin(admin.ModelAdmin):
    search_fields = ('name_eng', 'name_arm')
    readonly_fields = ('created', 'updated')
    get_list_display = custom_list_display
    get_list_display_links = custom_list_display_links

    admin_image = admin_image
    admin_image.short_description = _('Image')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", 'report_file', 'created', 'updated'],
                "classes": ["wide", "extrapretty"],
            }

        ),

    ]


class ArchiveProgramAdmin(ProgramModelAdmin):
    """Archive Programs"""


class CustomInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


class BannerImagesInline(ImageUploaderInline):
    model = BannerImages
    add_image_text = _("add_image_text")
    max_num = 3
    formset = CustomInlineFormSet

    def has_delete_permission(self, request, obj=None):
        return False

class BannerAdmin(SingletonModelAdmin):
    inlines = [BannerImagesInline, ]


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Program, ProgramModelAdmin)
admin.site.register(OpenCompetition, OpenCompetitionAdmin)
admin.site.register(JobAnnouncement, JobAnnouncementAdmin)
admin.site.register(BusinessPartners, BusinessPartnersAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(ArchiveProgram, ArchiveProgramAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
