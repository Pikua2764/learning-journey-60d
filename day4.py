import csv

def read_students_data(filename):
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

def calculate_average(subjects_dict):
    return sum(subjects_dict.values()) / len(subjects_dict)

def find_toppers(students, threshold=85):
    toppers = []
    for student in students:
        avg = calculate_average(student['subjects'])
        if avg > threshold:
            toppers.append({
                'name': student['name'],
                'average': avg
            })
    return toppers

def find_subject_toppers(students):
    subjects = ['math', 'science', 'english']
    subject_toppers = {}

    for subject in subjects:
        max_marks = 0
        topper = None
        for student in students:
            if student['subjects'][subject] > max_marks:
                max_marks = student['subjects'][subject]
                topper = student['name']
        subject_toppers[subject] = {'name': topper, 'marks': max_marks}
    return subject_toppers

def write_output(toppers, subject_toppers, filename='toppers.txt'):
    with open(filename, 'w') as file:
        file.write("STUDENTS WITH AVERAGE MARKS ABOVE 85:\n")
        file.write("=" * 35 + "\n")
        for topper in toppers:
            file.write(f"{topper['name']}: {topper['average']:.2f}\n")
        file.write("\nSUBJECT TOPPERS:\n")
        file.write("=" * 20 + "\n")
        for subject, data in subject_toppers.items():
            file.write(f"{subject.capitalize()}: {data['name']} ({data['marks']} marks)\n")

def main():
    students = read_students_data('students.csv')
    toppers = find_toppers(students)

    print("STUDENTS WITH AVERAGE MARKS ABOVE 85:")
    for topper in toppers:
        print(f"{topper['name']}: {topper['average']:.2f}")

    subject_toppers = find_subject_toppers(students)
    print("\nSUBJECT TOPPERS:")
    for subject, data in subject_toppers.items():
        print(f"{subject.capitalize()}: {data['name']} ({data['marks']} marks)")
    write_output(toppers, subject_toppers, 'toppers.txt')

if __name__ == "__main__":
    main()