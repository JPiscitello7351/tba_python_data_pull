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
        'X-TBA-Auth-Key': 'I1MLBtdsFA0kUBlum5sSYUbc3x3NXCYPXBFPhaQ8pezx4jTiflwgCeW2lRlQdiOD'
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
                              x.alliances.red.team_keys[0],x.alliances.red.team_keys[1],x.alliances.red.team_keys[2],
                              x.alliances.blue.team_keys[0],x.alliances.blue.team_keys[1],x.alliances.blue.team_keys[2],
                              x.score_breakdown['red']['autoChargeStationPoints'], x.score_breakdown['red']['autoChargeStationRobot1'], x.score_breakdown['red']['autoChargeStationRobot2'], x.score_breakdown['red']['autoChargeStationRobot3'],
                              x.score_breakdown['blue']['autoChargeStationPoints'], x.score_breakdown['blue']['autoChargeStationRobot1'], x.score_breakdown['blue']['autoChargeStationRobot2'], x.score_breakdown['blue']['autoChargeStationRobot3'],
                              x.score_breakdown['red']['mobilityRobot1'], x.score_breakdown['red']['mobilityRobot2'], x.score_breakdown['red']['mobilityRobot3'],
                              x.score_breakdown['blue']['mobilityRobot1'], x.score_breakdown['blue']['mobilityRobot2'], x.score_breakdown['blue']['mobilityRobot3'],
                              x.score_breakdown['red']['endGameBridgeState'], x.score_breakdown['red']['endGameChargeStationRobot1'], x.score_breakdown['red']['endGameChargeStationRobot2'], x.score_breakdown['red']['endGameChargeStationRobot3'],
                              x.score_breakdown['blue']['endGameBridgeState'], x.score_breakdown['blue']['endGameChargeStationRobot1'], x.score_breakdown['blue']['endGameChargeStationRobot2'], x.score_breakdown['blue']['endGameChargeStationRobot3'],
                              x.score_breakdown['red']['autoGamePieceCount'],x.score_breakdown['blue']['autoGamePieceCount'],x.score_breakdown['red']['teleopGamePieceCount'],x.score_breakdown['blue']['teleopGamePieceCount'],])


        #pprint(matchList)
        df = pd.DataFrame(matchList)
        df.to_csv("MatchList.csv")
        pprint("Done")

    except ApiException as e:
        print("Exception when calling MatchApi->get_event_matches: %s\n" % e)