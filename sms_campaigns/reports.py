
class SMSReports(object):
    def __init__(self, **kwargs):
        for field in ('campaign_id', 'contact_number', 'status', 'message_uuid'):
            setattr(self, field, kwargs.get(field, None))