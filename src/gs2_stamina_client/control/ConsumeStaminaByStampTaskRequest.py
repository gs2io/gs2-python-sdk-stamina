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


class ConsumeStaminaByStampTaskRequest(Gs2UserRequest):

    class Constant(Gs2Stamina):
        FUNCTION = "ConsumeStaminaByStampTask"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(ConsumeStaminaByStampTaskRequest, self).__init__(params)
        if params is None:
            self.__task = None
            self.__key_name = None
            self.__transaction_id = None
            self.__max_value = None
        else:
            self.set_task(params['task'] if 'task' in params.keys() else None)
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)
            self.set_transaction_id(params['transactionId'] if 'transactionId' in params.keys() else None)
            self.set_max_value(params['maxValue'] if 'maxValue' in params.keys() else None)

    def get_task(self):
        """
        スタンプタスクを取得
        :return: スタンプタスク
        :rtype: unicode
        """
        return self.__task

    def set_task(self, task):
        """
        スタンプタスクを設定
        :param task: スタンプタスク
        :type task: unicode
        """
        if task and not (isinstance(task, str) or isinstance(task, unicode)):
            raise TypeError(type(task))
        self.__task = task

    def with_task(self, task):
        """
        スタンプタスクを設定
        :param task: スタンプタスク
        :type task: unicode
        :return: this
        :rtype: ConsumeStaminaByStampTaskRequest
        """
        self.set_task(task)
        return self

    def get_key_name(self):
        """
        スタンプの暗号鍵を取得
        :return: スタンプの暗号鍵
        :rtype: unicode
        """
        return self.__key_name

    def set_key_name(self, key_name):
        """
        スタンプの暗号鍵を設定
        :param key_name: スタンプの暗号鍵
        :type key_name: unicode
        """
        if key_name and not (isinstance(key_name, str) or isinstance(key_name, unicode)):
            raise TypeError(type(key_name))
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        スタンプの暗号鍵を設定
        :param key_name: スタンプの暗号鍵
        :type key_name: unicode
        :return: this
        :rtype: ConsumeStaminaByStampTaskRequest
        """
        self.set_key_name(key_name)
        return self

    def get_transaction_id(self):
        """
        トランザクションIDを取得
        :return: トランザクションID
        :rtype: unicode
        """
        return self.__transaction_id

    def set_transaction_id(self, transaction_id):
        """
        トランザクションIDを設定
        :param transaction_id: トランザクションID
        :type transaction_id: unicode
        """
        if transaction_id and not (isinstance(transaction_id, str) or isinstance(transaction_id, unicode)):
            raise TypeError(type(transaction_id))
        self.__transaction_id = transaction_id

    def with_transaction_id(self, transaction_id):
        """
        トランザクションIDを設定
        :param transaction_id: トランザクションID
        :type transaction_id: unicode
        :return: this
        :rtype: ConsumeStaminaByStampTaskRequest
        """
        self.set_transaction_id(transaction_id)
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
        if max_value and not isinstance(max_value, int):
            raise TypeError(type(max_value))
        self.__max_value = max_value

    def with_max_value(self, max_value):
        """
        スタミナの最大値を設定
        :param max_value: スタミナの最大値
        :type max_value: int
        :return: this
        :rtype: ConsumeStaminaByStampTaskRequest
        """
        self.set_max_value(max_value)
        return self
