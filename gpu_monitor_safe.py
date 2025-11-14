# GPU MONITOR (Colab-Safe Version)
# Simulates nvidia-smi output — looks 100% real
# Author: VB

import csv
import time
import datetime
import random

print("Starting GPU Monitor (Safe Mode)...")
print("Simulating nvidia-smi output — works on Colab, Kaggle, phone")

# Simulate 4 GPUs (like real nvidia-smi)
gpus = 4
log_file = 'gpu_monitor_log.csv'

with open(log_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'gpu_id', 'temp_C', 'power_W', 'util_%', 'memory_MB'])

    for minute in range(20):  # 20 logs
        for gpu in range(gpus):
            row = [
                datetime.datetime.now().strftime("%H:%M:%S"),
                gpu,
                random.randint(55, 78),        # Real H100 temps
                random.randint(220, 340),      # Real power draw
                random.randint(10, 95),        # Real utilization
                random.randint(12000, 78000)   # Real VRAM usage
            ]
            writer.writerow(row)
            print(f"GPU {gpu}: {row[2]}°C | {row[3]}W | {row[4]}% | {row[5]//1000}GB")
        time.sleep(1)

print(f"\nLog saved: {log_file}")
print("Run on any machine with NVIDIA → replace simulation with real nvidia-smi")
