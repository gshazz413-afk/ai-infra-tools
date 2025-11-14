# AI INFRA TOOL: GPU Cluster Dashboard (Simulation)
# Author: VB

import time
import pandas as pd
import matplotlib.pyplot as plt
import random

print("Starting GPU cluster simulation...")

# Simulate 8 GPUs
data = []
for minute in range(30):
    for gpu in range(8):
        data.append({
            'time': minute,
            'gpu': f'GPU-{gpu}',
            'temp': random.randint(50, 85),
            'power': random.randint(200, 350),
            'util': random.randint(30, 100)
        })
    time.sleep(0.1)

df = pd.DataFrame(data)

# Save CSV
df.to_csv('gpu_log.csv', index=False)
print("Log saved: gpu_log.csv")

# Plot temperature
plt.figure(figsize=(10,6))
for gpu in df['gpu'].unique():
    subset = df[df['gpu'] == gpu]
    plt.plot(subset['time'], subset['temp'], label=gpu)
plt.title("8-GPU Cluster – Temperature (30 min)")
plt.xlabel("Time (min)")
plt.ylabel("Temp (°C)")
plt.legend()
plt.tight_layout()
plt.savefig('gpu_dashboard.png')
plt.show()

print("Graph saved: gpu_dashboard.png")
print("All done! Push to GitHub.")
