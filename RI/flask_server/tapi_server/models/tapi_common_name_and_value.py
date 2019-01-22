# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiCommonNameAndValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value_name=None, value=None):  # noqa: E501
        """TapiCommonNameAndValue - a model defined in OpenAPI

        :param value_name: The value_name of this TapiCommonNameAndValue.  # noqa: E501
        :type value_name: str
        :param value: The value of this TapiCommonNameAndValue.  # noqa: E501
        :type value: str
        """
        self.openapi_types = {
            'value_name': str,
            'value': str
        }

        self.attribute_map = {
            'value_name': 'value-name',
            'value': 'value'
        }

        self._value_name = value_name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonNameAndValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.NameAndValue of this TapiCommonNameAndValue.  # noqa: E501
        :rtype: TapiCommonNameAndValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value_name(self):
        """Gets the value_name of this TapiCommonNameAndValue.

        The name of the value. The value need not have a name.  # noqa: E501

        :return: The value_name of this TapiCommonNameAndValue.
        :rtype: str
        """
        return self._value_name

    @value_name.setter
    def value_name(self, value_name):
        """Sets the value_name of this TapiCommonNameAndValue.

        The name of the value. The value need not have a name.  # noqa: E501

        :param value_name: The value_name of this TapiCommonNameAndValue.
        :type value_name: str
        """

        self._value_name = value_name

    @property
    def value(self):
        """Gets the value of this TapiCommonNameAndValue.

        The value  # noqa: E501

        :return: The value of this TapiCommonNameAndValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TapiCommonNameAndValue.

        The value  # noqa: E501

        :param value: The value of this TapiCommonNameAndValue.
        :type value: str
        """

        self._value = value