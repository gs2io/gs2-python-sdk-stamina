# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_stamina_client.model import *


class ConsumeStaminaResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        self.__item = Stamina(response['item']) if 'item' in response.keys() and response['item'] is not None else None
        self.__next_increase_timestamp = int(response['nextIncreaseTimestamp']) if 'nextIncreaseTimestamp' in response.keys() and response['nextIncreaseTimestamp'] is not None else None
    def get_item(self):
        """
        スタミナを取得
        :return: スタミナ
        :rtype: Stamina
        """
        return self.__item
    def get_next_increase_timestamp(self):
        """
        次にスタミナが回復する時間を取得
        :return: 次にスタミナが回復する時間
        :rtype: int
        """
        return self.__next_increase_timestamp

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(ConsumeStaminaResult, self).__getitem__(key)

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return {
            'item': self.__item.to_dict(),
            'nextIncreaseTimestamp': self.__next_increase_timestamp,
        }
