#Jangan edit kode ni

import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logging.info("+ Bot Online Now")

start_time = time.time()

uptime = time.time() - start_time
hours, rem = divmod(uptime, 3600)
minutes, seconds = divmod(rem, 60)

logging.info(f"Uptime: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
