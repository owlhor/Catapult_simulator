import math

class XDisToSpringDis():
    g = 9.81
    mass = 0.1 # น้ำหนัก หน่วยเป็น Kg
    u = 0.2  # สัมประสิทธิแรงเสียดทาน
    def __init__(self,xdistance,ydistance,theta,Kspring): #Input ระยะทาง X ที่ต้องการ / ความสูงระหว่างปลายกระบอกกับตะกร้า / มุม (ยึด 45 องศา) / ค่า KSpring
        self.xdistance = xdistance
        self.ydistance = ydistance
        self.theta = math.radians(theta)  # แปลง 45 องศา เป็น เรเดียน
        self.Kspring = Kspring

    def XStimecal(self):
        self.time = math.sqrt(((4*math.tan(self.theta))-(self.ydistance))/self.g)  # คำนวนเวลาที่ต้องการ
        return self.time

    def XSvelocitycal(self):
        self.velocity = self.xdistance / (self.time * math.cos(self.theta))  # คำนวนความเร็วเริ่มต้นของลูก
        return self.velocity

    def XSpullingcal(self):
        self.x = 2 * self.g * (math.sin(self.theta) + self.u * math.cos(self.theta))  # รวมสมการ มันยาวเกินไป
        self.pulling_distance1 = (self.x + math.sqrt((self.x ** 2) + (4 * (self.Kspring / self.mass) * (self.velocity ** 2)))) / (2 * self.Kspring / self.mass)  # คำนวนหาระยะหดสปริง
        self.pulling_distance2 = (self.x - math.sqrt((self.x ** 2) + (4 * (self.Kspring / self.mass) * (self.velocity ** 2)))) / (2 * self.Kspring / self.mass)  # คำนวนหาระยะหดสปริง
        if self.pulling_distance1 < 0:
            return self.pulling_distance2
        else:
            return self.pulling_distance1

class SpringDisToXDis():
    g = 9.8
    mass = 0.1  # น้ำหนัก หน่วยเป็น Kg
    u = 0.2  # สัมประสิทธิแรงเสียดทาน
    def __init__(self,ydistance,pulling_distance,theta,Kspring): #Input รความสูงระหว่างปลายกระบอกกับตะกร้า / ระยะหดสปริง / มุม (ยึด 45 องศา) / ค่า KSpring
        self.pulling_distance = pulling_distance
        self.theta = math.radians(theta)
        self.Kspring = Kspring
        self.ydistance = ydistance

    def SXvelocitycal(self):
        self.x = 2 * self.g * self.pulling_distance * (math.sin(self.theta) + (self.u * math.cos(self.theta)))  # รวมสมการ มันยาวเกินไป
        self.velocity = math.sqrt(((self.Kspring * (self.pulling_distance**2))/self.mass)-(self.x))
        return self.velocity

    def SXtimecal(self):
        self.time1 = ((self.velocity * math.sin(self.theta)) + math.sqrt((self.velocity * math.sin(self.theta))**2)-(4 * (0.5 * self.g * self.ydistance))) / (2 * 0.5 * self.g)
        self.time2 = ((self.velocity * math.sin(self.theta)) - math.sqrt((self.velocity * math.sin(self.theta)) ** 2) - (4 * (0.5 * self.g * self.ydistance))) / (2 * 0.5 * self.g)
        if self.time1 < 0:
            self.time = self.time2
            return self.time
        else:
            self.time = self.time1
            return self.time

    def SXxdistancecal(self):
        self.xdistance = self.velocity * math.cos(self.theta) * self.time
        return self.xdistance
