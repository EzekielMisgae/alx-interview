#!/usr/bin/env python3
import random
import datetime
import sys
from time import sleep

for i in range(10000):
    sleep(random.random())
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    date = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    log_line = f"{ip_address} - [{date}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}\n"
    sys.stdout.write(log_line)
    sys.stdout.flush()