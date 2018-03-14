'''Opens a new tab on the browser with the selected AWS service.'''

from albertv0 import *
import os
import re
from urllib.parse import urlencode

__iid__ = "PythonInterface/v0.1"
__prettyname__ = 'Aws Caller'
__version__ = '1.0'
__trigger__ = 'aws'
__author__ = '<Lucca Mendonça> lucca.mendonca@gmail.com'
__dependencies__ = []
__icon_path__ = os.path.dirname(__file__)+"/logo.svg"

def getServiceAndParams(query_string):
    query = re.split('\s+', query_string)
    response = {"service_name": query.pop(0),
                "query_string": ""}

    if len(query) == 0:
        return response

    query_params = {}

    for item in query:
        if ':' not in item:
            continue
        param=re.split(':', item)
        if len(param[1]) == 0 or len(param[0]) == 0:
            continue
        query_params[param[0]] = param[1]

    if len(query_params) > 0:
        response["query_string"] = "?"+urlencode(query_params)

    return response

def handleQuery(query):
    if not query.isTriggered:
        return

    params = getServiceAndParams(query.string.strip())
    aws_url = "https://console.aws.amazon.com/" + params["service_name"] + params["query_string"]
    item = Item(id=__prettyname__,
                icon=__icon_path__,
                completion=query.rawString,
                text="AWS",
                subtext="Opens an AWS service console page for the given name",
                actions=[UrlAction(text="Open", url=aws_url)]
            )

    return [item]
