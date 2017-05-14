# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource

from twilio import serialize
from twilio import values
from twilio.base import deserialize, serialize, values
from twilio.base.page import Page


class BindingList(ListResource):

    def __init__(self, version, service_sid):
        """
        Initialize the BindingList
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        
        :returns: BindingList
        :rtype: BindingList
        """
        super(BindingList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
        }
        self._uri = '/Services/{service_sid}/Bindings'.format(**self._solution)

    def create(self, endpoint, identity, binding_type, address, tag=values.unset,
               notification_protocol_version=values.unset):
        """
        Create a new BindingInstance
        
        :param unicode endpoint: The endpoint
        :param unicode identity: The identity
        :param binding.binding_type binding_type: The binding_type
        :param unicode address: The address
        :param unicode tag: The tag
        :param unicode notification_protocol_version: The notification_protocol_version
        
        :returns: Newly created BindingInstance
        :rtype: BindingInstance
        """
        data = values.of({
            'Endpoint': endpoint,
            'Identity': identity,
            'BindingType': binding_type,
            'Address': address,
            'Tag': tag,
            'NotificationProtocolVersion': notification_protocol_version,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return BindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def stream(self, start_date_before=values.unset, start_date=values.unset,
               start_date_after=values.unset, end_date_before=values.unset,
               end_date=values.unset, end_date_after=values.unset,
               identity=values.unset, tag=values.unset, limit=None, page_size=None):
        """
        Streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param date start_date_before: The start_date
        :param date start_date: The start_date
        :param date start_date_after: The start_date
        :param date end_date_before: The end_date
        :param date end_date: The end_date
        :param date end_date_after: The end_date
        :param unicode identity: The identity
        :param unicode tag: The tag
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            start_date_before=start_date_before,
            start_date=start_date,
            start_date_after=start_date_after,
            end_date_before=end_date_before,
            end_date=end_date,
            end_date_after=end_date_after,
            identity=identity,
            tag=tag,
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, start_date_before=values.unset, start_date=values.unset,
             start_date_after=values.unset, end_date_before=values.unset,
             end_date=values.unset, end_date_after=values.unset,
             identity=values.unset, tag=values.unset, limit=None, page_size=None):
        """
        Lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param date start_date_before: The start_date
        :param date start_date: The start_date
        :param date start_date_after: The start_date
        :param date end_date_before: The end_date
        :param date end_date: The end_date
        :param date end_date_after: The end_date
        :param unicode identity: The identity
        :param unicode tag: The tag
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            start_date_before=start_date_before,
            start_date=start_date,
            start_date_after=start_date_after,
            end_date_before=end_date_before,
            end_date=end_date,
            end_date_after=end_date_after,
            identity=identity,
            tag=tag,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, start_date_before=values.unset, start_date=values.unset,
             start_date_after=values.unset, end_date_before=values.unset,
             end_date=values.unset, end_date_after=values.unset,
             identity=values.unset, tag=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BindingInstance records from the API.
        Request is executed immediately
        
        :param date start_date_before: The start_date
        :param date start_date: The start_date
        :param date start_date_after: The start_date
        :param date end_date_before: The end_date
        :param date end_date: The end_date
        :param date end_date_after: The end_date
        :param unicode identity: The identity
        :param unicode tag: The tag
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of BindingInstance
        :rtype: Page
        """
        params = values.of({
            'StartDate<': serialize.iso8601_date(start_date_before),
            'StartDate': serialize.iso8601_date(start_date),
            'StartDate>': serialize.iso8601_date(start_date_after),
            'EndDate<': serialize.iso8601_date(end_date_before),
            'EndDate': serialize.iso8601_date(end_date),
            'EndDate>': serialize.iso8601_date(end_date_after),
            'Identity': identity,
            'Tag': tag,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return BindingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a BindingContext
        
        :param sid: The sid
        
        :returns: BindingContext
        :rtype: BindingContext
        """
        return BindingContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a BindingContext
        
        :param sid: The sid
        
        :returns: BindingContext
        :rtype: BindingContext
        """
        return BindingContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notifications.V1.BindingList>'


class BindingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BindingPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        
        :returns: BindingPage
        :rtype: BindingPage
        """
        super(BindingPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BindingInstance
        
        :param dict payload: Payload response from the API
        
        :returns: BindingInstance
        :rtype: BindingInstance
        """
        return BindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notifications.V1.BindingPage>'


class BindingContext(InstanceContext):

    def __init__(self, version, service_sid, sid):
        """
        Initialize the BindingContext
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid
        
        :returns: BindingContext
        :rtype: BindingContext
        """
        super(BindingContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Bindings/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a BindingInstance
        
        :returns: Fetched BindingInstance
        :rtype: BindingInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return BindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the BindingInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notifications.V1.BindingContext {}>'.format(context)


class BindingInstance(InstanceResource):

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the BindingInstance
        
        :returns: BindingInstance
        :rtype: BindingInstance
        """
        super(BindingInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'notification_protocol_version': payload['notification_protocol_version'],
            'endpoint': payload['endpoint'],
            'identity': payload['identity'],
            'binding_type': payload['binding_type'],
            'address': payload['address'],
            'tags': payload['tags'],
            'url': payload['url'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: BindingContext for this BindingInstance
        :rtype: BindingContext
        """
        if self._context is None:
            self._context = BindingContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def notification_protocol_version(self):
        """
        :returns: The notification_protocol_version
        :rtype: unicode
        """
        return self._properties['notification_protocol_version']

    @property
    def endpoint(self):
        """
        :returns: The endpoint
        :rtype: unicode
        """
        return self._properties['endpoint']

    @property
    def identity(self):
        """
        :returns: The identity
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def binding_type(self):
        """
        :returns: The binding_type
        :rtype: unicode
        """
        return self._properties['binding_type']

    @property
    def address(self):
        """
        :returns: The address
        :rtype: unicode
        """
        return self._properties['address']

    @property
    def tags(self):
        """
        :returns: The tags
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a BindingInstance
        
        :returns: Fetched BindingInstance
        :rtype: BindingInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the BindingInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Notifications.V1.BindingInstance {}>'.format(context)
