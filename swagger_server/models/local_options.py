# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LocalOptions(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, more_than_two_samples: bool=False, threshold_method: str='mean', minimum: str=None, maximum: str=None, custom_library_url: str=None):  # noqa: E501
        """LocalOptions - a model defined in Swagger

        :param id: The id of this LocalOptions.  # noqa: E501
        :type id: int
        :param more_than_two_samples: The more_than_two_samples of this LocalOptions.  # noqa: E501
        :type more_than_two_samples: bool
        :param threshold_method: The threshold_method of this LocalOptions.  # noqa: E501
        :type threshold_method: str
        :param minimum: The minimum of this LocalOptions.  # noqa: E501
        :type minimum: str
        :param maximum: The maximum of this LocalOptions.  # noqa: E501
        :type maximum: str
        :param custom_library_url: The custom_library_url of this LocalOptions.  # noqa: E501
        :type custom_library_url: str
        """
        self.swagger_types = {
            'id': int,
            'more_than_two_samples': bool,
            'threshold_method': str,
            'minimum': str,
            'maximum': str,
            'custom_library_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'more_than_two_samples': 'moreThanTwoSamples',
            'threshold_method': 'thresholdMethod',
            'minimum': 'minimum',
            'maximum': 'maximum',
            'custom_library_url': 'customLibraryUrl'
        }

        self._id = id
        self._more_than_two_samples = more_than_two_samples
        self._threshold_method = threshold_method
        self._minimum = minimum
        self._maximum = maximum
        self._custom_library_url = custom_library_url

    @classmethod
    def from_dict(cls, dikt) -> 'LocalOptions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocalOptions of this LocalOptions.  # noqa: E501
        :rtype: LocalOptions
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this LocalOptions.


        :return: The id of this LocalOptions.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this LocalOptions.


        :param id: The id of this LocalOptions.
        :type id: int
        """

        self._id = id

    @property
    def more_than_two_samples(self) -> bool:
        """Gets the more_than_two_samples of this LocalOptions.


        :return: The more_than_two_samples of this LocalOptions.
        :rtype: bool
        """
        return self._more_than_two_samples

    @more_than_two_samples.setter
    def more_than_two_samples(self, more_than_two_samples: bool):
        """Sets the more_than_two_samples of this LocalOptions.


        :param more_than_two_samples: The more_than_two_samples of this LocalOptions.
        :type more_than_two_samples: bool
        """
        if more_than_two_samples is None:
            raise ValueError("Invalid value for `more_than_two_samples`, must not be `None`")  # noqa: E501

        self._more_than_two_samples = more_than_two_samples

    @property
    def threshold_method(self) -> str:
        """Gets the threshold_method of this LocalOptions.


        :return: The threshold_method of this LocalOptions.
        :rtype: str
        """
        return self._threshold_method

    @threshold_method.setter
    def threshold_method(self, threshold_method: str):
        """Sets the threshold_method of this LocalOptions.


        :param threshold_method: The threshold_method of this LocalOptions.
        :type threshold_method: str
        """
        allowed_values = ["minMaxMean", "mean", "custom"]  # noqa: E501
        if threshold_method not in allowed_values:
            raise ValueError(
                "Invalid value for `threshold_method` ({0}), must be one of {1}"
                .format(threshold_method, allowed_values)
            )

        self._threshold_method = threshold_method

    @property
    def minimum(self) -> str:
        """Gets the minimum of this LocalOptions.


        :return: The minimum of this LocalOptions.
        :rtype: str
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum: str):
        """Sets the minimum of this LocalOptions.


        :param minimum: The minimum of this LocalOptions.
        :type minimum: str
        """

        self._minimum = minimum

    @property
    def maximum(self) -> str:
        """Gets the maximum of this LocalOptions.


        :return: The maximum of this LocalOptions.
        :rtype: str
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: str):
        """Sets the maximum of this LocalOptions.


        :param maximum: The maximum of this LocalOptions.
        :type maximum: str
        """

        self._maximum = maximum

    @property
    def custom_library_url(self) -> str:
        """Gets the custom_library_url of this LocalOptions.


        :return: The custom_library_url of this LocalOptions.
        :rtype: str
        """
        return self._custom_library_url

    @custom_library_url.setter
    def custom_library_url(self, custom_library_url: str):
        """Sets the custom_library_url of this LocalOptions.


        :param custom_library_url: The custom_library_url of this LocalOptions.
        :type custom_library_url: str
        """

        self._custom_library_url = custom_library_url