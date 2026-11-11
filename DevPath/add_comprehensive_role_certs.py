import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, CertificationRecommendation

# Clear existing certifications to start fresh
CertificationRecommendation.objects.all().delete()
print('Cleared all existing certifications')

# Define comprehensive role-specific free certifications
role_certifications = {
    'Junior Software Developer/Engineer': [
        {
            'platform': 'freecodecamp',
            'title': 'freeCodeCamp Python Certification',
            'description': 'Comprehensive Python programming certification with hands-on projects.',
            'url': 'https://www.freecodecamp.org/learn/scientific-computing-with-python/',
            'difficulty_level': 'Intermediate',
            'duration': '300 hours',
            'rating': 4.8,
            'is_paid': False,
            'price': 'Free',
            'provider': 'freeCodeCamp',
            'prerequisites': 'Basic programming knowledge',
            'order': 1
        },
        {
            'platform': 'coursera',
            'title': 'Google Python Certificate',
            'description': 'Google official Python certification program.',
            'url': 'https://www.coursera.org/professional-certificates/google-automation-with-python',
            'difficulty_level': 'Intermediate',
            'duration': '6 months',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'Google',
            'prerequisites': 'Basic Python knowledge',
            'order': 2
        },
        {
            'platform': 'mit',
            'title': 'MIT Introduction to Computer Science',
            'description': 'MIT free computer science fundamentals course.',
            'url': 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/',
            'difficulty_level': 'Beginner',
            'duration': 'Self-paced',
            'rating': 4.9,
            'is_paid': False,
            'price': 'Free',
            'provider': 'MIT',
            'prerequisites': 'None',
            'order': 3
        }
    ],
    'Web Developer': [
        {
            'platform': 'freecodecamp',
            'title': 'freeCodeCamp Responsive Web Design',
            'description': 'Master HTML, CSS, and responsive design principles.',
            'url': 'https://www.freecodecamp.org/learn/2022/responsive-web-design/',
            'difficulty_level': 'Beginner',
            'duration': '300 hours',
            'rating': 4.9,
            'is_paid': False,
            'price': 'Free',
            'provider': 'freeCodeCamp',
            'prerequisites': 'None',
            'order': 1
        },
        {
            'platform': 'mdn',
            'title': 'MDN Web Developer Certification',
            'description': 'Mozilla comprehensive web development certification.',
            'url': 'https://developer.mozilla.org/en-US/docs/Learn',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.8,
            'is_paid': False,
            'price': 'Free',
            'provider': 'Mozilla',
            'prerequisites': 'HTML/CSS basics',
            'order': 2
        },
        {
            'platform': 'google',
            'title': 'Google UX Design Certificate',
            'description': 'Google official UX design certification for web developers.',
            'url': 'https://www.coursera.org/professional-certificates/google-ux-design',
            'difficulty_level': 'Intermediate',
            'duration': '6 months',
            'rating': 4.8,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'Google',
            'prerequisites': 'Basic design knowledge',
            'order': 3
        }
    ],
    'Full Stack Developer': [
        {
            'platform': 'freecodecamp',
            'title': 'freeCodeCamp Full Stack Certification',
            'description': 'Complete full stack development with React and Node.js.',
            'url': 'https://www.freecodecamp.org/learn/full-stack-development/',
            'difficulty_level': 'Intermediate',
            'duration': '400 hours',
            'rating': 4.8,
            'is_paid': False,
            'price': 'Free',
            'provider': 'freeCodeCamp',
            'prerequisites': 'HTML/CSS/JS basics',
            'order': 1
        },
        {
            'platform': 'ibm',
            'title': 'IBM Full Stack Developer Certificate',
            'description': 'IBM full stack development with cloud technologies.',
            'url': 'https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer',
            'difficulty_level': 'Intermediate',
            'duration': '12 months',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'IBM',
            'prerequisites': 'Programming basics',
            'order': 2
        }
    ],
    'Database Administrator (Trainee)': [
        {
            'platform': 'mongodb',
            'title': 'MongoDB Database Administrator Certification',
            'description': 'Official MongoDB certification for database administrators.',
            'url': 'https://university.mongodb.com/certification/dba',
            'difficulty_level': 'Intermediate',
            'duration': '8 weeks',
            'rating': 4.6,
            'is_paid': False,
            'price': 'Free',
            'provider': 'MongoDB',
            'prerequisites': 'Basic database knowledge',
            'order': 1
        },
        {
            'platform': 'oracle',
            'title': 'Oracle Database Free Certification',
            'description': 'Oracle free database administration fundamentals.',
            'url': 'https://education.oracle.com/database/free-certification',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.5,
            'is_paid': False,
            'price': 'Free',
            'provider': 'Oracle',
            'prerequisites': 'SQL knowledge',
            'order': 2
        },
        {
            'platform': 'microsoft',
            'title': 'Microsoft SQL Server Certification',
            'description': 'Microsoft SQL Server database administration.',
            'url': 'https://learn.microsoft.com/en-us/credentials/certifications/exams/70-462/',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.6,
            'is_paid': False,
            'price': 'Free (with Microsoft Learn)',
            'provider': 'Microsoft',
            'prerequisites': 'Database basics',
            'order': 3
        }
    ],
    'Data Analyst': [
        {
            'platform': 'ibm',
            'title': 'IBM Data Analyst Professional Certificate',
            'description': 'Comprehensive data analysis certification with IBM tools.',
            'url': 'https://www.coursera.org/professional-certificates/ibm-data-analyst',
            'difficulty_level': 'Beginner',
            'duration': '3 months',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'IBM',
            'prerequisites': 'Basic math skills',
            'order': 1
        },
        {
            'platform': 'google',
            'title': 'Google Data Analytics Certificate',
            'description': 'Google official data analytics professional certificate.',
            'url': 'https://www.coursera.org/professional-certificates/google-data-analytics',
            'difficulty_level': 'Beginner',
            'duration': '6 months',
            'rating': 4.8,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'Google',
            'prerequisites': 'None',
            'order': 2
        },
        {
            'platform': 'khan',
            'title': 'Khan Academy Data Analysis Course',
            'description': 'Free data analysis fundamentals from Khan Academy.',
            'url': 'https://www.khanacademy.org/math/statistics-probability',
            'difficulty_level': 'Beginner',
            'duration': 'Self-paced',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free',
            'provider': 'Khan Academy',
            'prerequisites': 'Basic math',
            'order': 3
        }
    ],
    'DevOps Engineer (Trainee)': [
        {
            'platform': 'linux',
            'title': 'Linux Foundation Certified System Administrator',
            'description': 'Official Linux certification for system administration.',
            'url': 'https://training.linuxfoundation.org/certification/lfsa',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.6,
            'is_paid': False,
            'price': 'Free (with financial aid)',
            'provider': 'Linux Foundation',
            'prerequisites': 'Basic Linux knowledge',
            'order': 1
        },
        {
            'platform': 'aws',
            'title': 'AWS Cloud Practitioner Free Certification',
            'description': 'AWS foundational cloud certification with free training.',
            'url': 'https://aws.amazon.com/training/digital-cloud-training/',
            'difficulty_level': 'Beginner',
            'duration': '30 hours',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free',
            'provider': 'Amazon Web Services',
            'prerequisites': 'Basic IT knowledge',
            'order': 2
        },
        {
            'platform': 'docker',
            'title': 'Docker Certified Associate',
            'description': 'Official Docker certification for containerization.',
            'url': 'https://www.docker.com/certified-associate/',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.5,
            'is_paid': False,
            'price': 'Free (with Docker Hub)',
            'provider': 'Docker',
            'prerequisites': 'Container basics',
            'order': 3
        }
    ],
    'Cybersecurity Analyst': [
        {
            'platform': 'cisco',
            'title': 'Cisco Cybersecurity Certification',
            'description': 'Cisco official cybersecurity fundamentals certification.',
            'url': 'https://www.netacad.com/courses/cybersecurity',
            'difficulty_level': 'Beginner',
            'duration': 'Self-paced',
            'rating': 4.6,
            'is_paid': False,
            'price': 'Free',
            'provider': 'Cisco',
            'prerequisites': 'Basic networking',
            'order': 1
        },
        {
            'platform': 'compTIA',
            'title': 'CompTIA Security+ Free Training',
            'description': 'Free training materials for CompTIA Security+ certification.',
            'url': 'https://www.comptia.org/training/resources',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.5,
            'is_paid': False,
            'price': 'Free',
            'provider': 'CompTIA',
            'prerequisites': 'IT fundamentals',
            'order': 2
        }
    ],
    'Game Developer': [
        {
            'platform': 'unity',
            'title': 'Unity Certified Developer',
            'description': 'Official Unity game development certification.',
            'url': 'https://learn.unity.com/certifications',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free (with Unity Learn)',
            'provider': 'Unity',
            'prerequisites': 'C# basics',
            'order': 1
        },
        {
            'platform': 'unreal',
            'title': 'Unreal Engine Certification',
            'description': 'Epic Games Unreal Engine development certification.',
            'url': 'https://www.unrealengine.com/en-US/online-learning-courses',
            'difficulty_level': 'Intermediate',
            'duration': 'Self-paced',
            'rating': 4.6,
            'is_paid': False,
            'price': 'Free',
            'provider': 'Epic Games',
            'prerequisites': 'C++ basics',
            'order': 2
        }
    ],
    'Data Scientist': [
        {
            'platform': 'ibm',
            'title': 'IBM Data Science Professional Certificate',
            'description': 'Comprehensive data science certification with Python and machine learning.',
            'url': 'https://www.coursera.org/professional-certificates/ibm-data-science',
            'difficulty_level': 'Intermediate',
            'duration': '6 months',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'IBM',
            'prerequisites': 'Python and statistics',
            'order': 1
        },
        {
            'platform': 'mit',
            'title': 'MIT Data Science Certificate',
            'description': 'MIT free data science and machine learning course.',
            'url': 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/',
            'difficulty_level': 'Advanced',
            'duration': 'Self-paced',
            'rating': 4.9,
            'is_paid': False,
            'price': 'Free',
            'provider': 'MIT',
            'prerequisites': 'Programming and math',
            'order': 2
        }
    ],
    'UI/UX Designer': [
        {
            'platform': 'google',
            'title': 'Google UX Design Certificate',
            'description': 'Google official UX design professional certificate.',
            'url': 'https://www.coursera.org/professional-certificates/google-ux-design',
            'difficulty_level': 'Beginner',
            'duration': '6 months',
            'rating': 4.8,
            'is_paid': False,
            'price': 'Free (financial aid available)',
            'provider': 'Google',
            'prerequisites': 'None',
            'order': 1
        },
        {
            'platform': 'interaction',
            'title': 'Interaction Design Foundation',
            'description': 'Free UX design courses and certification.',
            'url': 'https://www.interaction-design.org/',
            'difficulty_level': 'Beginner',
            'duration': 'Self-paced',
            'rating': 4.7,
            'is_paid': False,
            'price': 'Free (membership)',
            'provider': 'IxDF',
            'prerequisites': 'None',
            'order': 2
        }
    ]
}

# Add certifications to each role
roles = Role.objects.all()
for role in roles:
    role_name = role.name
    if role_name in role_certifications:
        print(f'Adding certifications for {role_name}')
        for cert_data in role_certifications[role_name]:
            cert = CertificationRecommendation.objects.create(
                role=role,
                platform=cert_data['platform'],
                title=cert_data['title'],
                description=cert_data['description'],
                url=cert_data['url'],
                difficulty_level=cert_data['difficulty_level'],
                duration=cert_data['duration'],
                rating=cert_data['rating'],
                is_paid=cert_data['is_paid'],
                price=cert_data['price'],
                provider=cert_data['provider'],
                prerequisites=cert_data['prerequisites'],
                order=cert_data['order']
            )
            print(f'  Added: {cert.title}')
    else:
        # Add default certifications for roles not specifically defined
        print(f'Adding default certifications for {role_name}')
        default_certs = [
            {
                'platform': 'coursera',
                'title': f'Coursera {role_name} Certificate',
                'description': f'Professional certification for {role_name} roles.',
                'url': 'https://www.coursera.org',
                'difficulty_level': 'Intermediate',
                'duration': '3 months',
                'rating': 4.5,
                'is_paid': False,
                'price': 'Free (financial aid available)',
                'provider': 'Coursera',
                'prerequisites': 'Role-specific knowledge',
                'order': 1
            }
        ]
        for cert_data in default_certs:
            cert = CertificationRecommendation.objects.create(
                role=role,
                platform=cert_data['platform'],
                title=cert_data['title'],
                description=cert_data['description'],
                url=cert_data['url'],
                difficulty_level=cert_data['difficulty_level'],
                duration=cert_data['duration'],
                rating=cert_data['rating'],
                is_paid=cert_data['is_paid'],
                price=cert_data['price'],
                provider=cert_data['provider'],
                prerequisites=cert_data['prerequisites'],
                order=cert_data['order']
            )
            print(f'  Added: {cert.title}')

print('Role-specific certifications added successfully!')
