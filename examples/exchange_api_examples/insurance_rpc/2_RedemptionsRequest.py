# Copyright 2021 Injective Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Injective Exchange API client for Python. Example only."""

import asyncio
import logging
import grpc

import injective.exchange_api.injective_insurance_rpc_pb2 as insurance_rpc_pb
import injective.exchange_api.injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('testnet-sentry0.injective.network:9910') as channel:
        insurance_exchange_rpc = insurance_rpc_grpc.InjectiveInsuranceRPCStub(channel)
        
        redemptions = await insurance_exchange_rpc.Redemptions(insurance_rpc_pb.RedemptionsRequest())
        print("\n-- Redemptions Update:\n", redemptions)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())