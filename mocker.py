import random
import string
import json


def main():
    '''Generate mock data and write to json file'''
    # Variables
    file_name = 'data'
    domain = 'sunway.edu.my'
    semester = '2018-03-26'
    length_of_lecturer_id = 5
    number_of_lecturers = 15
    subjects_per_lecturer = (0, 2)
    students_per_subject = (5, 100)
    class_limits = {
        'Lecture': 50,
        'Practical': 30
    }
    max_subjects_per_student = 4
    # Totals
    totals = {
        'lecturers': number_of_lecturers,
        'subjects': 0,
        'classes': 0,
        'students': 0
    }
    # Emails
    print('Generating emails...', end=' ', flush=True)
    emails = []
    for _ in range(number_of_lecturers):
        while True:
            id_ = ''.join([random.choice(list(string.ascii_lowercase))
                           for _ in range(length_of_lecturer_id)])
            email = '{}@{}'.format(id_, domain)
            if email not in emails:
                break
        emails.append(email)
    print('Done!')
    # Subjects
    data = {}
    all_codes = []
    print('Generating subjects...', end=' ', flush=True)
    for email in emails:
        subjects = []
        for _ in random_range(subjects_per_lecturer):
            while True:
                code = '{}{}{}'.format(
                    ''.join(random.sample(set(string.ascii_uppercase), 3)),
                    random.randint(1, 3),
                    ''.join([str(random.randint(0, 9)) for _ in range(3)])
                )
                if code not in all_codes:
                    all_codes.append(code)
                    break
            subject = {
                'code': code,
                'classes': []
            }
            subjects.append(subject)
            totals['subjects'] += 1
        content = {
            'semester': semester,
            'subjects': subjects
        }
        data[email] = content
    print('Done!')
    # Classes
    print('Generating classes...', end=' ', flush=True)
    all_students = {}
    for email, content in data.items():
        for subject in content['subjects']:
            # Generate students for subject
            subject_students = []
            for _ in random_range(students_per_subject):
                # Try to use existing students
                keys = list(all_students.keys())
                random.shuffle(keys)
                for key in keys:
                    if key not in subject_students and \
                       all_students[key] < max_subjects_per_student:
                        student = key
                        all_students[key] += 1
                        break
                else:
                    # If not, generate new student
                    student = '1{}{}'.format(
                        random.randint(3, 5),
                        ''.join([str(random.randint(0, 9)) for _ in range(6)])
                    )
                    all_students[student] = 1
                subject_students.append(student)
            # Assign students to classes
            for category, max_students in class_limits.items():
                random.shuffle(subject_students)
                chunks = list(create_chunks(subject_students, max_students))
                random.shuffle(chunks)
                for i, chunk in enumerate(chunks):
                    class_ = {
                        'category': category,
                        'group': i+1,
                        'students': chunk
                    }
                    subject['classes'].append(class_)
                    totals['classes'] += 1
    totals['students'] = len(list(all_students.keys()))
    print('Done!')
    # Write file
    print('Writing to file...', end=' ', flush=True)
    with open('{}.json'.format(file_name), 'w') as file:
        file.write(json.dumps(data, indent=4))
        file.write('\n')
    print('Done!')
    # Print totals
    for key, value in totals.items():
        print('Total {}: {}'.format(key, value))


def random_range(range_):
    '''Return range generator up to random integer given minimum and maximum'''
    random_integer = random.randint(range_[0], range_[1])
    return range(random_integer)


def create_chunks(chunkable, n):
    '''Return max-n size chunks from list'''
    for i in range(0, len(chunkable), n):
        yield chunkable[i:i+n]


if __name__ == '__main__':
    main()
