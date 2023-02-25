# Define the data structures
core_courses = {}

# Define the functions
def add_course(course_code, course_name, course_description, credit_hours):
    core_courses[course_code] = {
        'name': course_name,
        'description': course_description,
        'credit_hours': credit_hours
    }

def remove_course(course_code):
    del core_courses[course_code]

def update_course(course_code, course_name=None, course_description=None, credit_hours=None):
    if course_code in core_courses:
        if course_name:
            core_courses[course_code]['name'] = course_name
        if course_description:
            core_courses[course_code]['description'] = course_description
        if credit_hours:
            core_courses[course_code]['credit_hours'] = credit_hours

def get_course(course_code):
    return core_courses.get(course_code)

# Define the user interface
while True:
    print('Scheme of Study Manager - Core Courses')
    print('1. Add course')
    print('2. Remove course')
    print('3. Update course')
    print('4. Get course information')
    print('5. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        course_code = input('Enter course code: ')
        course_name = input('Enter course name: ')
        course_description = input('Enter course description: ')
        credit_hours = input('Enter credit hours: ')
        add_course(course_code, course_name, course_description, credit_hours)
    elif choice == '2':
        course_code = input('Enter course code: ')
        remove_course(course_code)
    elif choice == '3':
        course_code = input('Enter course code: ')
        course_name = input('Enter new course name (leave blank to skip): ')
        course_description = input('Enter new course description (leave blank to skip): ')
        credit_hours = input('Enter new credit hours (leave blank to skip): ')
        update_course(course_code, course_name, course_description, credit_hours)
    elif choice == '4':
        course_code = input('Enter course code: ')
        course = get_course(course_code)
        if course:
            print('Course Name:', course['name'])
            print('Course Description:', course['description'])
            print('Credit Hours:', course['credit_hours'])
        else:
            print('Course not found')
    elif choice == '5':
        break
    else:
        print('Invalid choice')
