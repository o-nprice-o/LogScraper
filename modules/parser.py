import re
import json
from datetime import datetime

def load_patterns(pattern_file):
    with open(pattern_file, 'r') as f:
        return json.load(f)

def parse_logs(logfile, pattern_file):
    patterns = load_patterns(pattern_file)
    events = []

    with open(logfile, 'r', errors='ignore') as f:
        for line in f:
            for event_type, regex in patterns.items():
                if event_type == 'timestamp':
                    continue
                match = re.search(regex, line)
                if match:
                    data = match.groupdict()
                    data['event_type'] = event_type
                    data['raw'] = line.strip()
                    data['timestamp'] = extract_timestamp(line, patterns.get('timestamp'))
                    events.append(data)
    return events

def extract_timestamp(line, timestamp_pattern):
    if not timestamp_pattern:
        return None
    match = re.search(timestamp_pattern, line)
    if match:
        ts = match.group('timestamp')
        try:
            return datetime.strptime(ts, '%b %d %H:%M:%S').replace(year=datetime.now().year).isoformat()
        except ValueError:
            return None
    return None
