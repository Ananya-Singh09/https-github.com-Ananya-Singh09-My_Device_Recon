import nmap # type: ignore
import datetime
import db

DEVICE_IP = "127.0.0.1"   # Scan your own machine

def run_scan():
    nm = nmap.PortScanner()
    print(f"Starting scan on {DEVICE_IP}...")

    nm.scan(DEVICE_IP, '1-1024')

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    scan_id = db.add_scan(time)

    for proto in nm[DEVICE_IP].all_protocols():
        ports = nm[DEVICE_IP][proto].keys()
        for port in ports:
            state = nm[DEVICE_IP][proto][port]['state']
            service = nm[DEVICE_IP][proto][port].get('name', '')
            db.add_port(scan_id, port, state, service)

    print(f"Scan completed. Saved scan ID: {scan_id}")

if __name__ == "__main__":
    run_scan()

