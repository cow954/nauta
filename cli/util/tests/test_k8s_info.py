#
# INTEL CONFIDENTIAL
# Copyright (c) 2018 Intel Corporation
#
# The source code contained or described herein and all documents related to
# the source code ("Material") are owned by Intel Corporation or its suppliers
# or licensors. Title to the Material remains with Intel Corporation or its
# suppliers and licensors. The Material contains trade secrets and proprietary
# and confidential information of Intel or its suppliers and licensors. The
# Material is protected by worldwide copyright and trade secret laws and treaty
# provisions. No part of the Material may be used, copied, reproduced, modified,
# published, uploaded, posted, transmitted, distributed, or disclosed in any way
# without Intel's prior express written permission.
#
# No license under any patent, copyright, trade secret or other intellectual
# property right is granted to or conferred upon you by disclosure or delivery
# of the Materials, either expressly, by implication, inducement, estoppel or
# otherwise. Any license under such intellectual property rights must be express
# and approved by Intel in writing.
#

import pytest

from util.k8s_info import get_kubectl_port, get_kubectl_host


@pytest.fixture()
def mocked_k8s_config(mocker):
    mocked_conf_class = mocker.patch('kubernetes.client.configuration.Configuration')
    conf_instance = mocked_conf_class.return_value
    conf_instance.host = 'https://127.0.0.1:8080'


def test_get_k8s_host(mocked_k8s_config):
    k8s_host = get_kubectl_host()

    assert k8s_host == '127.0.0.1'


def test_get_k8s_port(mocked_k8s_config):
    k8s_port = get_kubectl_port()

    assert k8s_port == 8080