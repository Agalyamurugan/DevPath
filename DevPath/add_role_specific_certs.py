import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, CertificationRecommendation

# Clear existing certifications to start fresh
CertificationRecommendation.objects.all().delete()
print('Cleared all existing certifications')

# Define role-specific free certifications
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
