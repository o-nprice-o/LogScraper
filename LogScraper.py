import argparse
import os
import datetime
from modules.parser import parse_logs
from modules.analyzer import analyze_events
from modules.geoip import enrich_with_geoip
from modules.timeline import generate_timeline
from modules.exporter import export_results


def get_timestamped_filename(basename):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{timestamp}_{basename}"

def main():
    parser = argparse.ArgumentParser(description="LogScraper - Parse and analyze system logs.")
    parser.add_argument("--logfile", required=True, help="Path to the log file")
    parser.add_argument("--patterns", default="patterns.json", help="Regex patterns file")
    parser.add_argument("--json", help="Output JSON file")
    parser.add_argument("--csv", help="Output CSV file")
    parser.add_argument("--timeline", action="store_true", help="Generate event timeline")
    parser.add_argument("--geoip", action="store_true", help="Enable GeoIP lookup via ip-api.com")
    parser.add_argument("--min-failures", type=int, default=5, help="Brute force threshold")
    args = parser.parse_args()

    # Step 1: Parse the logs
    events = parse_logs(args.logfile, args.patterns)

    # Step 2: Analyze for suspicious activity
    summary, flagged_ips = analyze_events(events, args.min_failures)

    # Step 3: Optional GeoIP lookup via public API
    if args.geoip:
        enrich_with_geoip(events, flagged_ips)

    # Step 4: Optional timeline generation
    if args.timeline:
        generate_timeline(events)

    # Step 5: Export
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)  # create folder if needed

    if args.json:
        filename = get_timestamped_filename("output.json")
        output_path = os.path.join(output_dir, filename)
        export_results(events, summary, output_path, fmt="json")

    if args.csv:
        filename = get_timestamped_filename("output.csv")
        output_path = os.path.join(output_dir, filename)
        export_results(events, summary, output_path, fmt="csv")

    # Print summary
    print("\n=== Analysis Summary ===")
    for k, v in summary.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()