import re
import csv
import sys


def parse_log(file_path):
    with open(file_path, 'r') as f:
        log = f.read()

    matches = re.findall(
        r'(test_\w+)\[(\w+)\].*?Function make_post_request took (\d+\.\d+) s.*?(PASSED|Request failed, details: {\'error\': \'(.*?)\'}).*?',
        log, re.DOTALL)

    for match in matches:
        if 'Request failed' in match:
            print(match.replace('PASSED', 'FAILED'))

    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Test Name', 'Variant', 'Execution Time', 'Result', 'Details'])
        for match in matches:
            writer.writerow(match)


if __name__ == "__main__":
    parse_log(sys.argv[1])
