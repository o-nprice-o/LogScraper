# LogScraper

LogScraper is a Python tool for parsing and analyzing system logs to detect suspicious activity such as failed logins, sudo commands, and brute force attempts. It supports regex-based pattern matching, optional GeoIP enrichment, event timeline visualization, and exports results in JSON or CSV formats.

## Features

- Parses system logs using customizable regex patterns.
- Analyzes login attempts and flags potential brute force attacks.
- Optional GeoIP lookup using the ip-api.com public API.
- Generates a timeline chart of log events over time.
- Exports results to timestamped JSON or CSV files in an `outputs/` directory.

## Usage

```
python LogScraper.py --logfile path/to/logfile --json --timeline --geoip
```

## Arguments

    --logfile (required): Path to the log file to analyze.

    --patterns: JSON file with regex patterns (default: patterns.json).

    --json: Output results as a timestamped JSON file in outputs/.

    --csv: Output results as a timestamped CSV file in outputs/.

    --timeline: Generate a timeline plot (timeline.png) of events.

    --geoip: Perform GeoIP lookup on flagged IPs.

    --min-failures: Minimum failed login attempts to flag as brute force (default: 5).

## Requirements

    Python 3.x

    requests library (pip install requests)

    matplotlib library (pip install matplotlib)

## Example

```
python LogScraper.py --logfile logs/sample_auth.log --json --timeline --geoip
```

Outputs a JSON report with geo-enriched flagged IPs and saves a timeline plot.
