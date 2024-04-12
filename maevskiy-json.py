employee_data = {
    'employee_id': 123,    
    'name': 'John Doe',    
    'position': 'Software Engineer',    
    'departments': ['Engineering', 'IT'],    
    'contact_info': {
        'email': 'john.doe@example.com',        
        'phone': '+1234567890'    
    },    
    'projects': [
        {
            'project_name': 'Web App Development',            
            'start_date': '2023-01-15',            
            'end-date': '2023-06-30'        
        },        
        {
            'project_name': 'Database Optimization',            
            'start_date': '2023-07-01',            
            'end_date': '2023-12-31'
        }
    ]
}

university_data = {
    'university_name': 'Tech University',   
    'faculties': [
        {
            'faculty_name': 'Engineering',           
            'departments': [
                {
                    'department_name': 'Computer Science',                    
                    'courses': [
                        {'course_name': 'Data Structures', 'credits': 4},                        
                        {'course_name': 'Algorithms', 'credits': 5}
                    ]
                },                
                {
                    'department_name': 'Electrical Engineering',                    
                    'courses': [
                        {'course_name': 'Circuit Design', 'credits': 4},                        
                        {'course_name': 'Power Systems', 'credits': 5}
                    ]
                }
            ]
        },       
        {
            'faculty_name': 'Business',            
            'departments': [
                 {
                    'department_name': 'Finance',                    
                    'courses': [
                        {'course_name': 'Investment Management', 'credits': 4},                        
                        {'course_name': 'Financial Accounting', 'credits': 5}
                    ]
                },
                {
                    'department_name': 'Marketing',                    
                    'courses': [
                        {'course_name': 'Consumer Behavior', 'credits': 4},                        
                        {'course_name': 'Digital Marketing', 'credits': 5}
                    ]
                }
            ]
        }
    ]
}


email = employee_data['contact_info']['email']
start_date1 = employee_data['projects'][0]['start_date']
start_date2 = employee_data['projects'][1]['start_date']
end_date = employee_data['projects'][1]['end_date']
computer_science = university_data['faculties'][0]['departments'][0]['department_name']
alg_credits = university_data['faculties'][0]['departments'][0]['courses'][1]['credits']
keys = list(university_data['faculties'][0]['departments'][1].keys())
courses = keys[1]
consumer_behavior = university_data['faculties'][1]['departments'][1]['courses'][0]['course_name']

print(email, start_date1, start_date2, end_date, computer_science, alg_credits, courses, consumer_behavior)