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


class OcrRegion(Model):
    """A region consists of multiple lines (e.g. a column of text in a
    multi-column document).

    :param bounding_box: Bounding box of a recognized region. The four
     integers represent the x-coordinate of the left edge, the y-coordinate of
     the top edge, width, and height of the bounding box, in the coordinate
     system of the input image, after it has been rotated around its center
     according to the detected text angle (see textAngle property), with the
     origin at the top-left corner, and the y-axis pointing down.
    :type bounding_box: str
    :param lines:
    :type lines:
     list[~azure.cognitiveservices.vision.computervision.models.OcrLine]
    """

    _attribute_map = {
        'bounding_box': {'key': 'boundingBox', 'type': 'str'},
        'lines': {'key': 'lines', 'type': '[OcrLine]'},
    }

    def __init__(self, bounding_box=None, lines=None):
        self.bounding_box = bounding_box
        self.lines = lines