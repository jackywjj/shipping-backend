from enum import Enum


class ScheduleStatusEnum(Enum):
    SCHEDULED = '已安排'
    IN_PROGRESS = '进行中'
    COMPLETED = '已完成'


def get_schedule_status_label(status):
    for item in ScheduleStatusEnum:
        if item.name == status:
            return item.value
        return None
    return None
