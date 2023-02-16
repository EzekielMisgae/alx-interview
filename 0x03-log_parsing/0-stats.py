#!/usr/bin/env python3

import sys

# Define the possible status codes
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize the metrics
total_size = 0
status_code_counts = {code: 0 for code in STATUS_CODES}

# Read input line by line and compute metrics
line_count = 0
for line in sys.stdin:
    # Parse the input line
    try:
        ip, date, request, status_code, file_size = line.split(' ')
        status_code = int(status_code)
        file_size = int(file_size)
        # We only count lines with the correct format
        if request != 'GET /projects/260 HTTP/1.1':
            continue
    except ValueError:
        # Skip lines with incorrect format
        continue
    
    # Update the metrics
    total_size += file_size
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1
    
    line_count += 1
    
    # Print the metrics every 10 lines
    if line_count % 10 == 0:
        print(f'Total file size: {total_size}')
        for code in sorted(status_code_counts):
            if status_code_counts[code] > 0:
                print(f'{code}: {status_code_counts[code]}')
        print()
        
# Print the final metrics
print(f'Total file size: {total_size}')
for code in sorted(status_code_counts):
    if status_code_counts[code] > 0:
        print(f'{code}: {status_code_counts[code]}')
