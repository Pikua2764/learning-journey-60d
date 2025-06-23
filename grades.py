"""
Grades module for student performance analysis.
Provides functions to read student data, calculate averages, find high achievers, and subject toppers.
"""

import csv
from typing import List, Dict, Any

def read_students(filename: str) -> List[Dict[str, Any]]:
    """
    Read student data from CSV file.
    
    Args:
        filename: Path to CSV file with student data
        
    Returns:
        List of dictionaries containing student names and subject marks
    """
    students = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                'name': row['name'],
                'subjects': {
                    'math': int(row['math']),
                    'science': int(row['science']),
                    'english': int(row['english'])
                }
            }
            students.append(student)
    return students

def student_averages(students: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate average marks for each student.
    
    Args:
        students: List of student dictionaries
        
    Returns:
        Dictionary mapping student names to their average marks
    """
    averages = {}
    for student in students:
        subjects = student['subjects']
        avg = sum(subjects.values()) / len(subjects)
        averages[student['name']] = avg
    return averages

def high_achievers(averages: Dict[str, float], threshold: float = 85.0) -> Dict[str, float]:
    """
    Find students with averages above the threshold.
    
    Args:
        averages: Dictionary of student names and their averages
        threshold: Minimum average required (default: 85.0)
        
    Returns:
        Dictionary of high achievers and their averages
    """
    return {name: avg for name, avg in averages.items() if avg > threshold}

def subject_toppers(students: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Find the highest scorer in each subject.
    
    Args:
        students: List of student dictionaries
        
    Returns:
        Dictionary mapping subjects to their toppers (name and marks)
    """
    subjects = ['math', 'science', 'english']
    toppers = {}
    
    for subject in subjects:
        max_marks = 0
        topper_name = None
        
        for student in students:
            marks = student['subjects'][subject]
            if marks > max_marks:
                max_marks = marks
                topper_name = student['name']
        
        toppers[subject] = {'name': topper_name, 'marks': max_marks}
    
    return toppers

def write_dict_to_file(data: Dict[str, Any], filename: str, title: str = "Results") -> None:
    """
    Write dictionary data to a text file with formatting.
    
    Args:
        data: Dictionary to write
        filename: Output file name
        title: Title for the output section
    """
    with open(filename, 'a') as file:
        file.write(f"\n{title.upper()}:\n")
        file.write("=" * len(title) + "\n")
        
        for key, value in data.items():
            if isinstance(value, dict):
                # Handle nested dictionaries (like subject toppers)
                file.write(f"{key.capitalize()}: {value['name']} ({value['marks']} marks)\n")
            elif isinstance(value, float):
                # Handle float values (like averages)
                file.write(f"{key}: {value:.2f}\n")
            else:
                file.write(f"{key}: {value}\n")
        file.write("\n")