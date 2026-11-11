from django.core.management.base import BaseCommand
from django.db import transaction
from roadmaps.models import Role, LevelQuiz


class Command(BaseCommand):
    help = 'Create sample quizzes for all roles and levels'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Get all roles
            roles = Role.objects.all()
            
            if not roles.exists():
                self.stdout.write(self.style.WARNING('No roles found. Please run seed_roadmaps first.'))
                return

            # Quiz data for different roles and levels
            quiz_data = {
                'Frontend Developer': {
                    1: [
                        {
                            'title': 'HTML Fundamentals Quiz',
                            'description': 'Test your knowledge of HTML basics, tags, and semantic markup.',
                            'questions': [
                                {
                                    'question': 'Which tag is used for the most important heading?',
                                    'options': ['<h1>', '<h6>', '<heading>', '<header>'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What does HTML stand for?',
                                    'options': ['Hyper Text Markup Language', 'High Tech Modern Language', 'Home Tool Markup Language', 'Hyperlinks and Text Markup Language'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which attribute is used to specify an image\'s alternative text?',
                                    'options': ['src', 'alt', 'title', 'href'],
                                    'correct': 1
                                },
                                {
                                    'question': 'What is the correct HTML for creating a hyperlink?',
                                    'options': ['<a href="url">link</a>', '<link>url</link>', '<hyperlink>url</hyperlink>', '<http>url</http>'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which HTML element is used for the largest heading?',
                                    'options': ['<h6>', '<heading>', '<h1>', '<head>'],
                                    'correct': 2
                                }
                            ]
                        },
                        {
                            'title': 'CSS Basics Quiz',
                            'description': 'Test your understanding of CSS selectors, properties, and basic styling.',
                            'questions': [
                                {
                                    'question': 'Which CSS property is used to change the text color?',
                                    'options': ['text-color', 'font-color', 'color', 'text-style'],
                                    'correct': 2
                                },
                                {
                                    'question': 'How do you select an element with id "header"?',
                                    'options': ['#header', '.header', 'header', '*header'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which property is used to change the background color?',
                                    'options': ['bgcolor', 'background-color', 'color', 'background'],
                                    'correct': 1
                                },
                                {
                                    'question': 'How do you make text bold in CSS?',
                                    'options': ['font-weight: bold;', 'font-style: bold;', 'text-bold: true;', 'bold: on;'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which property controls the space between elements?',
                                    'options': ['spacing', 'margin', 'padding', 'gap'],
                                    'correct': 1
                                }
                            ]
                        }
                    ],
                    2: [
                        {
                            'title': 'JavaScript Fundamentals',
                            'description': 'Test your knowledge of JavaScript basics, variables, and functions.',
                            'questions': [
                                {
                                    'question': 'Which keyword is used to declare a variable in JavaScript?',
                                    'options': ['var', 'let', 'const', 'All of the above'],
                                    'correct': 3
                                },
                                {
                                    'question': 'How do you write "Hello World" in an alert box?',
                                    'options': ['alert("Hello World");', 'msgBox("Hello World");', 'alertBox("Hello World");', 'msg("Hello World");'],
                                    'correct': 0
                                },
                                {
                                    'question': 'How do you create a function in JavaScript?',
                                    'options': ['function = myFunction() {}', 'function myFunction() {}', 'def myFunction() {}', 'create myFunction() {}'],
                                    'correct': 1
                                },
                                {
                                    'question': 'How do you call a function named "myFunction"?',
                                    'options': ['call myFunction()', 'myFunction()', 'execute myFunction()', 'run myFunction()'],
                                    'correct': 1
                                },
                                {
                                    'question': 'Which symbol is used for comments in JavaScript?',
                                    'options': ['//', '#', '--', '/*'],
                                    'correct': 0
                                }
                            ]
                        }
                    ],
                    3: [
                        {
                            'title': 'React Components Quiz',
                            'description': 'Test your knowledge of React components, props, and state.',
                            'questions': [
                                {
                                    'question': 'What is the correct way to create a functional component in React?',
                                    'options': ['function MyComponent() {}', 'component MyComponent() {}', 'create MyComponent() {}', 'def MyComponent() {}'],
                                    'correct': 0
                                },
                                {
                                    'question': 'How do you pass data to a React component?',
                                    'options': ['props', 'state', 'attributes', 'parameters'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which hook is used to manage state in functional components?',
                                    'options': ['useState', 'useEffect', 'useContext', 'useReducer'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is JSX?',
                                    'options': ['JavaScript XML', 'Java Syntax Extension', 'JavaScript Extension', 'JSON XML'],
                                    'correct': 0
                                },
                                {
                                    'question': 'How do you handle events in React?',
                                    'options': ['onClick', 'onEvent', 'handleEvent', 'eventHandler'],
                                    'correct': 0
                                }
                            ]
                        }
                    ],
                    4: [
                        {
                            'title': 'Advanced React Patterns',
                            'description': 'Test your knowledge of advanced React patterns and optimization.',
                            'questions': [
                                {
                                    'question': 'Which hook is used for side effects in React?',
                                    'options': ['useEffect', 'useSideEffect', 'useCallback', 'useMemo'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is the purpose of React.memo?',
                                    'options': ['Memoize components', 'Create memo functions', 'Store memories', 'Cache API calls'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which hook is used to optimize expensive calculations?',
                                    'options': ['useMemo', 'useCallback', 'useEffect', 'useState'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is Context API used for?',
                                    'options': ['Global state management', 'API calls', 'Routing', 'Styling'],
                                    'correct': 0
                                },
                                {
                                    'question': 'How do you optimize React performance?',
                                    'options': ['All of the above', 'Code splitting', 'Memoization', 'Virtual scrolling'],
                                    'correct': 0
                                }
                            ]
                        }
                    ]
                },
                'Backend Developer': {
                    1: [
                        {
                            'title': 'Python Basics Quiz',
                            'description': 'Test your knowledge of Python fundamentals, data types, and control flow.',
                            'questions': [
                                {
                                    'question': 'Which keyword is used to define a function in Python?',
                                    'options': ['def', 'function', 'func', 'define'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is the correct file extension for Python files?',
                                    'options': ['.py', '.python', '.pt', '.pyth'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which of these is a mutable data type in Python?',
                                    'options': ['list', 'tuple', 'string', 'int'],
                                    'correct': 0
                                },
                                {
                                    'question': 'How do you create a comment in Python?',
                                    'options': ['# comment', '// comment', '/* comment */', '-- comment'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is the output of print(2 ** 3)?',
                                    'options': ['6', '8', '9', '12'],
                                    'correct': 1
                                }
                            ]
                        }
                    ],
                    2: [
                        {
                            'title': 'Django Fundamentals',
                            'description': 'Test your understanding of Django framework basics, models, and views.',
                            'questions': [
                                {
                                    'question': 'What is Django?',
                                    'options': ['Web framework', 'Database', 'Frontend library', 'CSS framework'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which command starts the Django development server?',
                                    'options': ['python manage.py runserver', 'django run', 'start server', 'python server.py'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is a Django model?',
                                    'options': ['Database table representation', 'URL pattern', 'HTML template', 'View function'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which file contains URL patterns in Django?',
                                    'options': ['urls.py', 'views.py', 'models.py', 'settings.py'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What does MVT stand for in Django?',
                                    'options': ['Model View Template', 'Model View Controller', 'MVC Template', 'Module View Template'],
                                    'correct': 0
                                }
                            ]
                        }
                    ]
                },
                'Full Stack Developer': {
                    1: [
                        {
                            'title': 'Web Development Basics',
                            'description': 'Test your knowledge of fundamental web development concepts.',
                            'questions': [
                                {
                                    'question': 'What does HTTP stand for?',
                                    'options': ['HyperText Transfer Protocol', 'High Tech Transfer Protocol', 'Home Tool Transfer Protocol', 'HyperText Text Protocol'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which port is commonly used for web development?',
                                    'options': ['80', '443', '3000', '8080'],
                                    'correct': 3
                                },
                                {
                                    'question': 'What is the purpose of CSS?',
                                    'options': ['Styling web pages', 'Database queries', 'Server logic', 'File management'],
                                    'correct': 0
                                },
                                {
                                    'question': 'Which language runs in the browser?',
                                    'options': ['JavaScript', 'Python', 'Java', 'C++'],
                                    'correct': 0
                                },
                                {
                                    'question': 'What is a REST API?',
                                    'options': ['Architectural style for APIs', 'Database type', 'CSS framework', 'JavaScript library'],
                                    'correct': 0
                                }
                            ]
                        }
                    ]
                }
            }

            created_quizzes = 0
            
            for role in roles:
                if role.name in quiz_data:
                    role_quizzes = quiz_data[role.name]
                    
                    for level, quizzes in role_quizzes.items():
                        for order, quiz_info in enumerate(quizzes):
                            # Check if quiz already exists
                            existing = LevelQuiz.objects.filter(
                                role=role,
                                level=str(level),
                                title=quiz_info['title']
                            ).first()
                            
                            if not existing:
                                # Check if there's already a quiz for this role and level
                                existing_level_quiz = LevelQuiz.objects.filter(
                                    role=role,
                                    level=str(level)
                                ).first()
                                
                                if existing_level_quiz:
                                    self.stdout.write(
                                        self.style.WARNING(f'Quiz already exists for {role.name} Level {level}: {existing_level_quiz.title}')
                                    )
                                    continue
                                
                                quiz = LevelQuiz.objects.create(
                                    role=role,
                                    level=str(level),
                                    title=quiz_info['title'],
                                    description=quiz_info['description'],
                                    passing_score=70,
                                    order=order
                                )
                                created_quizzes += 1
                                self.stdout.write(
                                    self.style.SUCCESS(f'Created quiz: {quiz.title} for {role.name} Level {level}')
                                )
                            else:
                                self.stdout.write(
                                    self.style.WARNING(f'Quiz already exists: {existing.title}')
                                )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'No quiz data found for role: {role.name}')
                    )

            if created_quizzes > 0:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created {created_quizzes} quizzes!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('No new quizzes were created. They may already exist.')
                )
