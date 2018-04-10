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

from typing import List

from util.system import execute_system_command
from util.logger import initialize_logger

log = initialize_logger('draft.cmd')

DRAFT_BIN = 'draft'


def call_draft(args: List[str]) -> (str, int):
    full_command = [DRAFT_BIN]
    full_command.extend(args)

    return execute_system_command(full_command)


def create():
    output, exit_code = call_draft(['create'])
    print(output)


def up():
    output, exit_code = call_draft(['up'])
    print(output)
