# sensor_monitoring.py

def get_max_temperature(records):
    """
    REQ-01:
    Return the record dict with the highest temperature.
    Each record: {"timestamp": "...", "temperature": X}
    If list is empty, return None.
    """
    if len(records) == 0:
        return None
    highest = records[0]
    for item in records:
        if item['temperature'] > highest['temperature']: 
            highest = item
    return highest


def get_min_temperature(records):
    """
    REQ-02:
    Return the record dict with the lowest temperature.
    If list is empty, return None.
    """
    # Add your implementation here
    if len(records) == 0:
        return None
    lowest = records[0]
    for item in records:
        if item['temperature'] < lowest['temperature']: 
            lowest = item
    return lowest

def compute_avg_temperature(records):
    """
    REQ-03:
    Compute the average temperature as a float.
    If list is empty, return None.
    """
    # Add your implementation here
    if len(records) == 0:
        return None
    total = 0
    average = 0 
    for item in records:
        total += item['temperature']
    average = total / len(records)  
    average = round(average, 1)  
    return average


def detect_temperature_alerts(records):
    """
    REQ-04:
    Return a list of record dicts where temperature > 50°C.
    If none exceed 50°C, return [].
    """
    # Add your implementation here
    result = []
    for item in records:
        if item['temperature'] > 50:
            result.append(item)
    return result
