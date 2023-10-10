from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import (Staff,
                     JobAnnouncement,
                     BusinessPartners,
                     Programs,
                     ProgramsPhoto,
                     ProgramFiles,
                     Product,
                     ProductFiles,
                     Report,
                     ProductVideos,
                     ProductImages
                     )
from django.contrib import admin
from image_uploader_widget.admin import ImageUploaderInline
from django.contrib.auth.models import Group

admin.site.site_title = _("Martuni Women's Community Council Administration")
admin.site.index_title = _("Martuni Women's Community Council Administration")
admin.site.site_header = _('Site Administration')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng', 'position_eng', 'admin_image')
    list_display_links = ('id', 'name_eng', 'position_eng')
    search_fields = ('name_eng', 'name_arm', 'position_eng', 'position_arm')
    view_on_site = False
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

    def admin_image(self, other):
        if other.image:
            return mark_safe(f"<img src='{other.image.url} 'width='100'")
        else:
            return None


class JobAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng',)
    list_display_links = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm', 'company_name_eng', 'company_name_arm')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "description_eng", "company_name_eng", 'duration_eng',
                           'assessment_desc_eng', 'appraiser_requirements_eng', 'application_procedure_eng',
                           'about_company_eng', ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "description_arm", "company_name_arm", 'duration_arm',
                           'assessment_desc_arm', 'appraiser_requirements_arm', 'application_procedure_arm',
                           'about_company_arm', ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ['contacts', 'image', 'created', 'updated', 'active'],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]
    readonly_fields = ('created', 'updated')


class BusinessPartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng','admin_image')
    list_display_links = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm',)
    view_on_site = False
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

    def admin_image(self, other):
        if other.image:
            return mark_safe(f"<img src='{other.image.url} 'width='100'")
        else:
            return None


class PhotoInline(ImageUploaderInline):
    model = ProgramsPhoto
    add_image_text = _("add_image_text")


class FileInline(admin.TabularInline):
    model = ProgramFiles
    max_num = 10


class ProgramModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng',)
    list_display_links = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm',)
    view_on_site = False
    inlines = [PhotoInline, FileInline]
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "title_eng", "article_eng"],
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

    ]


class PhotoProductInline(ImageUploaderInline):
    model = ProductImages
    add_image_text = _("add_image_text")


class ProductFilesInline(admin.StackedInline):
    model = ProductFiles


class ProductVideosAdmin(admin.StackedInline):
    model = ProductVideos


class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ('name_eng', 'name_arm')
    list_display = ('id', 'name_eng',)
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

    ]
    inlines = [ProductFilesInline, PhotoProductInline, ProductVideosAdmin]


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm')
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
                "fields": ["image", 'report_file', ],
                "classes": ["wide", "extrapretty"],
            }

        ),

    ]


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         widgets = {
#             'password': PasswordInput(),
#         }
#
#
# class UserAdmin(admin.ModelAdmin):
#     search_fields = ('email', 'name')
#     form = UserForm
#     fieldsets = [
#
#         (
#             None,
#             {
#                 "fields": ["name", "email", "password"],
#                 "classes": ["wide", "extrapretty"],
#             },
#         ),
#
#     ]


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Programs, ProgramModelAdmin)
admin.site.register(JobAnnouncement, JobAnnouncementAdmin)
admin.site.register(BusinessPartners, BusinessPartnersAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.unregister(Group)
# admin.site.register(User, UserAdmin)
