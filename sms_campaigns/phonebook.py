class Contacts(object):
    def __init__(self, **kwargs):
        for field in ('phonebook_id', 'contact_name', 'contact_number'):
            setattr(self, field, kwargs.get(field, None))

