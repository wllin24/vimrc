#     Copyright 2015 Cedraro Andrea <a.cedraro@gmail.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#    limitations under the License.

import os
import sys


def add_vendor_folder_to_sys_path():
    vendor_folder = os.path.join(os.path.dirname(__file__), '..', 'vendor')

    for folder in os.listdir(vendor_folder):
        sys.path.insert(0, os.path.realpath(os.path.join(vendor_folder,
                                                         folder)))
