"""
Day 5: Using the grades module to analyze student performance.
"""

from grades import read_students, student_averages, high_achievers, subject_toppers, write_dict_to_file

def main():
    # Load student data
    students = read_students('students.csv')
    print(f"Loaded data for {len(students)} students\n")
    
    # Calculate averages for each student
    averages = student_averages(students)
    print("STUDENT AVERAGES:")
    print("=" * 17)
    for name, avg in averages.items():
        print(f"{name}: {avg:.2f}")
    
    # Find high achievers (above 85)
    achievers = high_achievers(averages, 85.0)
    print("\nHIGH ACHIEVERS (Above 85):")
    print("=" * 26)
    for name, avg in achievers.items():
        print(f"{name}: {avg:.2f}")
    
    # Find subject toppers
    toppers = subject_toppers(students)
    print("\nSUBJECT TOPPERS:")
    print("=" * 15)
    for subject, data in toppers.items():
        print(f"{subject.capitalize()}: {data['name']} ({data['marks']} marks)")
    
    # Write results to file
    # Clear the file first
    with open('results.txt', 'w') as f:
        f.write("STUDENT PERFORMANCE ANALYSIS\n")
        f.write("=" * 28 + "\n")
    
    # Write each section
    write_dict_to_file(averages, 'results.txt', 'Student Averages')
    write_dict_to_file(achievers, 'results.txt', 'High Achievers (Above 85)')
    write_dict_to_file(toppers, 'results.txt', 'Subject Toppers')
    
    print(f"\nResults saved to 'results.txt'")

if __name__ == "__main__":
    main()