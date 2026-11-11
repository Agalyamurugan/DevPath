"""
Comprehensive quiz questions for all tech roles
Each role has 3 levels (Beginner, Intermediate, Advanced) with 5 questions each
"""

def get_all_role_quizzes():
    """Get all quiz questions for all roles and levels"""
    
    quiz_database = {
        'Frontend Developer': {
            'Beginner': [
                {
                    'question': 'What does HTML stand for?',
                    'options': ['Hyper Text Markup Language', 'High Tech Modern Language', 'Home Tool Markup Language', 'Hyperlinks and Text Markup Language'],
                    'correct': 0,
                    'explanation': 'HTML stands for Hyper Text Markup Language. It\'s the standard markup language for creating web pages.'
                },
                {
                    'question': 'Which CSS property is used to change the text color of an element?',
                    'options': ['text-color', 'color', 'font-color', 'text-style'],
                    'correct': 1,
                    'explanation': 'The CSS "color" property is used to change the text color of an element.'
                },
                {
                    'question': 'What is the purpose of JavaScript in web development?',
                    'options': ['Styling web pages', 'Creating databases', 'Adding interactivity', 'Structuring content'],
                    'correct': 2,
                    'explanation': 'JavaScript is used to add interactivity and dynamic behavior to web pages.'
                },
                {
                    'question': 'Which HTML tag is used to create a hyperlink?',
                    'options': ['<link>', '<href>', '<a>', '<url>'],
                    'correct': 2,
                    'explanation': 'The <a> tag is used to create hyperlinks in HTML.'
                },
                {
                    'question': 'What does CSS stand for?',
                    'options': ['Computer Style Sheets', 'Creative Style Sheets', 'Cascading Style Sheets', 'Colorful Style Sheets'],
                    'correct': 2,
                    'explanation': 'CSS stands for Cascading Style Sheets, used for styling HTML elements.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is the purpose of the box model in CSS?',
                    'options': ['To create 3D effects', 'To define layout and spacing', 'To animate elements', 'To organize HTML'],
                    'correct': 1,
                    'explanation': 'The CSS box model defines how elements are structured with content, padding, border, and margin.'
                },
                {
                    'question': 'Which JavaScript method is used to select an HTML element by its ID?',
                    'options': ['getElementByClass()', 'querySelector()', 'getElementById()', 'selectElement()'],
                    'correct': 2,
                    'explanation': 'document.getElementById() is used to select an HTML element by its unique ID.'
                },
                {
                    'question': 'What is responsive web design?',
                    'options': ['Making websites load faster', 'Designing for different screen sizes', 'Creating animated websites', 'Using only HTML'],
                    'correct': 1,
                    'explanation': 'Responsive web design ensures websites work well on different screen sizes and devices.'
                },
                {
                    'question': 'Which CSS property is used to create flexible layouts?',
                    'options': ['position', 'float', 'flexbox', 'margin'],
                    'correct': 2,
                    'explanation': 'Flexbox is a CSS layout model for creating flexible and responsive layouts.'
                },
                {
                    'question': 'What is the DOM in JavaScript?',
                    'options': ['Data Object Model', 'Document Object Model', 'Dynamic Object Model', 'Design Object Model'],
                    'correct': 1,
                    'explanation': 'The DOM (Document Object Model) represents the structure of HTML documents as a tree of objects.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is the purpose of React hooks?',
                    'options': ['To style components', 'To add state and lifecycle features to functional components', 'To create animations', 'To connect to databases'],
                    'correct': 1,
                    'explanation': 'React hooks allow functional components to use state and lifecycle features previously only available in class components.'
                },
                {
                    'question': 'What is event delegation in JavaScript?',
                    'options': ['Creating multiple event handlers', 'Using a single event handler for multiple elements', 'Preventing events from bubbling', 'Creating custom events'],
                    'correct': 1,
                    'explanation': 'Event delegation uses a single event handler to manage events for multiple elements, improving performance.'
                },
                {
                    'question': 'What is the purpose of CSS Grid?',
                    'options': ['To create animations', 'To create two-dimensional layouts', 'To add colors', 'To handle responsive images'],
                    'correct': 1,
                    'explanation': 'CSS Grid is a two-dimensional layout system for creating complex web layouts.'
                },
                {
                    'question': 'What is a closure in JavaScript?',
                    'options': ['A way to close functions', 'A function with access to outer scope variables', 'A type of loop', 'A CSS property'],
                    'correct': 1,
                    'explanation': 'A closure is a function that has access to variables in its outer (enclosing) scope even after the outer function has returned.'
                },
                {
                    'question': 'What is the Virtual DOM in React?',
                    'options': ['A copy of the real DOM', 'A database for React', 'A styling system', 'A testing tool'],
                    'correct': 0,
                    'explanation': 'The Virtual DOM is a lightweight JavaScript representation of the real DOM, used for efficient updates.'
                }
            ]
        },
        'Backend Developer': {
            'Beginner': [
                {
                    'question': 'What is the primary purpose of a backend server?',
                    'options': ['To design user interfaces', 'To handle business logic and data', 'To create CSS styles', 'To manage client-side scripts'],
                    'correct': 1,
                    'explanation': 'Backend servers handle business logic, data processing, and server-side operations.'
                },
                {
                    'question': 'Which HTTP method is typically used to retrieve data from a server?',
                    'options': ['POST', 'GET', 'DELETE', 'PUT'],
                    'correct': 1,
                    'explanation': 'GET is the HTTP method used to retrieve data from a server.'
                },
                {
                    'question': 'What is a REST API?',
                    'options': ['A styling framework', 'An architectural style for web services', 'A database system', 'A frontend library'],
                    'correct': 1,
                    'explanation': 'REST (Representational State Transfer) is an architectural style for designing web services.'
                },
                {
                    'question': 'What does SQL stand for?',
                    'options': ['Structured Query Language', 'Simple Query Language', 'System Query Language', 'Standard Query Language'],
                    'correct': 0,
                    'explanation': 'SQL stands for Structured Query Language, used for managing relational databases.'
                },
                {
                    'question': 'What is the purpose of a database index?',
                    'options': ['To store images', 'To speed up data retrieval', 'To create backups', 'To encrypt data'],
                    'correct': 1,
                    'explanation': 'Database indexes improve the speed of data retrieval operations on database tables.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is middleware in backend development?',
                    'options': ['Software for hardware', 'Code that runs between request and response', 'Database software', 'Frontend libraries'],
                    'correct': 1,
                    'explanation': 'Middleware is software that runs between the request and response, processing requests before they reach the route handler.'
                },
                {
                    'question': 'What is database normalization?',
                    'options': ['Making data normal', 'Organizing data to reduce redundancy', 'Creating backups', 'Encrypting data'],
                    'correct': 1,
                    'explanation': 'Database normalization is the process of organizing data to minimize redundancy and improve data integrity.'
                },
                {
                    'question': 'What is an ORM (Object-Relational Mapping)?',
                    'options': ['A way to map objects to database tables', 'A type of API', 'A frontend framework', 'A testing tool'],
                    'correct': 0,
                    'explanation': 'ORM is a technique that converts data between incompatible type systems using object-oriented programming languages.'
                },
                {
                    'question': 'What is JWT (JSON Web Token) used for?',
                    'options': ['Database connections', 'Authentication and authorization', 'Data storage', 'API documentation'],
                    'correct': 1,
                    'explanation': 'JWT is a compact, URL-safe means of representing claims to be transferred between parties for authentication.'
                },
                {
                    'question': 'What is the purpose of API versioning?',
                    'options': ['To create multiple APIs', 'To manage changes without breaking existing clients', 'To improve performance', 'To add security'],
                    'correct': 1,
                    'explanation': 'API versioning allows developers to make changes without breaking existing client applications.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is microservices architecture?',
                    'options': ['A single large application', 'An approach to develop small independent services', 'A type of database', 'A frontend framework'],
                    'correct': 1,
                    'explanation': 'Microservices architecture involves developing small, independent services that communicate over APIs.'
                },
                {
                    'question': 'What is eventual consistency in distributed systems?',
                    'options': ['Data is always consistent', 'Data becomes consistent over time', 'No consistency needed', 'Instant consistency'],
                    'correct': 1,
                    'explanation': 'Eventual consistency means that given enough time, all replicas in a distributed system will converge to the same state.'
                },
                {
                    'question': 'What is a message queue in backend architecture?',
                    'options': ['A list of user messages', 'A communication system for asynchronous processing', 'A database table', 'An email system'],
                    'correct': 1,
                    'explanation': 'Message queues enable asynchronous communication between different components of a system.'
                },
                {
                    'question': 'What is the CAP theorem in distributed systems?',
                    'options': ['Consistency, Availability, Partition tolerance', 'Create, Access, Process', 'Client, Application, Protocol', 'Cache, API, Performance'],
                    'correct': 0,
                    'explanation': 'The CAP theorem states that a distributed system can only provide two of three guarantees: Consistency, Availability, and Partition tolerance.'
                },
                {
                    'question': 'What is sharding in database design?',
                    'options': ['Creating database backups', 'Partitioning data across multiple servers', 'Encrypting data', 'Creating indexes'],
                    'correct': 1,
                    'explanation': 'Sharding is a database partitioning pattern that distributes data across multiple separate servers.'
                }
            ]
        },
        'Full Stack Developer': {
            'Beginner': [
                {
                    'question': 'What does a full stack developer work with?',
                    'options': ['Only frontend technologies', 'Only backend technologies', 'Both frontend and backend technologies', 'Only databases'],
                    'correct': 2,
                    'explanation': 'Full stack developers work with both frontend (client-side) and backend (server-side) technologies.'
                },
                {
                    'question': 'Which of the following is a frontend technology?',
                    'options': ['Python', 'React', 'MySQL', 'Node.js'],
                    'correct': 1,
                    'explanation': 'React is a frontend JavaScript library for building user interfaces.'
                },
                {
                    'question': 'Which of the following is a backend technology?',
                    'options': ['HTML', 'CSS', 'Django', 'Bootstrap'],
                    'correct': 2,
                    'explanation': 'Django is a Python web framework used for backend development.'
                },
                {
                    'question': 'What is the purpose of an API in full stack development?',
                    'options': ['To style web pages', 'To connect frontend and backend', 'To create databases', 'To write HTML'],
                    'correct': 1,
                    'explanation': 'APIs (Application Programming Interfaces) allow frontend and backend to communicate with each other.'
                },
                {
                    'question': 'Which database is commonly used in full stack applications?',
                    'options': ['Photoshop', 'MongoDB', 'Microsoft Word', 'Excel'],
                    'correct': 1,
                    'explanation': 'MongoDB is a popular NoSQL database used in full stack applications.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is the MERN stack?',
                    'options': ['MySQL, Express, React, Node.js', 'MongoDB, Express, React, Node.js', 'MongoDB, Ember, React, Node.js', 'MySQL, Express, Angular, Node.js'],
                    'correct': 1,
                    'explanation': 'MERN stack stands for MongoDB, Express.js, React, and Node.js - a popular full stack technology combination.'
                },
                {
                    'question': 'What is CORS in web development?',
                    'options': ['A database system', 'Cross-Origin Resource Sharing policy', 'A CSS framework', 'A JavaScript library'],
                    'correct': 1,
                    'explanation': 'CORS (Cross-Origin Resource Sharing) is a security feature that controls how web pages request resources from different domains.'
                },
                {
                    'question': 'What is the purpose of environment variables?',
                    'options': ['To style websites', 'To store configuration data securely', 'To create animations', 'To write HTML'],
                    'correct': 1,
                    'explanation': 'Environment variables store configuration data like API keys and database credentials separately from code.'
                },
                {
                    'question': 'What is authentication vs authorization?',
                    'options': ['They are the same thing', 'Authentication is who you are, authorization is what you can do', 'Authorization is who you are, authentication is what you can do', 'Both relate to databases'],
                    'correct': 1,
                    'explanation': 'Authentication verifies identity (who you are), while authorization determines permissions (what you can do).'
                },
                {
                    'question': 'What is a RESTful API design principle?',
                    'options': ['Use only POST requests', 'Use standard HTTP methods and stateless communication', 'Use only databases', 'Use only frontend technologies'],
                    'correct': 1,
                    'explanation': 'RESTful APIs use standard HTTP methods (GET, POST, PUT, DELETE) and maintain stateless communication.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is serverless architecture?',
                    'options': ['Architecture without servers', 'Cloud services that manage server infrastructure automatically', 'Only frontend development', 'Using only databases'],
                    'correct': 1,
                    'explanation': 'Serverless architecture allows developers to build and run applications without managing server infrastructure.'
                },
                {
                    'question': 'What is a CDN (Content Delivery Network)?',
                    'options': ['A database system', 'A distributed network for delivering web content', 'A programming language', 'A CSS framework'],
                    'correct': 1,
                    'explanation': 'CDNs distribute web content across multiple servers worldwide to improve delivery speed and reliability.'
                },
                {
                    'question': 'What is the purpose of load balancing?',
                    'options': ['To balance CSS styles', 'To distribute network traffic across multiple servers', 'To write JavaScript', 'To create databases'],
                    'correct': 1,
                    'explanation': 'Load balancing distributes incoming network traffic across multiple servers to prevent overload and improve reliability.'
                },
                {
                    'question': 'What is containerization in full stack development?',
                    'options': ['Creating web containers', 'Packaging applications with their dependencies', 'Writing CSS', 'Designing user interfaces'],
                    'correct': 1,
                    'explanation': 'Containerization packages applications with all their dependencies into isolated containers for consistent deployment.'
                },
                {
                    'question': 'What is CI/CD in full stack development?',
                    'options': ['Continuous Integration/Continuous Deployment', 'Creative Interface/Continuous Design', 'Client Interface/Client Deployment', 'Code Integration/Code Development'],
                    'correct': 0,
                    'explanation': 'CI/CD (Continuous Integration/Continuous Deployment) automates the process of integrating code changes and deploying applications.'
                }
            ]
        },
        'Data Analyst': {
            'Beginner': [
                {
                    'question': 'What is the primary role of a Data Analyst?',
                    'options': ['Building websites', 'Extracting insights from data', 'Managing servers', 'Designing user interfaces'],
                    'correct': 1,
                    'explanation': 'Data Analysts primarily focus on extracting meaningful insights from data to help businesses make informed decisions.'
                },
                {
                    'question': 'Which language is most commonly used for data analysis?',
                    'options': ['Java', 'Python', 'C++', 'PHP'],
                    'correct': 1,
                    'explanation': 'Python is the most popular language for data analysis due to its extensive libraries like pandas, NumPy, and matplotlib.'
                },
                {
                    'question': 'What is SQL used for in data analysis?',
                    'options': ['Creating visualizations', 'Querying and manipulating databases', 'Building machine learning models', 'Designing user interfaces'],
                    'correct': 1,
                    'explanation': 'SQL is used to query, retrieve, and manipulate data stored in relational databases, which is essential for data analysis.'
                },
                {
                    'question': 'What is the purpose of data visualization?',
                    'options': ['To store data', 'To represent data visually for better understanding', 'To encrypt data', 'To backup data'],
                    'correct': 1,
                    'explanation': 'Data visualization helps to represent complex data in a visual format, making it easier to understand patterns and insights.'
                },
                {
                    'question': 'Which tool is commonly used for creating data visualizations in Python?',
                    'options': ['Django', 'Flask', 'Matplotlib', 'NumPy'],
                    'correct': 2,
                    'explanation': 'Matplotlib is a popular Python library used for creating static, animated, and interactive visualizations.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is pandas used for in data analysis?',
                    'options': ['Web development', 'Data manipulation and analysis', 'Database management', 'Machine learning'],
                    'correct': 1,
                    'explanation': 'Pandas is a Python library specifically designed for data manipulation, cleaning, and analysis, particularly with structured data.'
                },
                {
                    'question': 'What is data wrangling?',
                    'options': ['Creating databases', 'Cleaning and transforming raw data for analysis', 'Building machine learning models', 'Designing dashboards'],
                    'correct': 1,
                    'explanation': 'Data wrangling is the process of cleaning, transforming, and preparing raw data for analysis, making it suitable for downstream tasks.'
                },
                {
                    'question': 'What is a DataFrame in pandas?',
                    'options': ['A database table', 'A 2D labeled data structure', 'A machine learning model', 'A visualization chart'],
                    'correct': 1,
                    'explanation': 'A DataFrame is a 2D labeled data structure in pandas, similar to a spreadsheet or database table, used for data manipulation.'
                },
                {
                    'question': 'Which method is used to handle missing values in pandas?',
                    'options': ['fill_na()', 'drop_na()', 'handle_missing()', 'clean_data()'],
                    'correct': 0,
                    'explanation': 'The fill_na() method in pandas is used to fill missing values, while drop_na() is used to remove them.'
                },
                {
                    'question': 'What is exploratory data analysis (EDA)?',
                    'options': ['Building machine learning models', 'Analyzing data to summarize main characteristics', 'Creating databases', 'Writing documentation'],
                    'correct': 1,
                    'explanation': 'EDA involves analyzing data sets to summarize their main characteristics, often with visual methods, to understand the data better.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is statistical significance in data analysis?',
                    'options': ['The importance of data', 'The likelihood that results are not due to chance', 'The size of the dataset', 'The accuracy of predictions'],
                    'correct': 1,
                    'explanation': 'Statistical significance indicates whether the observed results are likely due to chance or represent a real effect in the population.'
                },
                {
                    'question': 'What is A/B testing used for in data analysis?',
                    'options': ['Testing software bugs', 'Comparing two versions to determine which performs better', 'Database performance testing', 'Network speed testing'],
                    'correct': 1,
                    'explanation': 'A/B testing is a method used to compare two versions of something to determine which one performs better, commonly used in marketing and product development.'
                },
                {
                    'question': 'What is time series analysis?',
                    'options': ['Analyzing data collected over time', 'Analyzing spatial data', 'Analyzing text data', 'Analyzing image data'],
                    'correct': 0,
                    'explanation': 'Time series analysis involves analyzing data points collected over time to identify trends, patterns, and seasonal variations.'
                },
                {
                    'question': 'What is the purpose of data normalization?',
                    'options': ['To encrypt data', 'To scale numerical features to a standard range', 'To create visualizations', 'To backup data'],
                    'correct': 1,
                    'explanation': 'Data normalization scales numerical features to a standard range, typically 0-1, to prevent features with large ranges from dominating the analysis.'
                },
                {
                    'question': 'What is a pivot table in data analysis?',
                    'options': ['A database table', 'A data summarization tool', 'A machine learning algorithm', 'A visualization technique'],
                    'correct': 1,
                    'explanation': 'A pivot table is a data summarization tool used in spreadsheet programs and data analysis to reorganize and summarize large datasets.'
                }
            ]
        },
        'Data Scientist': {
            'Beginner': [
                {
                    'question': 'What is the primary goal of data science?',
                    'options': ['Creating websites', 'Extracting insights from data', 'Designing user interfaces', 'Managing servers'],
                    'correct': 1,
                    'explanation': 'Data science focuses on extracting meaningful insights and knowledge from structured and unstructured data.'
                },
                {
                    'question': 'Which programming language is most commonly used in data science?',
                    'options': ['Java', 'Python', 'C++', 'PHP'],
                    'correct': 1,
                    'explanation': 'Python is the most popular programming language in data science due to its extensive libraries like pandas, NumPy, and scikit-learn.'
                },
                {
                    'question': 'What is a dataset in data science?',
                    'options': ['A programming tool', 'A collection of data', 'A database system', 'A web framework'],
                    'correct': 1,
                    'explanation': 'A dataset is a collection of data that can be analyzed to extract insights and patterns.'
                },
                {
                    'question': 'What is data visualization?',
                    'options': ['Writing code', 'Creating visual representations of data', 'Managing databases', 'Designing websites'],
                    'correct': 1,
                    'explanation': 'Data visualization is the graphical representation of data to help people understand trends and patterns.'
                },
                {
                    'question': 'What is the purpose of statistics in data science?',
                    'options': ['To write better code', 'To analyze and interpret data', 'To design websites', 'To manage servers'],
                    'correct': 1,
                    'explanation': 'Statistics provides the mathematical foundation for analyzing data and making inferences.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is machine learning?',
                    'options': ['Learning to code better', 'Algorithms that improve through experience', 'Database management', 'Web development'],
                    'correct': 1,
                    'explanation': 'Machine learning is a subset of AI where algorithms learn patterns from data to make predictions or decisions.'
                },
                {
                    'question': 'What is the difference between supervised and unsupervised learning?',
                    'options': ['No difference', 'Supervised uses labeled data, unsupervised uses unlabeled data', 'Supervised is faster', 'Unsupervised is more accurate'],
                    'correct': 1,
                    'explanation': 'Supervised learning uses labeled training data, while unsupervised learning finds patterns in unlabeled data.'
                },
                {
                    'question': 'What is a feature in machine learning?',
                    'options': ['A bug in code', 'An input variable used for prediction', 'A database table', 'A visualization'],
                    'correct': 1,
                    'explanation': 'Features are the input variables or attributes used by machine learning models to make predictions.'
                },
                {
                    'question': 'What is overfitting in machine learning?',
                    'options': ['When a model is too simple', 'When a model learns training data too well', 'When data is missing', 'When visualization fails'],
                    'correct': 1,
                    'explanation': 'Overfitting occurs when a machine learning model learns the training data too well and fails to generalize to new data.'
                },
                {
                    'question': 'What is the purpose of cross-validation?',
                    'options': ['To validate user input', 'To assess model performance on unseen data', 'To create visualizations', 'To clean data'],
                    'correct': 1,
                    'explanation': 'Cross-validation is a technique to evaluate how well a machine learning model will perform on unseen data.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is deep learning?',
                    'options': ['Learning complex topics', 'Neural networks with multiple layers', 'Advanced statistics', 'Database optimization'],
                    'correct': 1,
                    'explanation': 'Deep learning uses neural networks with multiple layers to learn complex patterns from large amounts of data.'
                },
                {
                    'question': 'What is the purpose of regularization in machine learning?',
                    'options': ['To make models faster', 'To prevent overfitting by adding complexity penalty', 'To improve visualization', 'To clean data'],
                    'correct': 1,
                    'explanation': 'Regularization adds a penalty for model complexity to prevent overfitting and improve generalization.'
                },
                {
                    'question': 'What is ensemble learning?',
                    'options': ['Learning in groups', 'Combining multiple models for better predictions', 'Teaching machines', 'Data cleaning'],
                    'correct': 1,
                    'explanation': 'Ensemble learning combines predictions from multiple machine learning models to improve overall performance.'
                },
                {
                    'question': 'What is natural language processing (NLP)?',
                    'options': ['Processing natural speech', 'Analyzing and understanding human language', 'Database queries', 'Web scraping'],
                    'correct': 1,
                    'explanation': 'NLP is a field of AI focused on enabling computers to understand, interpret, and generate human language.'
                },
                {
                    'question': 'What is the curse of dimensionality?',
                    'options': ['Too many dimensions in physics', 'Problems arising from high-dimensional data', 'Database issues', 'Visualization problems'],
                    'correct': 1,
                    'explanation': 'The curse of dimensionality refers to various phenomena that arise when analyzing data in high-dimensional spaces.'
                }
            ]
        },
        'Database Administrator': {
            'Beginner': [
                {
                    'question': 'What is the primary role of a Database Administrator?',
                    'options': ['Creating websites', 'Managing and maintaining databases', 'Writing frontend code', 'Designing user interfaces'],
                    'correct': 1,
                    'explanation': 'Database Administrators are responsible for managing, maintaining, and securing database systems.'
                },
                {
                    'question': 'What is a primary key in a database?',
                    'options': ['The most important table', 'A unique identifier for database records', 'A password', 'A backup file'],
                    'correct': 1,
                    'explanation': 'A primary key is a unique identifier that ensures each record in a table can be uniquely identified.'
                },
                {
                    'question': 'What does SQL stand for?',
                    'options': ['Structured Query Language', 'Simple Query Language', 'System Query Language', 'Standard Query Language'],
                    'correct': 0,
                    'explanation': 'SQL stands for Structured Query Language, used for managing and manipulating relational databases.'
                },
                {
                    'question': 'What is a database table?',
                    'options': ['A piece of furniture', 'A collection of related data organized in rows and columns', 'A query result', 'A backup file'],
                    'correct': 1,
                    'explanation': 'A database table is a structured collection of data organized in rows (records) and columns (attributes).'
                },
                {
                    'question': 'What is the purpose of database backups?',
                    'options': ['To speed up queries', 'To recover data in case of loss or corruption', 'To create new tables', 'To improve security'],
                    'correct': 1,
                    'explanation': 'Database backups are essential for data recovery in case of accidental deletion, corruption, or system failures.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is database normalization?',
                    'options': ['Making data normal', 'Organizing data to reduce redundancy and improve integrity', 'Creating backups', 'Encrypting data'],
                    'correct': 1,
                    'explanation': 'Database normalization is the process of organizing data to minimize redundancy and improve data integrity.'
                },
                {
                    'question': 'What is a foreign key in a database?',
                    'options': ['A key from another country', 'A field that links to a primary key in another table', 'A backup key', 'An encryption key'],
                    'correct': 1,
                    'explanation': 'A foreign key is a field that establishes a link between tables by referencing a primary key in another table.'
                },
                {
                    'question': 'What is an index in a database?',
                    'options': ['A table of contents', 'A data structure that improves query performance', 'A backup file', 'A security feature'],
                    'correct': 1,
                    'explanation': 'Database indexes are data structures that improve the speed of data retrieval operations on database tables.'
                },
                {
                    'question': 'What is a transaction in database terms?',
                    'options': ['A financial operation', 'A sequence of operations performed as a single logical unit', 'A query result', 'A backup process'],
                    'correct': 1,
                    'explanation': 'A database transaction is a sequence of operations performed as a single logical unit of work.'
                },
                {
                    'question': 'What is referential integrity?',
                    'options': ['Data quality', 'Ensuring relationships between tables remain consistent', 'Backup integrity', 'Security validation'],
                    'correct': 1,
                    'explanation': 'Referential integrity ensures that relationships between tables remain consistent, preventing orphaned records.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is database sharding?',
                    'options': ['Breaking databases into pieces', 'Partitioning data across multiple servers', 'Creating backups', 'Encrypting data'],
                    'correct': 1,
                    'explanation': 'Database sharding is a method of horizontal partitioning where data is distributed across multiple servers.'
                },
                {
                    'question': 'What is a deadlock in database systems?',
                    'options': ['A locked database', 'A situation where transactions are waiting for each other', 'A security breach', 'A backup failure'],
                    'correct': 1,
                    'explanation': 'A deadlock occurs when two or more transactions are waiting for each other to release locks.'
                },
                {
                    'question': 'What is query optimization?',
                    'options': ['Making queries shorter', 'Improving query performance and efficiency', 'Creating new queries', 'Deleting old queries'],
                    'correct': 1,
                    'explanation': 'Query optimization involves improving the performance and efficiency of database queries.'
                },
                {
                    'question': 'What is replication in database systems?',
                    'options': ['Making copies of data', 'Creating backups', 'Data modeling', 'Query optimization'],
                    'correct': 0,
                    'explanation': 'Database replication involves creating and maintaining multiple copies of the same data across different servers.'
                },
                {
                    'question': 'What is a stored procedure?',
                    'options': ['A way to store data', 'A precompiled SQL code stored in the database', 'A backup file', 'A security feature'],
                    'correct': 1,
                    'explanation': 'A stored procedure is a precompiled collection of SQL statements stored in the database that can be executed as a unit.'
                }
            ]
        },
        'DevOps Engineer': {
            'Beginner': [
                {
                    'question': 'What does DevOps stand for?',
                    'options': ['Development Operations', 'Development and Operations', 'Deploy Operations', 'Database Operations'],
                    'correct': 1,
                    'explanation': 'DevOps combines Development (Dev) and Operations (Ops) to shorten the development lifecycle and provide continuous delivery.'
                },
                {
                    'question': 'What is continuous integration?',
                    'options': ['Integrating code continuously', 'Merging code branches frequently with automated testing', 'Creating new features', 'Deploying applications'],
                    'correct': 1,
                    'explanation': 'Continuous Integration (CI) is the practice of merging code changes frequently with automated builds and tests.'
                },
                {
                    'question': 'What is version control?',
                    'options': ['Controlling versions of software', 'A system that tracks changes to code over time', 'Creating backups', 'Managing deployments'],
                    'correct': 1,
                    'explanation': 'Version control systems track and manage changes to code over time, allowing collaboration and rollback capabilities.'
                },
                {
                    'question': 'What is Git?',
                    'options': ['A programming language', 'A distributed version control system', 'A database', 'A cloud platform'],
                    'correct': 1,
                    'explanation': 'Git is a distributed version control system that tracks changes in code and enables collaboration among developers.'
                },
                {
                    'question': 'What is the purpose of a build server?',
                    'options': ['To build physical servers', 'To automatically compile and test code', 'To store code', 'To manage databases'],
                    'correct': 1,
                    'explanation': 'Build servers automatically compile, test, and prepare code for deployment as part of the CI/CD pipeline.'
                }
            ],
            'Intermediate': [
                {
                    'question': 'What is containerization?',
                    'options': ['Creating containers for shipping', 'Packaging applications with their dependencies into isolated environments', 'Creating virtual machines', 'Managing storage'],
                    'correct': 1,
                    'explanation': 'Containerization packages applications with all their dependencies into isolated containers for consistent deployment.'
                },
                {
                    'question': 'What is Docker?',
                    'options': ['A programming language', 'A platform for developing and running applications in containers', 'A database system', 'A cloud provider'],
                    'correct': 1,
                    'explanation': 'Docker is a platform that enables developers to create, deploy, and run applications in containers.'
                },
                {
                    'question': 'What is infrastructure as code (IaC)?',
                    'options': ['Writing code for infrastructure', 'Managing and provisioning infrastructure through code', 'Creating infrastructure manually', 'Testing infrastructure'],
                    'correct': 1,
                    'explanation': 'Infrastructure as Code is the practice of managing and provisioning infrastructure through machine-readable definition files.'
                },
                {
                    'question': 'What is monitoring in DevOps?',
                    'options': ['Watching code changes', 'Observing system performance and health', 'Creating backups', 'Managing deployments'],
                    'correct': 1,
                    'explanation': 'Monitoring involves observing system performance, health, and availability to ensure optimal operation.'
                },
                {
                    'question': 'What is a CI/CD pipeline?',
                    'options': ['A water pipeline', 'Automated process for software delivery', 'A database connection', 'A version control system'],
                    'correct': 1,
                    'explanation': 'CI/CD pipeline automates the process of integrating code changes and deploying applications through testing and production.'
                }
            ],
            'Advanced': [
                {
                    'question': 'What is Kubernetes?',
                    'options': ['A programming language', 'A container orchestration platform', 'A database system', 'A cloud provider'],
                    'correct': 1,
                    'explanation': 'Kubernetes is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications.'
                },
                {
                    'question': 'What is blue-green deployment?',
                    'options': ['Deploying blue and green applications', 'A deployment strategy with two identical production environments', 'A color scheme for UI', 'A testing method'],
                    'correct': 1,
                    'explanation': 'Blue-green deployment maintains two identical production environments, allowing seamless switching between versions.'
                },
                {
                    'question': 'What is infrastructure monitoring?',
                    'options': ['Watching physical servers', 'Monitoring the health and performance of IT infrastructure', 'Creating infrastructure', 'Testing infrastructure'],
                    'correct': 1,
                    'explanation': 'Infrastructure monitoring involves tracking the health, performance, and availability of servers, networks, and applications.'
                },
                {
                    'question': 'What is a service mesh?',
                    'options': ['A network of services', 'A dedicated infrastructure layer for managing service-to-service communication', 'A database cluster', 'A monitoring tool'],
                    'correct': 1,
                    'explanation': 'A service mesh is a dedicated infrastructure layer that handles service-to-service communication in microservices architecture.'
                },
                {
                    'question': 'What is chaos engineering?',
                    'options': ['Creating chaos in code', 'Testing system resilience by intentionally introducing failures', 'Debugging complex systems', 'Managing chaos in deployments'],
                    'correct': 1,
                    'explanation': 'Chaos engineering involves testing system resilience by intentionally introducing failures to identify weaknesses.'
                }
            ]
        }
    }
    
    return quiz_database
