import psutil

def get_cpu_temperature():
    try:
        temperature = psutil.sensors_temperatures()['coretemp'][0].current
        return temperature
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    cpu_temperature = get_cpu_temperature()

    if cpu_temperature is not None:
        print(f"CPU Temperature: {cpu_temperature}°C")
    else:
        print("Failed to retrieve CPU temperature.")


