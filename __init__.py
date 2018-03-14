'''Opens a new tab on the browser with the selected AWS service.'''

from albertv0 import *
import os

__iid__ = "PythonInterface/v0.1"
__prettyname__ = 'Aws Caller'
__version__ = '1.0'
__trigger__ = 'aws'
__author__ = '<Lucca Mendonça> lucca.mendonca@gmail.com'
__dependencies__ = []
__icon_path__ = os.path.dirname(__file__)+"/logo.svg"

def handleQuery(query):
    if not query.isTriggered:
        return

    service_name = query.string.strip()

    aws_url = "https://console.aws.amazon.com/" + service_name

    item = Item(id=__prettyname__,
                icon=__icon_path__,
                completion=query.rawString,
                text="AWS",
                subtext="Opens an AWS service console page for the given name",
                actions=[UrlAction(text="Open", url=aws_url)]
            )

    return [item]
