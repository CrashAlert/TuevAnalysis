import numpy as np

class SensorData(object):
    def __init__(self, x, y, z, gps, time, alert):
        self.x = x
        self.y = y
        self.z = z
        self.speed = gps
        self.time = self.to_secs(time)
        self.alerts = alert
        
    def gyro_force(self):
        rms = self.x ** 2 + self.y ** 2 + self.z ** 2
        return np.sqrt(rms)
    
    def gyro_sum(self):
        return self.x + self.y + self.z
    
    def gyro_abs_sum(self):
        return np.abs(self.x) + np.abs(self.y) + np.abs(self.z)
    
    @classmethod
    def to_secs(cls, t):
        h = int(t[:2])
        m = int(t[3:5])
        s = int(t[6:])
        return 60 ** 2 * h + 60 * m + s