# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Baseline(Model):
    """The baseline values for a single sensitivity value.

    All required parameters must be populated in order to send to Azure.

    :param sensitivity: Required. the sensitivity of the baseline. Possible
     values include: 'Low', 'Medium', 'High'
    :type sensitivity: str or ~azure.mgmt.monitor.models.Sensitivity
    :param low_thresholds: Required. The low thresholds of the baseline.
    :type low_thresholds: list[float]
    :param high_thresholds: Required. The high thresholds of the baseline.
    :type high_thresholds: list[float]
    """

    _validation = {
        'sensitivity': {'required': True},
        'low_thresholds': {'required': True},
        'high_thresholds': {'required': True},
    }

    _attribute_map = {
        'sensitivity': {'key': 'sensitivity', 'type': 'Sensitivity'},
        'low_thresholds': {'key': 'lowThresholds', 'type': '[float]'},
        'high_thresholds': {'key': 'highThresholds', 'type': '[float]'},
    }

    def __init__(self, *, sensitivity, low_thresholds, high_thresholds, **kwargs) -> None:
        super(Baseline, self).__init__(**kwargs)
        self.sensitivity = sensitivity
        self.low_thresholds = low_thresholds
        self.high_thresholds = high_thresholds
