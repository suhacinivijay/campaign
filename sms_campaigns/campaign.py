class Campaign(object):
    def __init__(self, **kwargs):
        for field in ('campaign_id', 'campaign_name', 'user_id', 'type', 'phonebook_id', 'message'):
            setattr(self, field, kwargs.get(field, None))


