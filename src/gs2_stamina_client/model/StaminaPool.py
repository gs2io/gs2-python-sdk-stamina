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

class StaminaPool(object):

    def __init__(self, params=None):
        if params is None:
            self.__description = None
            self.__stamina_pool_id = None
            self.__service_class = None
            self.__create_at = None
            self.__owner_id = None
            self.__increase_interval = None
            self.__update_at = None
            self.__name = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_stamina_pool_id(params['staminaPoolId'] if 'staminaPoolId' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_increase_interval(params['increaseInterval'] if 'increaseInterval' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)


    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def get_stamina_pool_id(self):
        """
        スタミナプールGRNを取得
        :return: スタミナプールGRN
        :rtype: unicode
        """
        return self.__stamina_pool_id

    def set_stamina_pool_id(self, stamina_pool_id):
        """
        スタミナプールGRNを設定
        :param stamina_pool_id: スタミナプールGRN
        :type stamina_pool_id: unicode
        """
        self.__stamina_pool_id = stamina_pool_id

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

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

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_name(self):
        """
        スタミナプール名を取得
        :return: スタミナプール名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        スタミナプール名を設定
        :param name: スタミナプール名
        :type name: unicode
        """
        self.__name = name

    def to_dict(self):
        return { 
            "description": self.__description,
            "staminaPoolId": self.__stamina_pool_id,
            "serviceClass": self.__service_class,
            "createAt": self.__create_at,
            "ownerId": self.__owner_id,
            "increaseInterval": self.__increase_interval,
            "updateAt": self.__update_at,
            "name": self.__name,
        }