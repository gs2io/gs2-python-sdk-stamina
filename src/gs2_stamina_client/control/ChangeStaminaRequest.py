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


class ChangeStaminaRequest(Gs2UserRequest):

    class Constant(Gs2Stamina):
        FUNCTION = "ChangeStamina"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ChangeStaminaRequest, self).__init__(params)
        if params is None:
            self.__stamina_pool_name = None
            self.__overflow = None
            self.__max_value = None
            self.__variation = None
        else:
            self.set_stamina_pool_name(params['staminaPoolName'] if 'staminaPoolName' in params.keys() else None)
            self.set_overflow(params['overflow'] if 'overflow' in params.keys() else None)
            self.set_max_value(params['maxValue'] if 'maxValue' in params.keys() else None)
            self.set_variation(params['variation'] if 'variation' in params.keys() else None)

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
        :rtype: ChangeStaminaRequest
        """
        self.set_stamina_pool_name(stamina_pool_name)
        return self

    def get_overflow(self):
        """
        スタミナを回復する際に最大値を超えて回復するかを取得
        :return: スタミナを回復する際に最大値を超えて回復するか
        :rtype: bool
        """
        return self.__overflow

    def set_overflow(self, overflow):
        """
        スタミナを回復する際に最大値を超えて回復するかを設定
        :param overflow: スタミナを回復する際に最大値を超えて回復するか
        :type overflow: bool
        """
        if not isinstance(overflow, bool):
            raise TypeError(type(overflow))
        self.__overflow = overflow

    def with_overflow(self, overflow):
        """
        スタミナを回復する際に最大値を超えて回復するかを設定
        :param overflow: スタミナを回復する際に最大値を超えて回復するか
        :type overflow: bool
        :return: this
        :rtype: ChangeStaminaRequest
        """
        self.set_overflow(overflow)
        return self

    def get_max_value(self):
        """
        スタミナの最大値を取得
        :return: スタミナの最大値
        :rtype: int
        """
        return self.__max_value

    def set_max_value(self, max_value):
        """
        スタミナの最大値を設定
        :param max_value: スタミナの最大値
        :type max_value: int
        """
        if not isinstance(max_value, int):
            raise TypeError(type(max_value))
        self.__max_value = max_value

    def with_max_value(self, max_value):
        """
        スタミナの最大値を設定
        :param max_value: スタミナの最大値
        :type max_value: int
        :return: this
        :rtype: ChangeStaminaRequest
        """
        self.set_max_value(max_value)
        return self

    def get_variation(self):
        """
        スタミナの増減量を取得
        :return: スタミナの増減量
        :rtype: int
        """
        return self.__variation

    def set_variation(self, variation):
        """
        スタミナの増減量を設定
        :param variation: スタミナの増減量
        :type variation: int
        """
        if not isinstance(variation, int):
            raise TypeError(type(variation))
        self.__variation = variation

    def with_variation(self, variation):
        """
        スタミナの増減量を設定
        :param variation: スタミナの増減量
        :type variation: int
        :return: this
        :rtype: ChangeStaminaRequest
        """
        self.set_variation(variation)
        return self
