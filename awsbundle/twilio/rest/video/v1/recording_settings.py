# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class RecordingSettingsList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the RecordingSettingsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsList
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsList
        """
        super(RecordingSettingsList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a RecordingSettingsContext

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        """
        return RecordingSettingsContext(self._version, )

    def __call__(self):
        """
        Constructs a RecordingSettingsContext

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        """
        return RecordingSettingsContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RecordingSettingsList>'


class RecordingSettingsPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the RecordingSettingsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsPage
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsPage
        """
        super(RecordingSettingsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RecordingSettingsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        """
        return RecordingSettingsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RecordingSettingsPage>'


class RecordingSettingsContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the RecordingSettingsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        """
        super(RecordingSettingsContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/RecordingSettings/Default'.format(**self._solution)

    def fetch(self):
        """
        Fetch a RecordingSettingsInstance

        :returns: Fetched RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return RecordingSettingsInstance(self._version, payload, )

    def create(self, friendly_name, aws_credentials_sid=values.unset,
               encryption_key_sid=values.unset, aws_s3_url=values.unset,
               aws_storage_enabled=values.unset, encryption_enabled=values.unset):
        """
        Create a new RecordingSettingsInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode aws_credentials_sid: The SID of the stored Credential resource
        :param unicode encryption_key_sid: The SID of the Public Key resource to use for encryption
        :param unicode aws_s3_url: The URL of the AWS S3 bucket where the recordings should be stored
        :param bool aws_storage_enabled: Whether all recordings should be written to the aws_s3_url
        :param bool encryption_enabled: Whether all recordings should be stored in an encrypted form

        :returns: Newly created RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'AwsCredentialsSid': aws_credentials_sid,
            'EncryptionKeySid': encryption_key_sid,
            'AwsS3Url': aws_s3_url,
            'AwsStorageEnabled': aws_storage_enabled,
            'EncryptionEnabled': encryption_enabled,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return RecordingSettingsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RecordingSettingsContext {}>'.format(context)


class RecordingSettingsInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the RecordingSettingsInstance

        :returns: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        """
        super(RecordingSettingsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'aws_credentials_sid': payload['aws_credentials_sid'],
            'aws_s3_url': payload['aws_s3_url'],
            'aws_storage_enabled': payload['aws_storage_enabled'],
            'encryption_key_sid': payload['encryption_key_sid'],
            'encryption_enabled': payload['encryption_enabled'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RecordingSettingsContext for this RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsContext
        """
        if self._context is None:
            self._context = RecordingSettingsContext(self._version, )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def aws_credentials_sid(self):
        """
        :returns: The SID of the stored Credential resource
        :rtype: unicode
        """
        return self._properties['aws_credentials_sid']

    @property
    def aws_s3_url(self):
        """
        :returns: The URL of the AWS S3 bucket where the recordings are stored
        :rtype: unicode
        """
        return self._properties['aws_s3_url']

    @property
    def aws_storage_enabled(self):
        """
        :returns: Whether all recordings are written to the aws_s3_url
        :rtype: bool
        """
        return self._properties['aws_storage_enabled']

    @property
    def encryption_key_sid(self):
        """
        :returns: The SID of the Public Key resource used for encryption
        :rtype: unicode
        """
        return self._properties['encryption_key_sid']

    @property
    def encryption_enabled(self):
        """
        :returns: Whether all recordings are stored in an encrypted form
        :rtype: bool
        """
        return self._properties['encryption_enabled']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a RecordingSettingsInstance

        :returns: Fetched RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        """
        return self._proxy.fetch()

    def create(self, friendly_name, aws_credentials_sid=values.unset,
               encryption_key_sid=values.unset, aws_s3_url=values.unset,
               aws_storage_enabled=values.unset, encryption_enabled=values.unset):
        """
        Create a new RecordingSettingsInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode aws_credentials_sid: The SID of the stored Credential resource
        :param unicode encryption_key_sid: The SID of the Public Key resource to use for encryption
        :param unicode aws_s3_url: The URL of the AWS S3 bucket where the recordings should be stored
        :param bool aws_storage_enabled: Whether all recordings should be written to the aws_s3_url
        :param bool encryption_enabled: Whether all recordings should be stored in an encrypted form

        :returns: Newly created RecordingSettingsInstance
        :rtype: twilio.rest.video.v1.recording_settings.RecordingSettingsInstance
        """
        return self._proxy.create(
            friendly_name,
            aws_credentials_sid=aws_credentials_sid,
            encryption_key_sid=encryption_key_sid,
            aws_s3_url=aws_s3_url,
            aws_storage_enabled=aws_storage_enabled,
            encryption_enabled=encryption_enabled,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RecordingSettingsInstance {}>'.format(context)