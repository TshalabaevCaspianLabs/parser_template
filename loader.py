import asyncio

import requests

from utils.logging import logger

asinc = asyncio
session = requests.Session()
logger.info('START PARSER')

asinc.get_event_loop()
