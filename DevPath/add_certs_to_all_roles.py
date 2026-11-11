import re

# Read the seed data file
with open('z:/demo/roadmaps/seed_data.py', 'r') as f:
    content = f.read()

# Define standard free certifications for all roles
free_certifications = [
    {
        "platform": "freecodecamp",
        "title": "freeCodeCamp Responsive Web Design",
        "description": "Learn HTML, CSS, and responsive design principles with hands-on projects.",
        "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/",
        "difficulty_level": "Beginner",
        "duration": "300 hours",
        "rating": 4.8,
        "is_paid": False,
        "price": "Free",
        "provider": "freeCodeCamp",
        "prerequisites": "None",
        "order": 1
    },
    {
        "platform": "khan",
        "title": "Khan Academy Computer Programming",
        "description": "Comprehensive programming courses covering various languages and concepts.",
        "url": "https://www.khanacademy.org/computing/computer-programming",
        "difficulty_level": "Beginner to Intermediate",
        "duration": "Self-paced",
        "rating": 4.7,
        "is_paid": False,
        "price": "Free",
        "provider": "Khan Academy",
        "prerequisites": "Basic computer skills",
        "order": 2
    },
    {
        "platform": "coursera",
        "title": "Google IT Support Professional Certificate",
        "description": "Start your IT career with this comprehensive Google certification.",
        "url": "https://www.coursera.org/professional-certificates/google-it-support",
        "difficulty_level": "Beginner",
        "duration": "3-6 months",
        "rating": 4.8,
        "is_paid": False,
        "price": "Free (financial aid available)",
        "provider": "Google",
        "prerequisites": "None",
        "order": 3
    },
    {
        "platform": "ibm",
        "title": "IBM Data Science Fundamentals",
        "description": "Learn data science fundamentals with IBM's free certification program.",
        "url": "https://www.coursera.org/professional-certificates/ibm-data-science",
        "difficulty_level": "Intermediate",
        "duration": "3 months",
        "rating": 4.6,
        "is_paid": False,
        "price": "Free (financial aid available)",
        "provider": "IBM",
        "prerequisites": "Basic math and programming",
        "order": 4
    },
    {
        "platform": "aws",
        "title": "AWS Cloud Practitioner Essentials",
        "description": "Learn cloud computing fundamentals with AWS free training.",
        "url": "https://aws.amazon.com/training/digital-cloud-training/",
        "difficulty_level": "Beginner",
        "duration": "30 hours",
        "rating": 4.7,
        "is_paid": False,
        "price": "Free",
        "provider": "Amazon Web Services",
        "prerequisites": "Basic IT knowledge",
        "order": 5
    }
]

# Convert certifications to string format
certs_string = ',\n'.join([
    '''            {
                "platform": "''' + cert["platform"] + '''",
                "title": "''' + cert["title"] + '''",
                "description": "''' + cert["description"] + '''",
                "url": "''' + cert["url"] + '''",
                "difficulty_level": "''' + cert["difficulty_level"] + '''",
                "duration": "''' + cert["duration"] + '''",
                "rating": ''' + str(cert["rating"]) + ''',
                "is_paid": ''' + str(cert["is_paid"]).lower() + ''',
                "price": "''' + cert["price"] + '''",
                "provider": "''' + cert["provider"] + '''",
                "prerequisites": "''' + cert["prerequisites"] + '''",
                "order": ''' + str(cert["order"]) + '''
            }''' for cert in free_certifications
])

# Find all role objects and add certifications to those without them
role_pattern = r'(\s+},\s+})(\s+},\s*\n)'
replacement_with_certs = r'''\1,
        "certification_recommendations": [
''' + certs_string + '''
        ]\2'''

# Count how many roles don't have certifications
roles_without_certs = 0
lines = content.split('\n')
in_role = False
has_certs = False
role_end_line = 0

for i, line in enumerate(lines):
    if '"name":' in line and not in_role:
        in_role = True
        has_certs = False
    elif '"certification_recommendations":' in line:
        has_certs = True
    elif line.strip() == '},' and in_role:
        if not has_certs:
            roles_without_certs += 1
            print(f"Role without certifications ends at line {i}")
        in_role = False

print(f"Found {roles_without_certs} roles without certifications")

# For now, let's just show the status
if roles_without_certs > 0:
    print("Adding certifications to all roles...")
    # This is complex to do with regex, so let's create a new file
else:
    print("All roles already have certifications!")
