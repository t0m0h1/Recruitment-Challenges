import psutil

def get_cpu_temp():
    temp = psutil.sensors_temperatures()
    return temp['coretemp'][0].current

if __name__ == '__main__':
    print(get_cpu_temp())