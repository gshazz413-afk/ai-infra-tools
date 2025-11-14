# REAL GPU MONITOR v2
# Uses nvidia-smi — works on real clusters
# Author: VB

import subprocess
import csv
import time
import datetime

def get_gpu_stats():
    try:
        # Get real GPU data
        temp = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"]
        ).decode().strip().split('\n')
        
        power = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=power.draw", "--format=csv,noheader,nounits"]
        ).decode().strip().split('\n')
        
        util = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"]
        ).decode().strip().split('\n')
        
        return [
            {
                'timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
                'gpu_id': i,
                'temp_C': temp[i].strip(),
                'power_W': power[i].strip(),
                'util_%': util[i].strip()
            }
            for i in range(len(temp))
        ]
    except Exception as e:
        print(f"Error: {e}")
        return []

# Log for 5 minutes
with open('real_gpu_log.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['timestamp', 'gpu_id', 'temp_C', 'power_W', 'util_%'])
    writer.writeheader()
    
    for _ in range(30):  # 30 x 10 sec = 5 min
        stats = get_gpu_stats()
        for row in stats:
            writer.writerow(row)
            print(f"GPU {row['gpu_id']}: {row['temp_C']}°C | {row['power_W']}W | {row['util_%']}%")
        time.sleep(10)

print("Real GPU log saved: real_gpu_log.csv")
