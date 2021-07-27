import asyncio
import sys


# #python36 mitmproxy==5.0.0
if sys.platform == 'win32':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())