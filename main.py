from facepy import GraphAPI
import json
import os
from dotenv import load_dotenv

load_dotenv()

graph = GraphAPI(os.getenv('APP_TOKEN'))

#posts = graph.get('me/posts')

groupIDs = ("621862203973053") # group Ids

# In graph explorer, try to access group:
#   621862203973053/feed
# 
# I don't have permission.
#
# API docs: https://developers.facebook.com/docs/graph-api/reference/v22.0/group/feed

for gID in groupIDs:
    groupData = graph.get(gID + "/feed", page=True, retry=3, limit=500)
    for data in groupData:
        json_data=json.dumps(data, indent = 4,cls=DecimalEncoder)
        decoded_response = json_data.decode("UTF-8")
        data = json.loads(decoded_response)
        print("Paging group data...")

        for item in data["data"]:
            print("Paging group data...")