# auto.py
from apscheduler.schedulers.blocking import BlockingScheduler # type: ignore
import scanner

sched = BlockingScheduler()

# run every 5 minutes (change as needed)
@sched.scheduled_job('interval', minutes=5)
def job():
    print("Scheduled scan job running...")
    scanner.scan_device()

if __name__ == "__main__":
    print("Starting scheduler. Press Ctrl+C to stop.")
    sched.start()
