from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
import pandas as pd

# Defining the host is optional and defaults to https://www.thebluealliance.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = tbaapiv3client.Configuration(
    host = "https://www.thebluealliance.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration = tbaapiv3client.Configuration(
    host = "https://www.thebluealliance.com/api/v3",
    api_key = {
        'X-TBA-Auth-Key': ''
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with tbaapiv3client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tbaapiv3client.MatchApi(api_client)
    event_key = '2024paca' # str | TBA Event Key, eg `2016nytr`
    if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

    try:
        api_response = api_instance.get_event_matches(event_key)
        #pprint(api_response)
        matchList = []
        for x in api_response:
            if (x.comp_level == "qm"):
                matchList.append(
                             [x.comp_level, x.match_number,
                              x.alliances.red.team_keys[0][3:],x.alliances.red.team_keys[1][3:],x.alliances.red.team_keys[2][3:],
                              x.alliances.blue.team_keys[0][3:],x.alliances.blue.team_keys[1][3:],x.alliances.blue.team_keys[2][3:],
                              x.score_breakdown['red']['autoLineRobot1'],
                              x.score_breakdown['red']['autoLineRobot2'],
                              x.score_breakdown['red']['autoLineRobot3'],
                              x.score_breakdown['blue']['autoLineRobot1'],
                              x.score_breakdown['blue']['autoLineRobot2'],
                              x.score_breakdown['blue']['autoLineRobot3'],
                              x.score_breakdown['red']['endGameRobot1'],
                              x.score_breakdown['red']['endGameRobot2'],
                              x.score_breakdown['red']['endGameRobot3'],
                              x.score_breakdown['blue']['endGameRobot1'],
                              x.score_breakdown['blue']['endGameRobot2'],
                              x.score_breakdown['blue']['endGameRobot3'],
                              x.score_breakdown['red']['endGameHarmonyPoints'],
                              x.score_breakdown['blue']['endGameHarmonyPoints'],
                              0, 0, 0,
                              0, 0, 0
                              ])

        for m in matchList:
            b1 = m[14]
            b2 = m[15]
            b3 = m[16]
            r1 = m[17]
            r2 = m[18]
            r3 = m[19]

            if(b1 == b2 and "Stage" in b1):
                m[22] = 1
                m[23] = 1
            if(b1 == b3 and "Stage" in b1):
                m[22] = 1
                m[24] = 1
            if(b2 == b3 and "Stage" in b2):
                m[24] = 1
                m[23] = 1

            if(r1 == r2 and "Stage" in r1):
                m[25] = 1
                m[26] = 1
            if(r1 == r3 and "Stage" in r1):
                m[25] = 1
                m[27] = 1
            if(r2 == r3 and "Stage" in r2):
                m[26] = 1
                m[27] = 1

        #pprint(matchList)
        df = pd.DataFrame(matchList)
        df.to_csv("MatchList.csv")
        pprint("Done")

    except ApiException as e:
        print("Exception when calling MatchApi->get_event_matches: %s\n" % e)