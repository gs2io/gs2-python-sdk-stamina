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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_stamina_client.Gs2Stamina import Gs2Stamina


class GetStaminaRequest(Gs2UserRequest):

    class Constant(Gs2Stamina):
        FUNCTION = "GetStamina"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetStaminaRequest, self).__init__(params)
        if params is None:
            self.__stamina_pool_name = None
            self.__max_value = None
        else:
            self.set_stamina_pool_name(params['staminaPoolName'] if 'staminaPoolName' in params.keys() else None)
            self.set_max_value(params['maxValue'] if 'maxValue' in params.keys() else None)

    def get_stamina_pool_name(self):
        """
        スタミナプールの名前を指定します。を取得
        :return: スタミナプールの名前を指定します。
        :rtype: unicode
        """
        return self.__stamina_pool_name

    def set_stamina_pool_name(self, stamina_pool_name):
        """
        スタミナプールの名前を指定します。を設定
        :param stamina_pool_name: スタミナプールの名前を指定します。
        :type stamina_pool_name: unicode
        """
        if not isinstance(stamina_pool_name, unicode):
            raise TypeError(type(stamina_pool_name))
        self.__stamina_pool_name = stamina_pool_name

    def with_stamina_pool_name(self, stamina_pool_name):
        """
        スタミナプールの名前を指定します。を設定
        :param stamina_pool_name: スタミナプールの名前を指定します。
        :type stamina_pool_name: unicode
        :return: this
        :rtype: GetStaminaRequest
        """
        self.set_stamina_pool_name(stamina_pool_name)
        return self

    def get_max_value(self):
        """
        スタミナの最大値を指定しますを取得
        :return: スタミナの最大値を指定します
        :rtype: int
        """
        return self.__max_value

    def set_max_value(self, max_value):
        """
        スタミナの最大値を指定しますを設定
        :param max_value: スタミナの最大値を指定します
        :type max_value: int
        """
        if not isinstance(max_value, int):
            raise TypeError(type(max_value))
        self.__max_value = max_value

    def with_max_value(self, max_value):
        """
        スタミナの最大値を指定しますを設定
        :param max_value: スタミナの最大値を指定します
        :type max_value: int
        :return: this
        :rtype: GetStaminaRequest
        """
        self.set_max_value(max_value)
        return self
