from django.db.models import QuerySet
from django.urls import reverse
from core.models import JobAnnouncement, Staff, BusinessPartners, Program, OpenCompetition, ArchiveProgram, Product, \
    Report
from typing import Dict, Union, Iterator
from itertools import chain


def get_announcements_qs() -> list:
    combined_queryset = list(chain(OpenCompetition.objects.filter(is_active=True).order_by('-created'),
                                   JobAnnouncement.objects.filter(active=True).order_by('-created')))
    combined_queryset.sort(key=lambda x: x.created, reverse=True)

    return combined_queryset


def get_job_announcement_qs() -> QuerySet[JobAnnouncement]:
    return JobAnnouncement.objects.order_by('-created')


def get_open_competition_detail_dict(open_competition: OpenCompetition, lang: str
                                     ) -> Dict[str, Union[int, str, list[dict[str, str]]]]:
    required_files = []
    if lang == 'arm':
        title, description, requirements, article = (
            open_competition.name_arm,
            open_competition.description_arm,
            open_competition.requirements_arm,
            open_competition.article_arm
        )
    else:
        title, description, requirements, article = (
            open_competition.name_eng,
            open_competition.description_eng,
            open_competition.requirements_eng,
            open_competition.article_eng
        )
    for file in open_competition.required_files.order_by('id'):
        file_dict = {
            'name': file.name_arm if lang == 'arm' else open_competition.name_eng,
            'url': file.file.url
        }
        required_files.append(file_dict)
    return {
        'id': open_competition.id,
        'title': title,
        'description': description,
        'requirements': requirements,
        'article': article,
        'image': open_competition.image.url,
        'required_files': required_files
    }


def get_open_competition_qs() -> QuerySet[OpenCompetition]:
    return OpenCompetition.objects.order_by('-created')


def get_job_announcement_detail_dict(job_announcement: JobAnnouncement, lang: str
                                     ) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name, description, appraiser_requirements, about_company, duration, assessment_desc, application_procedure = (
            job_announcement.name_arm,
            job_announcement.description_arm,
            job_announcement.appraiser_requirements_arm,
            job_announcement.about_company_arm,
            job_announcement.duration_arm,
            job_announcement.assessment_desc_arm,
            job_announcement.application_procedure_arm

        )
    else:
        name, description, appraiser_requirements, about_company, duration, assessment_desc, application_procedure = (
            job_announcement.name_eng,
            job_announcement.description_eng,
            job_announcement.appraiser_requirements_eng,
            job_announcement.about_company_eng,
            job_announcement.duration_eng,
            job_announcement.assessment_desc_eng,
            job_announcement.application_procedure_eng
        )

    return {
        'id': job_announcement.id,
        'name': name,
        'description': description,
        'image': job_announcement.image.url,
        'appraiser_requirements': appraiser_requirements,
        'about_company': about_company,
        'duration': duration,
        'assessment_desc': assessment_desc,
        'created': job_announcement.created.strftime('%d/%m/%Y, %H:%M:%S'),
        'application_procedure': application_procedure
    }


def get_dict_for_announcement_list(announcement: Union[JobAnnouncement, OpenCompetition], lang: str):
    if lang == 'arm':
        name, description = (
            announcement.name_arm,
            announcement.description_arm,
        )
    else:
        name, description = (
            announcement.name_eng,
            announcement.description_eng,
        )
    if isinstance(announcement, JobAnnouncement):
        url = reverse('job_announcement_detail', kwargs={'lang': lang, 'id': announcement.id})
    else:
        url = reverse('open_competition_detail', kwargs={'lang': lang, 'id': announcement.id})
    return {
        'id': announcement.id,
        'name': name,
        'description': description,
        'image': announcement.image.url,
        'url': url
    }


def get_staff_members_queryset() -> QuerySet[Staff]:
    queryset = Staff.objects.order_by('id')
    return queryset


def get_dict_for_staff_members(
        staff: Staff, lang: str
) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name, position = staff.name_arm, staff.position_arm
    else:
        name, position = staff.name_eng, staff.position_eng

    return {
        'id': staff.id,
        'name': name,
        'position': position,
        'image': staff.image.url,
    }


def get_partners_qs() -> QuerySet[BusinessPartners]:
    queryset = BusinessPartners.objects.order_by('id')
    return queryset


def get_dict_for_partners(
        partner: BusinessPartners, lang: str
) -> Dict[str, Union[int, str]]:

    name = partner.name_arm if lang == 'arm' else partner.name_eng
    return {
        'id': partner.id,
        'name': name,
        'duration': partner.duration,
        'projects_count': partner.projects_count,
        'image': partner.image.url,
    }


def get_program_qs() -> QuerySet[Program]:
    return Program.objects.order_by('-id')


def get_program_list_dict(program: Program, lang: str, url_arg) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        title, article, name = (
            program.title_arm,
            program.article_arm,
            program.name_arm
        )
    else:
        title, article, name = (
            program.title_eng,
            program.article_eng,
            program.name_eng
        )
    url = reverse(url_arg, kwargs={'lang': lang, 'id': program.id})

    return {
        'id': program.id,
        'name': name,
        'image': program.image.url,
        'title': title,
        'article': article,
        'url': url
    }


def get_program_detail_dict(program: Program, lang: str) -> Dict[str, Union[int, str, list]]:
    program_images = []
    for image in program.program_images.order_by('id'):
        program_images.append({'url': image.image.url})
    if lang == 'arm':
        title, article, name = (
            program.name_arm,
            program.title_arm,
            program.article_arm,

        )
    else:
        title, article, name = (
            program.name_eng,
            program.title_eng,
            program.article_eng,
        )

    return {
        'id': program.id,
        'name': name,
        'title': title,
        'created': program.created.strftime('%d/%m/%Y, %H:%M:%S'),
        'main_image': program.image.url,
        'article': article,
        'program_images': program_images
    }


def get_archive_programs_qs() -> QuerySet[ArchiveProgram]:
    return ArchiveProgram.objects.order_by('-created')


def get_product_qs() -> QuerySet[Product]:
    return Product.objects.order_by('-created')


def get_product_dict(product: Product, lang: str) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name, description = product.name_arm, product.description_arm
    else:
        name, description = product.name_eng, product.description_eng

    url = reverse('product_detail', kwargs={'lang': lang, 'id': product.id})
    return {
        'name': name,
        'description': description,
        'url': url
    }


def get_product_detail_dict(product: Product, lang: str) -> Dict[str, Union[int, str, list]]:
    product_files = []
    product_videos = []
    product_images = []
    if lang == 'arm':
        name, description = product.name_arm, product.description_arm
    else:
        name, description = product.name_eng, product.description_eng
    for file in product.product_files.order_by('id'):
        file_dict = {
            'name': file.name_arm if lang == 'arm' else file.name_eng,
            'url': file.file.url
        }
        product_files.append(file_dict)
    for image in product.product_images.order_by('id'):
        image = {'url': image.image.url}
        product_images.append(image)
    for product_video in product.product_videos.order_by('id'):
        video_dict = {
            'description': product_video.video_description_arm if lang == 'arm' else product_video.video_description_eng,
            'url': product_video.video_url,
        }
        product_videos.append(video_dict)

    return {
        'id': product.id,
        'name': name,
        'description': description,
        'files': product_files,
        'images': product_images,
        'videos': product_videos,
        'created': product.created.strftime('%d/%m/%Y, %H:%M:%S'),

    }


def get_report_qs() -> QuerySet[Report]:
    return Report.objects.order_by('-created')


def get_report_dict(report: Report, lang: str) -> Dict[str, Union[int, str]]:
    name = report.name_arm if lang == 'arm' else report.name_eng
    return {
        'name': name,
        'file': report.report_file.url,
        'image': report.image.url
    }