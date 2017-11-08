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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_stamina_client.Gs2Stamina import Gs2Stamina


class DeleteStaminaPoolRequest(Gs2BasicRequest):

    class Constant(Gs2Stamina):
        FUNCTION = "DeleteStaminaPool"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteStaminaPoolRequest, self).__init__(params)
        if params is None:
            self.__stamina_pool_name = None
        else:
            self.set_stamina_pool_name(params['staminaPoolName'] if 'staminaPoolName' in params.keys() else None)

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
        self.__stamina_pool_name = stamina_pool_name

    def with_stamina_pool_name(self, stamina_pool_name):
        """
        スタミナプールの名前を指定します。を設定
        :param stamina_pool_name: スタミナプールの名前を指定します。
        :type stamina_pool_name: unicode
        :return: this
        :rtype: DeleteStaminaPoolRequest
        """
        self.set_stamina_pool_name(stamina_pool_name)
        return self
