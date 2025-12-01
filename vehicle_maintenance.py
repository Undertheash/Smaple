# vehicle_maintenance.py

def calc_total_cost(records):
    """
    REQ-01:
    Calculate total maintenance cost.
    Each record: {"vehicle": "...", "cost": X, "duration": Y, "completed": True/False}
    Return float.
    If list is empty, return 0.
    """
    # Add your implementation here
    cost = 0 
    if len(records) == 0:
        return 0
    for item in records:
        cost += item['cost']
    return cost



def calc_average_duration(records):
    """
    REQ-02:
    Compute average maintenance duration.
    Return value rounded to 1 decimal place.
    If list is empty, return None.
    """
    # Add your implementation here
    average = 0
    total_duration=0
    if len(records) == 0:
        return None
    for item in records:
        total_duration+= item['duration']
    average = total_duration/len(records)
    average = round(average,1)
    return average


def find_highest_cost_record(records):
    """
    REQ-03:
    Return the record dict with the highest maintenance cost.
    If list is empty, return None.
    """
    # Add your implementation here
    if len(records) == 0:
        return None
    longest = records[0]
    for item in records:
        if item['cost'] > longest['cost']:
            longest = item
    return longest


def count_pending(records):
    """
    REQ-04:
    Count number of vehicles where completed == False.
    Return integer.
    If list is empty, return 0.
    """
    # Add your implementation here
    count = 0
    for item in records:
        if item['completed'] == False:
            count += 1
    return count
    


def filter_cost_above(records, threshold):
    """
    REQ-05:
    Return list of records where cost > threshold.
    If none match, return [].
    """
    # Add your implementation here
    result =[]
    for item in records:
        if item['cost'] > threshold:
            result.append(item)
    return result
