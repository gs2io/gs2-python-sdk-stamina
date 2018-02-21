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

class Stamina(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__value = None
            self.__overflow = None
            self.__last_update_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_value(params['value'] if 'value' in params.keys() else None)
            self.set_overflow(params['overflow'] if 'overflow' in params.keys() else None)
            self.set_last_update_at(params['lastUpdateAt'] if 'lastUpdateAt' in params.keys() else None)


    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_value(self):
        """
        スタミナ値を取得
        :return: スタミナ値
        :rtype: int
        """
        return self.__value

    def set_value(self, value):
        """
        スタミナ値を設定
        :param value: スタミナ値
        :type value: int
        """
        self.__value = value

    def get_overflow(self):
        """
        最大値を超えて保持しているスタミナ値を取得
        :return: 最大値を超えて保持しているスタミナ値
        :rtype: int
        """
        return self.__overflow

    def set_overflow(self, overflow):
        """
        最大値を超えて保持しているスタミナ値を設定
        :param overflow: 最大値を超えて保持しているスタミナ値
        :type overflow: int
        """
        self.__overflow = overflow

    def get_last_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__last_update_at

    def set_last_update_at(self, last_update_at):
        """
        最終更新日時(エポック秒)を設定
        :param last_update_at: 最終更新日時(エポック秒)
        :type last_update_at: int
        """
        self.__last_update_at = last_update_at

    def to_dict(self):
        return { 
            "userId": self.__user_id,
            "value": self.__value,
            "overflow": self.__overflow,
            "lastUpdateAt": self.__last_update_at,
        }