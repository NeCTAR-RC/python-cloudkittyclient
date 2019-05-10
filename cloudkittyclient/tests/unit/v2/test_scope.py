# Copyright 2019 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
from cloudkittyclient.tests.unit.v2 import base


class TestScope(base.BaseAPIEndpointTestCase):

    def test_get_scope(self):
        self.scope.get_scope_state()
        self.api_client.get.assert_called_once_with('/v2/scope')

    def test_get_scope_with_args(self):
        self.scope.get_scope_state(offset=10, limit=10)
        try:
            self.api_client.get.assert_called_once_with(
                '/v2/scope?limit=10&offset=10')
        except AssertionError:
            self.api_client.get.assert_called_once_with(
                '/v2/scope?offset=10&limit=10')
