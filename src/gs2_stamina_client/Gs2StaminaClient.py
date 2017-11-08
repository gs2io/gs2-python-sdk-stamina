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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2StaminaClient(AbstractGs2Client):

    ENDPOINT = "stamina"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2StaminaClient, self).__init__(credential, region)


    def change_stamina(self, request):
        """
        スタミナを増減します<br>
        <br>
        - 消費クオータ: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.ChangeStaminaRequest.ChangeStaminaRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.ChangeStaminaResult.ChangeStaminaResult
        """
        body = { 
            "maxValue": request.get_max_value(),
            "variation": request.get_variation(),
        }

        if request.get_overflow() is not None:
            body["overflow"] = request.get_overflow()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_stamina_client.control.ChangeStaminaRequest import ChangeStaminaRequest

        from gs2_stamina_client.control.ChangeStaminaResult import ChangeStaminaResult
        return ChangeStaminaResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "/stamina",
            service=self.ENDPOINT,
            module=ChangeStaminaRequest.Constant.MODULE,
            function=ChangeStaminaRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def consume_stamina(self, request):
        """
        スタミナを消費します。<br>
        このエンドポイントは回復に使用できません。<br>
        ポリシーで消費と回復を分けて管理したい場合に使用してください。<br>
        <br>
        - 消費クオータ: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.ConsumeStaminaRequest.ConsumeStaminaRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.ConsumeStaminaResult.ConsumeStaminaResult
        """
        body = { 
            "maxValue": request.get_max_value(),
            "variation": request.get_variation(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_stamina_client.control.ConsumeStaminaRequest import ConsumeStaminaRequest

        from gs2_stamina_client.control.ConsumeStaminaResult import ConsumeStaminaResult
        return ConsumeStaminaResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "/stamina/consume",
            service=self.ENDPOINT,
            module=ConsumeStaminaRequest.Constant.MODULE,
            function=ConsumeStaminaRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_stamina_pool(self, request):
        """
        スタミナプールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.CreateStaminaPoolRequest.CreateStaminaPoolRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.CreateStaminaPoolResult.CreateStaminaPoolResult
        """
        body = { 
            "increaseInterval": request.get_increase_interval(),
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_stamina_client.control.CreateStaminaPoolRequest import CreateStaminaPoolRequest

        from gs2_stamina_client.control.CreateStaminaPoolResult import CreateStaminaPoolResult
        return CreateStaminaPoolResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool",
            service=self.ENDPOINT,
            module=CreateStaminaPoolRequest.Constant.MODULE,
            function=CreateStaminaPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_stamina_pool(self, request):
        """
        スタミナプールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.DeleteStaminaPoolRequest.DeleteStaminaPoolRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_stamina_client.control.DeleteStaminaPoolRequest import DeleteStaminaPoolRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "",
            service=self.ENDPOINT,
            module=DeleteStaminaPoolRequest.Constant.MODULE,
            function=DeleteStaminaPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_stamina_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_stamina_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/serviceClass",
            service=self.ENDPOINT,
            module=DescribeServiceClassRequest.Constant.MODULE,
            function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_stamina_pool(self, request):
        """
        スタミナプールの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.DescribeStaminaPoolRequest.DescribeStaminaPoolRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.DescribeStaminaPoolResult.DescribeStaminaPoolResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_stamina_client.control.DescribeStaminaPoolRequest import DescribeStaminaPoolRequest

        from gs2_stamina_client.control.DescribeStaminaPoolResult import DescribeStaminaPoolResult
        return DescribeStaminaPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool",
            service=self.ENDPOINT,
            module=DescribeStaminaPoolRequest.Constant.MODULE,
            function=DescribeStaminaPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_stamina(self, request):
        """
        現在のスタミナ値を取得します<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.GetStaminaRequest.GetStaminaRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.GetStaminaResult.GetStaminaResult
        """

        query_strings = {

            'maxValue': request.get_max_value(),

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_stamina_client.control.GetStaminaRequest import GetStaminaRequest

        from gs2_stamina_client.control.GetStaminaResult import GetStaminaResult
        return GetStaminaResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "/stamina",
            service=self.ENDPOINT,
            module=GetStaminaRequest.Constant.MODULE,
            function=GetStaminaRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_stamina_pool(self, request):
        """
        スタミナプールを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.GetStaminaPoolRequest.GetStaminaPoolRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.GetStaminaPoolResult.GetStaminaPoolResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_stamina_client.control.GetStaminaPoolRequest import GetStaminaPoolRequest

        from gs2_stamina_client.control.GetStaminaPoolResult import GetStaminaPoolResult
        return GetStaminaPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "",
            service=self.ENDPOINT,
            module=GetStaminaPoolRequest.Constant.MODULE,
            function=GetStaminaPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_stamina_pool_status(self, request):
        """
        スタミナプールの状態を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.GetStaminaPoolStatusRequest.GetStaminaPoolStatusRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.GetStaminaPoolStatusResult.GetStaminaPoolStatusResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_stamina_client.control.GetStaminaPoolStatusRequest import GetStaminaPoolStatusRequest

        from gs2_stamina_client.control.GetStaminaPoolStatusResult import GetStaminaPoolStatusResult
        return GetStaminaPoolStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "/status",
            service=self.ENDPOINT,
            module=GetStaminaPoolStatusRequest.Constant.MODULE,
            function=GetStaminaPoolStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def update_stamina_pool(self, request):
        """
        スタミナプールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_stamina_client.control.UpdateStaminaPoolRequest.UpdateStaminaPoolRequest
        :return: 結果
        :rtype: gs2_stamina_client.control.UpdateStaminaPoolResult.UpdateStaminaPoolResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
            "increaseInterval": request.get_increase_interval(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_stamina_client.control.UpdateStaminaPoolRequest import UpdateStaminaPoolRequest

        from gs2_stamina_client.control.UpdateStaminaPoolResult import UpdateStaminaPoolResult
        return UpdateStaminaPoolResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/staminaPool/" + str(("null" if request.get_stamina_pool_name() is None else request.get_stamina_pool_name())) + "",
            service=self.ENDPOINT,
            module=UpdateStaminaPoolRequest.Constant.MODULE,
            function=UpdateStaminaPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


