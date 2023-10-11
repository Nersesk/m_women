from django.db.models import QuerySet
from django.urls import reverse

from core.models import JobAnnouncement, Staff, BusinessPartners, Programs
from typing import Dict, Union, Optional


def get_job_announcement_queryset() -> QuerySet[JobAnnouncement]:
    queryset = JobAnnouncement.objects.order_by('-id')
    return queryset


def get_job_announcement_detail_dict(job_announcement: JobAnnouncement, lang: str
                                       ) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name, description, appraiser_requirements, about_company,duration, assessment_desc  = (
            job_announcement.name_arm,
            job_announcement.description_arm,
            job_announcement.appraiser_requirements_arm,
            job_announcement.about_company_arm,
            job_announcement.duration_arm,
            job_announcement.assessment_desc_arm

        )
    else:
        name, description, appraiser_requirements, about_company, duration,assessment_desc = (
            job_announcement.name_eng,
            job_announcement.description_eng,
            job_announcement.appraiser_requirements_eng,
            job_announcement.about_company_eng,
            job_announcement.duration_eng,
            job_announcement.assessment_desc_eng
        )

    return {
        'id': job_announcement.id,
        'name': name,
        'description': description,
        'image': job_announcement.image.url,
        'appraiser_requirements':appraiser_requirements,
        'about_company':about_company,
        'duration':duration,
        'assessment_desc': assessment_desc,
        'created': job_announcement.created

    }


def get_dict_for_job_announcement_list(job_announcement: JobAnnouncement, lang: str):
    if lang == 'arm':
        name, description = (
            job_announcement.name_arm,
            job_announcement.description_arm,
        )
    else:
        name, description = (
            job_announcement.name_eng,
            job_announcement.description_eng,
        )
    url = reverse('job_announcement_detail', kwargs={'lang': lang, 'id': job_announcement.id})
    return {
        'id': job_announcement.id,
        'name': name,
        'description': description,
        'image': job_announcement.image.url,
        'url':url
    }


def get_staff_members_queryset() -> QuerySet[Staff]:
    queryset = Staff.objects.order_by('-id')
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
    queryset = BusinessPartners.objects.order_by('-id')
    return queryset


def get_dict_for_partners(
        partner: BusinessPartners, lang: str
) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name = (partner.name_arm,)
    else:
        name = (partner.name_eng,)

    return {
        'id': partner.id,
        'name': name,
        'duration': partner.duration,
        'projects_count': partner.projects_count,
        'image': partner.image.url,
    }


def get_program_qs() -> QuerySet[Programs]:
    return Programs.objects.order_by('-id')


def get_program_list_dict(program: Programs, lang: str) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        title, prologue = (
            program.title_arm,
            program.prologue_arm,
        )
    else:
        title, prologue = (
            program.title_eng,
            program.prologue_eng,
        )
    url = reverse('program_detail', kwargs={'lang': lang, 'id': program.id})

    return {
        'id': program.id,
        'title': title,
        'prologue': prologue,
        'url': url
    }


def get_program_detail_dict(program: Programs, lang: str) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        title, prologue, requirements, article = (
            program.title_arm,
            program.prologue_arm,
            program.requirements_arm,
            program.article_arm,
        )
    else:
        title, prologue, requirements, article = (
            program.title_eng,
            program.prologue_eng,
            program.requirements_eng,
            program.article_eng,
        )

    return {
        'id': program.id,
        'title': title,
        'prologue': prologue,
        'requirements': requirements,
        'article': article,
    }
