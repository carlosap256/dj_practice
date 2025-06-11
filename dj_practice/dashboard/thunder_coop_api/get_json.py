# from dashboard.thunder_coop_api.serializers import NormalSerializer, Normal, BigRunSerializer, BigRun, TeamContestSerializer, TeamContest, PhaseRewardsSerializer
from rest_framework.serializers import ModelSerializer
from dashboard.thunder_coop_api.serializers import deserialize_bulk

import json
import urllib3

def get_current_json()-> str:
    return example_json


class JsonDataGrabber:
  # url="https://lemoncapsule.com/api/v1/three/coop/phases"
  url="https://splatoon.oatmealdome.me/api/v1/three/coop/phases?count=5"

  def __init__(self, url=None, etag=None):
      if url is not None:
         self.url = url
      self.etag = etag
  
  def get_json_data_from_url(self):
      resp = urllib3.request("GET", self.url, headers=self.build_headers())
      print(resp.headers)
      return resp.data if resp.status == 200 else None
  
  def build_headers(self):
      headers = urllib3.HTTPHeaderDict()
      # headers.add("Accept", "application/json")
      headers.add("Accept", "text/plain")
      if self.etag:
          headers.add("etag", self.etag)
      return headers
    
def data_importer(url=None):
    grabber = JsonDataGrabber(url)

    raw_string_data = grabber.get_json_data_from_url()
    new_objects_added = deserialize_bulk(raw_string_data)
    return new_objects_added


example_json='''
{
  "Normal": [
    {
      "bigBoss": "SakeRope",
      "rewardGear": {
        "rewardId": "6825bd798e479642ada4750f",
        "kind": "Head",
        "id": 21018
      },
      "phaseId": "6825bd798e479642ada4750e",
      "startTime": "2025-05-22T00:00:00Z",
      "endTime": "2025-05-23T16:00:00Z",
      "stage": 9,
      "weapons": [
        1020,
        200,
        5020,
        2000
      ],
      "rareWeapons": []
    },
    {
      "bigBoss": "SakeJaw",
      "rewardGear": {
        "rewardId": "6827eff98e479642ada47539",
        "kind": "Clothes",
        "id": 21013
      },
      "phaseId": "6827eff98e479642ada47538",
      "startTime": "2025-05-23T16:00:00Z",
      "endTime": "2025-05-25T08:00:00Z",
      "stage": 8,
      "weapons": [
        1100,
        3030,
        8000,
        7030
      ],
      "rareWeapons": []
    },
    {
      "bigBoss": "SakelienGiant",
      "rewardGear": {
        "rewardId": "682a22798e479642ada47563",
        "kind": "Head",
        "id": 21019
      },
      "phaseId": "682a22798e479642ada47562",
      "startTime": "2025-05-25T08:00:00Z",
      "endTime": "2025-05-27T00:00:00Z",
      "stage": 1,
      "weapons": [
        3010,
        0,
        3000,
        80
      ],
      "rareWeapons": []
    },
    {
      "bigBoss": "SakeRope",
      "rewardGear": {
        "rewardId": "682c54f98e479642ada47594",
        "kind": "Clothes",
        "id": 21014
      },
      "phaseId": "682c54f98e479642ada47593",
      "startTime": "2025-05-27T00:00:00Z",
      "endTime": "2025-05-28T16:00:00Z",
      "stage": 2,
      "weapons": [
        8010,
        10,
        30,
        4020
      ],
      "rareWeapons": []
    },
    {
      "bigBoss": "SakeJaw",
      "rewardGear": {
        "rewardId": "682e87798e479642ada47695",
        "kind": "Shoes",
        "id": 21008
      },
      "phaseId": "682e87798e479642ada47694",
      "startTime": "2025-05-28T16:00:00Z",
      "endTime": "2025-05-30T08:00:00Z",
      "stage": 6,
      "weapons": [
        1030,
        400,
        3020,
        2070
      ],
      "rareWeapons": []
    }
  ],
  "BigRun": [],
  "TeamContest": []
}
'''



# '''
# {
#   "Normal": [
#     {
#       "bigBoss": "SakelienGiant",
#       "rewardGear": {
#         "rewardId": "681f25f98e479642ada4748f",
#         "kind": "Clothes",
#         "id": 21012
#       },
#       "phaseId": "681f25f98e479642ada4748e",
#       "startTime": "2025-05-15T08:00:00Z",
#       "endTime": "2025-05-17T00:00:00Z",
#       "stage": 2,
#       "weapons": [
#         0,
#         30,
#         8020,
#         250
#       ],
#       "rareWeapons": []
#     },
#     {
#       "bigBoss": "SakeRope",
#       "rewardGear": {
#         "rewardId": "682158798e479642ada474ba",
#         "kind": "Head",
#         "id": 21016
#       },
#       "phaseId": "682158798e479642ada474b8",
#       "startTime": "2025-05-17T00:00:00Z",
#       "endTime": "2025-05-18T16:00:00Z",
#       "stage": 6,
#       "weapons": [
#         1000,
#         60,
#         4020,
#         -1
#       ],
#       "rareWeapons": []
#     },
#     {
#       "bigBoss": "SakeJaw",
#       "rewardGear": {
#         "rewardId": "682158798e479642ada474bb",
#         "kind": "Clothes",
#         "id": 21011
#       },
#       "phaseId": "682158798e479642ada474b9",
#       "startTime": "2025-05-18T16:00:00Z",
#       "endTime": "2025-05-20T08:00:00Z",
#       "stage": 4,
#       "weapons": [
#         4000,
#         1010,
#         7020,
#         2030
#       ],
#       "rareWeapons": []
#     },
#     {
#       "bigBoss": "SakelienGiant",
#       "rewardGear": {
#         "rewardId": "68238af98e479642ada474e5",
#         "kind": "Head",
#         "id": 21017
#       },
#       "phaseId": "68238af98e479642ada474e4",
#       "startTime": "2025-05-20T08:00:00Z",
#       "endTime": "2025-05-22T00:00:00Z",
#       "stage": 7,
#       "weapons": [
#         6030,
#         50,
#         100,
#         2060
#       ],
#       "rareWeapons": []
#     },
#     {
#       "bigBoss": "SakeRope",
#       "rewardGear": {
#         "rewardId": "6825bd798e479642ada4750f",
#         "kind": "Head",
#         "id": 21018
#       },
#       "phaseId": "6825bd798e479642ada4750e",
#       "startTime": "2025-05-22T00:00:00Z",
#       "endTime": "2025-05-23T16:00:00Z",
#       "stage": 9,
#       "weapons": [
#         1020,
#         200,
#         5020,
#         2000
#       ],
#       "rareWeapons": []
#     }
#   ],
#   "BigRun": [],
#   "TeamContest": []
# }
# '''

# '''
# {"Normal":[{"bigBoss":"SakeRope","rewardGear":{"rewardId":"681ac0f98e479642ada47434","kind":"Head","id":21012},"phaseId":"681ac0f98e479642ada47433","startTime":"2025-05-12T00:00:00Z","endTime":"2025-05-13T16:00:00Z","stage":1,"weapons":[6020,20,3030,7030],"rareWeapons":[]},{"bigBoss":"SakeJaw","rewardGear":{"rewardId":"681cf3798e479642ada4745e","kind":"Head","id":21014},"phaseId":"681cf3798e479642ada4745d","startTime":"2025-05-13T16:00:00Z","endTime":"2025-05-15T08:00:00Z","stage":4,"weapons":[40,1120,400,90],"rareWeapons":[]},{"bigBoss":"SakelienGiant","rewardGear":{"rewardId":"681f25f98e479642ada4748f","kind":"Clothes","id":21012},"phaseId":"681f25f98e479642ada4748e","startTime":"2025-05-15T08:00:00Z","endTime":"2025-05-17T00:00:00Z","stage":2,"weapons":[0,30,8020,250],"rareWeapons":[]},{"bigBoss":"SakeRope","rewardGear":{"rewardId":"682158798e479642ada474ba","kind":"Head","id":21016},"phaseId":"682158798e479642ada474b8","startTime":"2025-05-17T00:00:00Z","endTime":"2025-05-18T16:00:00Z","stage":6,"weapons":[1000,60,4020,-1],"rareWeapons":[]},{"bigBoss":"SakeJaw","rewardGear":{"rewardId":"682158798e479642ada474bb","kind":"Clothes","id":21011},"phaseId":"682158798e479642ada474b9","startTime":"2025-05-18T16:00:00Z","endTime":"2025-05-20T08:00:00Z","stage":4,"weapons":[4000,1010,7020,2030],"rareWeapons":[]}],"BigRun":[],"TeamContest":[]}
# '''



# ## Response headers
#  alt-svc: h3=":443"; ma=86400 
#  cf-cache-status: DYNAMIC 
#  cf-ray: 943d285cce524597-LHR 
#  content-encoding: zstd 
#  content-type: application/json 
#  date: Thu,22 May 2025 14:55:59 GMT 
#  etag: W/"cdea4837731e87d1e6137670fc3b32dcdaa649388fdc46f7d4aa00a66eb5d7e8_EUen" 
#  nel: {"success_fraction":0,"report_to":"cf-nel","max_age":604800} 
#  report-to: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v4?s=n838IpUzRmjDZw3%2F0m5EllvpVq69EivAHVoIOhbtw%2Blho1wzAmmi7zmfHVSR8DUr97rjafcT%2BYzcJ1bTHd1EUOuBUs%2B4bpVJCktgmZ5TlUOY60VBScts2TmJynPBGChCgFQDP1ZhUpW3%2Fw%3D%3D"}],"group":"cf-nel","max_age":604800} 
#  server: cloudflare 
#  server-timing: cfL4;desc="?proto=QUIC&rtt=9580&min_rtt=6796&rtt_var=4182&sent=14&recv=10&lost=0&retrans=1&sent_bytes=3827&recv_bytes=3448&delivery_rate=291053&cwnd=12000&unsent_bytes=0&cid=be655a7cf368b1f5&ts=249&x=80" 
#  strict-transport-security: max-age=15552000; includeSubDomains; preload 
#  x-content-type-options: nosniff 
#  x-rate-limit-limit: 1s 
#  x-rate-limit-remaining: 4 
#  x-rate-limit-reset: 2025-05-22T14:56:00.6407440Z 
