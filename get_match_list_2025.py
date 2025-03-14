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
    event_key = '2025mose' # str | TBA Event Key, eg `2016nytr`
    if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)
    last_complete_qual_match = 49

    try:
        api_response = api_instance.get_event_matches(event_key)
        #pprint(api_response)
        matchList = []
        for x in api_response:
            if (x.comp_level == "qm" and x.match_number < last_complete_qual_match):
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
                              ])

        #pprint(matchList)
        df = pd.DataFrame(matchList)
        df.to_csv("MatchList.csv")
        pprint("Done")

    except ApiException as e:
        print("Exception when calling MatchApi->get_event_matches: %s\n" % e)