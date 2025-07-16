from collections import Counter

def analyze_events(events, min_failures=5):
    failed_ips = [e['ip'] for e in events if e['event_type'] == 'failed_login' and 'ip' in e]
    brute_ips = [ip for ip, count in Counter(failed_ips).items() if count >= min_failures]

    summary = {
        "failed_logins": len([e for e in events if e['event_type'] == 'failed_login']),
        "accepted_logins": len([e for e in events if e['event_type'] == 'accepted_login']),
        "sudo_commands": len([e for e in events if e['event_type'] == 'sudo']),
        "brute_force_ips": brute_ips
    }

    return summary, brute_ips
