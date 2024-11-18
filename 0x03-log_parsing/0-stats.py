#!/usr/bin/python3
"""Code"""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    """Main script logic."""
    total_size = 0
    status_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()

            # Skip invalid lines
            if len(parts) < 7 or not parts[-1].isdigit() or not parts[-2].isdigit():
                continue

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print stats on interruption
        print_stats(total_size, status_counts)
        raise

    # Print final stats
    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
