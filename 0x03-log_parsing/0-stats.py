import sys
import signal

total_file_size = 0
status_code_counts = {}

# Handler function for keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Print the current statistics
def print_stats():
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_counts.keys()):
        print(f'{code}: {status_code_counts[code]}')

# Register the handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for i, line in enumerate(sys.stdin):
    # Parse the line
    parts = line.split()
    if len(parts) != 7:
        continue
    ip, date, _, path, status, size, _ = parts
    if path != '/projects/260':
        continue
    try:
        size = int(size)
        status = int(status)
    except ValueError:
        continue
    # Update the statistics
    total_file_size += size
    status_code_counts[status] = status_code_counts.get(status, 0) + 1
    # Print the statistics after every 10 lines
    if (i + 1) % 10 == 0:
        print_stats()