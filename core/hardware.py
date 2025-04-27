import psutil
import platform
from datetime import datetime

class HardwareMonitor:
    def __init__(self):
        self.update()
        
    def update(self):
        self.cpu_usage = psutil.cpu_percent(interval=1)
        self.memory_usage = psutil.virtual_memory().percent
        try:
            self.battery = psutil.sensors_battery()
        except:
            self.battery = None
        self.last_update = datetime.now()
            
    def get_full_info(self, language="en"):
        self.update()
        
        info = {
            "System": platform.system(),
            "Processor": platform.processor(),
            "CPU Usage": f"{self.cpu_usage}%",
            "Memory Usage": f"{self.memory_usage}%",
            "Battery": f"{self.battery.percent}%" if self.battery else "N/A",
            "Last Update": self.last_update.strftime("%H:%M:%S")
        }
        
        if language == "id":
            return "\n".join([f"{k}: {v}" for k, v in info.items()])
        return "\n".join([f"{k}: {v}" for k, v in info.items()])
    
    def get_short_status(self):
        self.update()
        return (f"CPU: {self.cpu_usage}% | "
                f"Memory: {self.memory_usage}% | "
                f"Battery: {self.battery.percent if self.battery else 100}%")