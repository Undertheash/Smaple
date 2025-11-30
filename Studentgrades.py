# student_grades.py

def calc_average_score(students):
    """
    REQ-01:
    Calculate the average score of all students.
    Return a float.
    If list is empty, return None.
    """
    # Add your implementation here
    if len(students) == 0:
        return None
    average = 0 
    total = 0
    for item in students:
        total += item['score']

    average = total / len(students)
    return average
    
    


def get_highest_scoring_student(students):
    """
    REQ-02:
    Return the student dictionary with the highest score.
    Example student dict: {"name": "Alex", "score": 82}
    If list is empty, return None.
    """
    # Add your implementation here
    if len(students) ==0:
        return None
    longest = students[0]
    for item in students:
        if item['score'] > longest['score']:
            longest = item
        
    return longest



def count_passed_students(students):
    """
    REQ-03:
    Count how many students passed.
    Passing criteria: score >= 50
    Return integer count.
    """
    # Add your implementation here
    passed = 0
    
    for item in students:
        if item['score'] >= 50:
            passed += 1

    return passed



def get_students_below_50(students):
    """
    REQ-04:
    Return a list of student dictionaries where score < 50.
    If none found, return empty list [].
    """
    # Add your implementation here
    result = []
    for item in students:
        if item['score'] < 50:
            result.append(item)
    return result
