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


class CreateStaminaPoolRequest(Gs2BasicRequest):

    class Constant(Gs2Stamina):
        FUNCTION = "CreateStaminaPool"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateStaminaPoolRequest, self).__init__(params)
        if params is None:
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__increase_interval = None
            self.__consume_stamina_trigger_script = None
            self.__consume_stamina_done_trigger_script = None
            self.__add_stamina_trigger_script = None
            self.__add_stamina_done_trigger_script = None
            self.__get_max_stamina_trigger_script = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_increase_interval(params['increaseInterval'] if 'increaseInterval' in params.keys() else None)
            self.set_consume_stamina_trigger_script(params['consumeStaminaTriggerScript'] if 'consumeStaminaTriggerScript' in params.keys() else None)
            self.set_consume_stamina_done_trigger_script(params['consumeStaminaDoneTriggerScript'] if 'consumeStaminaDoneTriggerScript' in params.keys() else None)
            self.set_add_stamina_trigger_script(params['addStaminaTriggerScript'] if 'addStaminaTriggerScript' in params.keys() else None)
            self.set_add_stamina_done_trigger_script(params['addStaminaDoneTriggerScript'] if 'addStaminaDoneTriggerScript' in params.keys() else None)
            self.set_get_max_stamina_trigger_script(params['getMaxStaminaTriggerScript'] if 'getMaxStaminaTriggerScript' in params.keys() else None)

    def get_name(self):
        """
        スタミナプールの名前を取得
        :return: スタミナプールの名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        スタミナプールの名前を設定
        :param name: スタミナプールの名前
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        スタミナプールの名前を設定
        :param name: スタミナプールの名前
        :type name: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_name(name)
        return self

    def get_description(self):
        """
        スタミナプールの説明を取得
        :return: スタミナプールの説明
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        スタミナプールの説明を設定
        :param description: スタミナプールの説明
        :type description: unicode
        """
        self.__description = description

    def with_description(self, description):
        """
        スタミナプールの説明を設定
        :param description: スタミナプールの説明
        :type description: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_description(description)
        return self

    def get_service_class(self):
        """
        スタミナプールのサービスクラスを取得
        :return: スタミナプールのサービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        スタミナプールのサービスクラスを設定
        :param service_class: スタミナプールのサービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        スタミナプールのサービスクラスを設定
        :param service_class: スタミナプールのサービスクラス
        :type service_class: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_service_class(service_class)
        return self

    def get_increase_interval(self):
        """
        スタミナの回復速度(秒)を取得
        :return: スタミナの回復速度(秒)
        :rtype: int
        """
        return self.__increase_interval

    def set_increase_interval(self, increase_interval):
        """
        スタミナの回復速度(秒)を設定
        :param increase_interval: スタミナの回復速度(秒)
        :type increase_interval: int
        """
        self.__increase_interval = increase_interval

    def with_increase_interval(self, increase_interval):
        """
        スタミナの回復速度(秒)を設定
        :param increase_interval: スタミナの回復速度(秒)
        :type increase_interval: int
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_increase_interval(increase_interval)
        return self

    def get_consume_stamina_trigger_script(self):
        """
        スタミナ消費時 に実行されるGS2-Scriptを取得
        :return: スタミナ消費時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_stamina_trigger_script

    def set_consume_stamina_trigger_script(self, consume_stamina_trigger_script):
        """
        スタミナ消費時 に実行されるGS2-Scriptを設定
        :param consume_stamina_trigger_script: スタミナ消費時 に実行されるGS2-Script
        :type consume_stamina_trigger_script: unicode
        """
        self.__consume_stamina_trigger_script = consume_stamina_trigger_script

    def with_consume_stamina_trigger_script(self, consume_stamina_trigger_script):
        """
        スタミナ消費時 に実行されるGS2-Scriptを設定
        :param consume_stamina_trigger_script: スタミナ消費時 に実行されるGS2-Script
        :type consume_stamina_trigger_script: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_consume_stamina_trigger_script(consume_stamina_trigger_script)
        return self

    def get_consume_stamina_done_trigger_script(self):
        """
        スタミナ消費完了時 に実行されるGS2-Scriptを取得
        :return: スタミナ消費完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_stamina_done_trigger_script

    def set_consume_stamina_done_trigger_script(self, consume_stamina_done_trigger_script):
        """
        スタミナ消費完了時 に実行されるGS2-Scriptを設定
        :param consume_stamina_done_trigger_script: スタミナ消費完了時 に実行されるGS2-Script
        :type consume_stamina_done_trigger_script: unicode
        """
        self.__consume_stamina_done_trigger_script = consume_stamina_done_trigger_script

    def with_consume_stamina_done_trigger_script(self, consume_stamina_done_trigger_script):
        """
        スタミナ消費完了時 に実行されるGS2-Scriptを設定
        :param consume_stamina_done_trigger_script: スタミナ消費完了時 に実行されるGS2-Script
        :type consume_stamina_done_trigger_script: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_consume_stamina_done_trigger_script(consume_stamina_done_trigger_script)
        return self

    def get_add_stamina_trigger_script(self):
        """
        スタミナ回復時 に実行されるGS2-Scriptを取得
        :return: スタミナ回復時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__add_stamina_trigger_script

    def set_add_stamina_trigger_script(self, add_stamina_trigger_script):
        """
        スタミナ回復時 に実行されるGS2-Scriptを設定
        :param add_stamina_trigger_script: スタミナ回復時 に実行されるGS2-Script
        :type add_stamina_trigger_script: unicode
        """
        self.__add_stamina_trigger_script = add_stamina_trigger_script

    def with_add_stamina_trigger_script(self, add_stamina_trigger_script):
        """
        スタミナ回復時 に実行されるGS2-Scriptを設定
        :param add_stamina_trigger_script: スタミナ回復時 に実行されるGS2-Script
        :type add_stamina_trigger_script: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_add_stamina_trigger_script(add_stamina_trigger_script)
        return self

    def get_add_stamina_done_trigger_script(self):
        """
        スタミナ回復完了時 に実行されるGS2-Scriptを取得
        :return: スタミナ回復完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__add_stamina_done_trigger_script

    def set_add_stamina_done_trigger_script(self, add_stamina_done_trigger_script):
        """
        スタミナ回復完了時 に実行されるGS2-Scriptを設定
        :param add_stamina_done_trigger_script: スタミナ回復完了時 に実行されるGS2-Script
        :type add_stamina_done_trigger_script: unicode
        """
        self.__add_stamina_done_trigger_script = add_stamina_done_trigger_script

    def with_add_stamina_done_trigger_script(self, add_stamina_done_trigger_script):
        """
        スタミナ回復完了時 に実行されるGS2-Scriptを設定
        :param add_stamina_done_trigger_script: スタミナ回復完了時 に実行されるGS2-Script
        :type add_stamina_done_trigger_script: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_add_stamina_done_trigger_script(add_stamina_done_trigger_script)
        return self

    def get_get_max_stamina_trigger_script(self):
        """
        スタミナの最大値取得 に実行されるGS2-Scriptを取得
        :return: スタミナの最大値取得 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__get_max_stamina_trigger_script

    def set_get_max_stamina_trigger_script(self, get_max_stamina_trigger_script):
        """
        スタミナの最大値取得 に実行されるGS2-Scriptを設定
        :param get_max_stamina_trigger_script: スタミナの最大値取得 に実行されるGS2-Script
        :type get_max_stamina_trigger_script: unicode
        """
        self.__get_max_stamina_trigger_script = get_max_stamina_trigger_script

    def with_get_max_stamina_trigger_script(self, get_max_stamina_trigger_script):
        """
        スタミナの最大値取得 に実行されるGS2-Scriptを設定
        :param get_max_stamina_trigger_script: スタミナの最大値取得 に実行されるGS2-Script
        :type get_max_stamina_trigger_script: unicode
        :return: this
        :rtype: CreateStaminaPoolRequest
        """
        self.set_get_max_stamina_trigger_script(get_max_stamina_trigger_script)
        return self
