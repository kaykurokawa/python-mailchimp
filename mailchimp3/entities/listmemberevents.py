# coding=utf-8
"""
The List Member Events API endpoint

Documentation: https://mailchimp.com/developer/reference/lists/list-members/list-member-events/
Schema: https://api.mailchimp.com/schema/3.0/Lists/Members/Goals/Collection.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi
from mailchimp3.helpers import check_subscriber_hash


class ListMemberEvents(BaseApi):
    """
    Get information about recent goal events for a specific list member.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListMemberEvents, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.subscriber_hash = None

    def create(self, list_id, subscriber_hash, data):
        subscriber_hash = check_subscriber_hash(subscriber_hash)
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        response = self._mc_client._post(url=self._build_path(list_id, 'members', subscriber_hash, 'events'), data=data)
        if response is not None:
            self.note_id = response['id']
        else:
            self.note_id = None
        return response


