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


class JobPropertiesExecutionInfo(Model):
    """Contains information about the execution of a job in the Azure Batch
    service.

    :param start_time: The time at which the job started running. 'Running'
     corresponds to the running state. If the job has been restarted or
     retried, this is the most recent time at which the job started running.
     This property is present only for job that are in the running or completed
     state.
    :type start_time: datetime
    :param end_time: The time at which the job completed. This property is
     only returned if the job is in completed state.
    :type end_time: datetime
    :param exit_code: The exit code of the job. This property is only returned
     if the job is in completed state.
    :type exit_code: int
    :param errors: Contains details of various errors encountered by the
     service during job execution.
    :type errors: list of :class:`BatchAIError
     <azure.mgmt.batchai.models.BatchAIError>`
    """

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'errors': {'key': 'errors', 'type': '[BatchAIError]'},
    }

    def __init__(self, start_time=None, end_time=None, exit_code=None, errors=None):
        self.start_time = start_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.errors = errors