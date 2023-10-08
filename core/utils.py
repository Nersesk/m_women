from django.db.models import QuerySet

from core.models import JobAnnouncement, Staff, BusinessPartners
from typing import Dict, Union, Optional


def get_job_announcement_queryset() -> QuerySet[JobAnnouncement]:
    queryset = JobAnnouncement.objects.order_by('-id')
    return queryset


def get_dict_for_job_announcement_list(job_announcement: JobAnnouncement, lang: str) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name, description = job_announcement.name_arm, job_announcement.description_arm
    else:
        name, description = job_announcement.name_eng, job_announcement.description_eng

    return {
        'id': job_announcement.id,
        'name': name,
        'description': description,
        'image': job_announcement.image.url
    }


def get_staff_members_queryset() -> QuerySet[Staff]:
    queryset = Staff.objects.order_by('-id')
    return queryset


def get_dict_for_staff_members(staff: Staff, lang: str) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name, position = staff.name_arm, staff.position_arm
    else:
        name, position = staff.name_eng, staff.position_eng

    return {
        'id': staff.id,
        'name': name,
        'position': position,
        'image': staff.image.url
    }


def get_partners_qs() -> QuerySet[BusinessPartners]:
    queryset = BusinessPartners.objects.order_by('-id')
    return queryset

def get_dict_for_partners(partner: BusinessPartners, lang: str) -> Dict[str, Union[int, str]]:
    if lang == 'arm':
        name = partner.name_arm,
    else:
        name = partner.name_eng,

    return {
        'id': partner.id,
        'name': name,
        'duration': partner.duration,
        'projects_count': partner.projects_count
        'image': partner.image.url
    }
