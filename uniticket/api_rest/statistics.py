from pydantic import BaseModel

from django.utils import timezone
from uni_ticket.models import Ticket

from typing import Union


class uniTicketStatsModel(BaseModel):
    date_start : Union[timezone.datetime, None]
    date_end : Union[timezone.datetime, None]
    structure_slug : Union[str, None]
    category_slug : Union[str, None]


class uniTicketStats:

    def __init__(
        self,
        date_start:Union[timezone.datetime, None] = None,
        date_end:Union[timezone.datetime, None] = None,
        structure_slug:Union[str, None] = None,
        category_slug:Union[str, None] = None
    ):
        # args validation
        uniTicketStatsModel(
            date_start, date_end, structure_slug, category_slug
        )

        self.date_end = date_end or timezone.localtime()
        # if not date_start it will go back for 6 months by default
        self.date_start = self.date_end - timezone.timedelta(days = 365 * 6)

        self.structure_slug = structure_slug
        self.category_slug = category_slug

        self.closed: int = 0
        self.reopened: int = 0

        # unassigned tickets
        self.new: int = 0

        # assinged tickets that needs to be closed
        self.pending: int = 0

        # in minutes (time between assingment and close)
        self.avg_processing: int = 0

        # in minutes (time between open and close)
        self.avg_pre_processing: int = 0

        # how many ticket have been closed by each user:str
        self.closed_by_ops:dict = {}

        # how many ticket have been opened by each user:str
        self.open_by_user:dict = {}

        # how many messages before closing the tickets, average in minutes
        self.avg_msg_to_close: int = 0

        # primo tempo di risposta: TODO
        # Time between creating a ticket and a user’s first message.
        # Automatic responses, automatic ticket closing messages and
        # internal notes are not taken into account.
        # self.first_time_answer_avg: int = 0

        # TODO
        # self.time_answer_avg: int = 0

    def get_tickets(self):
        _q = {
            'date_start': self.date_start,
            'date_end': self.date_end
        }

        if self.structure_slug:
            _q[
                'input_module'
                '__ticket_category'
                '__organizational_structure'
                '__slug'
            ] = self.structure_slug

        if self.category_slug:
            _q[
                'input_module'
                '__ticket_category'
                '__slug'
            ] = self.category_slug

        self.tickets = Ticket.objects.select_related(
            'input_module'
        ).filter(**_q)

    def load(self):
        self.get_tickets()
