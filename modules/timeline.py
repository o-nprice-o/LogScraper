from collections import Counter
import matplotlib.pyplot as plt

def generate_timeline(events):
    timestamps = [
        e['timestamp'][:13]  # hourly granularity
        for e in events
        if e.get('timestamp')
    ]
    count_by_hour = Counter(timestamps)

    times = sorted(count_by_hour.keys())
    values = [count_by_hour[t] for t in times]

    plt.figure(figsize=(12, 5))
    plt.plot(times, values, marker='o')
    plt.xticks(rotation=45)
    plt.title('Log Events Over Time')
    plt.xlabel('Time (hour)')
    plt.ylabel('Event Count')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('timeline.png')
    print("[+] Timeline saved to timeline.png")
