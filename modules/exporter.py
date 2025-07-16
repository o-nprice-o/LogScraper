import json
import csv

def export_results(events, summary, output_file, fmt='json'):
    if fmt == 'json':
        with open(output_file, 'w') as f:
            json.dump({"summary": summary, "events": events}, f, indent=2)
    elif fmt == 'csv':
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['timestamp', 'event_type', 'user', 'ip'])
            writer.writeheader()
            for e in events:
                writer.writerow({
                    'timestamp': e.get('timestamp', ''),
                    'event_type': e.get('event_type', ''),
                    'user': e.get('user', ''),
                    'ip': e.get('ip', '')
                })
