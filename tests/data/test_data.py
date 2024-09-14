# -*- coding: utf-8 -*-
# Copyright 2024 Ant Group Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest
from datasets import Dataset

from yijian_community.data import load_data, save_data


def test_load_data_invalid_data_path():
    with pytest.raises(ValueError):
        load_data("data.txt")


def test_save_data_invalid_data_path():
    with pytest.raises(ValueError):
        save_data("data.txt", Dataset.from_dict({"prompt_text": ["tell me a joke"]}))

if __name__ == "__main__":
    test_load_data_invalid_data_path()
    test_save_data_invalid_data_path()
