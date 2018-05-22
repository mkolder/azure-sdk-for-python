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


class BackupPolicyDescription(Model):
    """Describes a backup policy for configuring periodic backup.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The unique name identifying this backup policy.
    :type name: str
    :param auto_restore_on_data_loss: Required. Specifies whether to trigger
     restore automatically using the latest available backup in case the
     partition experiences a data loss event.
    :type auto_restore_on_data_loss: bool
    :param max_incremental_backups: Required. Defines the maximum number of
     incremental backups to be taken between two full backups. This is just the
     upper limit. A full backup may be taken before specified number of
     incremental backups are completed in one of the following conditions
     - The replica has never taken a full backup since it has become primary,
     - Some of the log records since the last backup has been truncated, or
     - Replica passed the MaxAccumulatedBackupLogSizeInMB limit.
    :type max_incremental_backups: int
    :param schedule: Required. Describes the backup schedule parameters.
    :type schedule: ~azure.servicefabric.models.BackupScheduleDescription
    :param storage: Required. Describes the details of backup storage where to
     store the periodic backups.
    :type storage: ~azure.servicefabric.models.BackupStorageDescription
    """

    _validation = {
        'name': {'required': True},
        'auto_restore_on_data_loss': {'required': True},
        'max_incremental_backups': {'required': True, 'maximum': 255, 'minimum': 0},
        'schedule': {'required': True},
        'storage': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'auto_restore_on_data_loss': {'key': 'AutoRestoreOnDataLoss', 'type': 'bool'},
        'max_incremental_backups': {'key': 'MaxIncrementalBackups', 'type': 'int'},
        'schedule': {'key': 'Schedule', 'type': 'BackupScheduleDescription'},
        'storage': {'key': 'Storage', 'type': 'BackupStorageDescription'},
    }

    def __init__(self, *, name: str, auto_restore_on_data_loss: bool, max_incremental_backups: int, schedule, storage, **kwargs) -> None:
        super(BackupPolicyDescription, self).__init__(**kwargs)
        self.name = name
        self.auto_restore_on_data_loss = auto_restore_on_data_loss
        self.max_incremental_backups = max_incremental_backups
        self.schedule = schedule
        self.storage = storage