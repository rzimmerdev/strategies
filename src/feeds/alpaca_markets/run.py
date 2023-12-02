import os

import dxlib as dx
from dxlib import info_logger
from dxlib.managers import FeedManager

from dotenv import load_dotenv

load_dotenv()


def main():
    logger = info_logger("alpaca-markets-feed")
    market = dx.markets.sandbox
    feed = FeedManager(None, port=os.environ.get("WEBSOCKET_PORT", None), logger=logger)
    feed.start()



    logger.info("Feed manager is running. Press Ctrl+C to stop...")

    try:
        wss_client.run()
    except KeyboardInterrupt:
        wss_client.close()
    finally:
        feed.stop()
        logger.info("Feed manager has been shutdown.")


if __name__ == "__main__":
    main()
