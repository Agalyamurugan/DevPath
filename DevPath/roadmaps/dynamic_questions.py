"""
Dynamic quiz question generator based on user level.
Generates appropriate difficulty questions for each learning level.
"""

import random

def get_beginner_questions():
    """Generate beginner-level questions"""
    questions = [
        {
            'question': 'What is the primary purpose of HTML in web development?',
            'options': [
                'Styling web pages',
                'Creating web structure', 
                'Adding interactivity',
                'Database management'
            ],
            'correct': 0,
            'explanation': 'HTML is used for creating the structure and content of web pages.'
        },
        {
            'question': 'Which programming language is known as the "language of the web"?',
            'options': [
                'JavaScript',
                'Python',
                'Java',
                'C++'
            ],
            'correct': 0,
            'explanation': 'JavaScript is called the "language of the web" because it runs in all web browsers.'
        },
        {
            'question': 'What does CSS stand for?',
            'options': [
                'Computer Style Sheets',
                'Creative Style Sheets', 
                'Cascading Style Sheets',
                'Colorful Style Sheets'
            ],
            'correct': 2,
            'explanation': 'CSS stands for Cascading Style Sheets, which describes how styles cascade down through documents.'
        },
        {
            'question': 'Which HTML tag is used to create the largest heading?',
            'options': [
                '<h1>',
                '<h2>',
                '<h3>',
                '<h4>'
            ],
            'correct': 0,
            'explanation': 'The <h1> tag creates the largest heading, followed by <h2>, <h3>, etc.'
        },
        {
            'question': 'What is the correct way to declare a variable in JavaScript?',
            'options': [
                'var myVar = "value"',
                'let myVar = "value"',
                'const myVar = "value"',
                'myVar = "value"'
            ],
            'correct': 1,
            'explanation': 'The modern way is to use "const" for variables that won\'t change, "let" for variables that will be reassigned, and "var" for older code.'
        }
    ]
    return random.sample(questions, 5)  # Return 5 random questions

def get_intermediate_questions():
    """Generate intermediate-level questions"""
    questions = [
        {
            'question': 'What is the purpose of a REST API in web development?',
            'options': [
                'To connect frontend to backend',
                'To create database connections',
                'To style web pages',
                'To handle user authentication'
            ],
            'correct': 0,
            'explanation': 'REST APIs are used to create standardized communication between frontend and backend systems, allowing them to exchange data.'
        },
        {
            'question': 'Which HTTP status code indicates a successful request?',
            'options': [
                '200 OK',
                '404 Not Found',
                '500 Internal Server Error',
                '301 Moved Permanently'
            ],
            'correct': 0,
            'explanation': 'HTTP 200 OK indicates the request was successful. Other codes like 404, 500, and 301 indicate different conditions.'
        },
        {
            'question': 'What is the main advantage of using a version control system like Git?',
            'options': [
                'Automatic backups',
                'Collaboration features',
                'Branching and merging',
                'Code history tracking'
            ],
            'correct': 2,
            'explanation': 'While all are benefits, the main advantage is branching and merging, which allows multiple developers to work on different features simultaneously.'
        },
        {
            'question': 'Which JavaScript method is used to make asynchronous API calls?',
            'options': [
                'XMLHttpRequest',
                'Fetch API',
                'Async/Await',
                'Callbacks'
            ],
            'correct': 1,
            'explanation': 'The modern Fetch API and async/await syntax provide cleaner, more readable asynchronous code compared to callbacks and raw XMLHttpRequest.'
        },
        {
            'question': 'What is the purpose of responsive web design?',
            'options': [
                'Make websites load faster',
                'Improve SEO rankings',
                'Better mobile experience',
                'Reduce development time'
            ],
            'correct': 1,
            'explanation': 'Responsive web design ensures websites work well on all devices, improving user experience and SEO.'
        }
    ]
    return random.sample(questions, 5)

def get_advanced_questions():
    """Generate advanced-level questions"""
    questions = [
        {
            'question': 'What is the primary benefit of using a microservices architecture?',
            'options': [
                'Improved scalability',
                'Better fault isolation',
                'Independent deployment',
                'Increased complexity'
            ],
            'correct': 0,
            'explanation': 'The primary benefit is improved scalability, as services can be scaled independently based on demand.'
        },
        {
            'question': 'Which database indexing strategy is most effective for large datasets?',
            'options': [
                'Full table scan',
                'Partial indexing',
                'No indexing',
                'Composite indexing'
            ],
            'correct': 1,
            'explanation': 'For large datasets, partial indexing is often most effective as it balances query performance with storage efficiency.'
        },
        {
            'question': 'What is the main purpose of Docker in development workflows?',
            'options': [
                'Containerization of applications',
                'Environment consistency',
                'Simplified deployment',
                'Resource optimization'
            ],
            'correct': 2,
            'explanation': 'While containerization is a key benefit, the main purpose is ensuring environment consistency across development, testing, and production.'
        },
        {
            'question': 'Which approach is best for handling authentication in modern web applications?',
            'options': [
                'Session-based authentication',
                'JWT tokens',
                'OAuth 2.0',
                'Traditional cookies'
            ],
            'correct': 1,
            'explanation': 'JWT (JSON Web Tokens) provide stateless authentication, better security, and work well with modern APIs compared to traditional sessions.'
        },
        {
            'question': 'What is the primary advantage of using a Content Delivery Network (CDN)?',
            'options': [
                'Faster content delivery',
                'Reduced server load',
                'Better global availability',
                'Improved security'
            ],
            'correct': 0,
            'explanation': 'While all are benefits, the primary advantage is reduced server load, as content is distributed across multiple edge locations.'
        }
    ]
    return random.sample(questions, 5)

def get_data_science_questions(level):
    """Generate Data Science specific questions based on level"""
    if level == 'Beginner':
        return [
            {
                'question': 'What is the primary purpose of a histogram in data analysis?',
                'options': [
                    'Show data distribution',
                    'Compare categories',
                    'Display trends over time',
                    'Show relationships between variables'
                ],
                'correct': 0,
                'explanation': 'Histograms are used to visualize the distribution of continuous data and understand its frequency patterns.'
            },
            {
                'question': 'Which Python library is most commonly used for data manipulation?',
                'options': [
                    'NumPy',
                    'Pandas',
                    'Matplotlib',
                    'Scikit-learn'
                ],
                'correct': 1,
                'explanation': 'Pandas is the most popular library for data manipulation and analysis in Python.'
            },
            {
                'question': 'What does the term "correlation" measure in data science?',
                'options': [
                    'Causation between variables',
                    'Statistical relationship between variables',
                    'Data quality',
                    'Sample size'
                ],
                'correct': 1,
                'explanation': 'Correlation measures the strength and direction of the statistical relationship between two variables.'
            },
            {
                'question': 'Which type of data visualization is best for showing parts of a whole?',
                'options': [
                    'Bar chart',
                    'Line chart',
                    'Pie chart',
                    'Scatter plot'
                ],
                'correct': 2,
                'explanation': 'Pie charts are specifically designed to show the proportion of parts to a whole.'
            },
            {
                'question': 'What is the purpose of data cleaning in data science?',
                'options': [
                    'Make data look better',
                    'Remove errors and inconsistencies',
                    'Increase data size',
                    'Reduce processing time'
                ],
                'correct': 1,
                'explanation': 'Data cleaning involves identifying and correcting errors, inconsistencies, and inaccuracies in the data.'
            }
        ]
    elif level == 'Intermediate':
        return [
            {
                'question': 'What is the difference between supervised and unsupervised learning?',
                'options': [
                    'Data size requirements',
                    'Presence of labeled training data',
                    'Algorithm complexity',
                    'Processing speed'
                ],
                'correct': 1,
                'explanation': 'Supervised learning uses labeled data, while unsupervised learning works with unlabeled data to find patterns.'
            },
            {
                'question': 'Which metric is most appropriate for evaluating a binary classification model with imbalanced classes?',
                'options': [
                    'Accuracy',
                    'Precision',
                    'F1-Score',
                    'Mean Squared Error'
                ],
                'correct': 2,
                'explanation': 'F1-Score balances precision and recall, making it suitable for imbalanced datasets.'
            },
            {
                'question': 'What is the purpose of feature scaling in machine learning?',
                'options': [
                    'Increase model accuracy',
                    'Normalize feature ranges',
                    'Reduce overfitting',
                    'Speed up training'
                ],
                'correct': 1,
                'explanation': 'Feature scaling ensures all features have comparable ranges, preventing features with larger scales from dominating the model.'
            },
            {
                'question': 'Which Python library is best for statistical modeling and hypothesis testing?',
                'options': [
                    'TensorFlow',
                    'SciPy',
                    'Statsmodels',
                    'Keras'
                ],
                'correct': 2,
                'explanation': 'Statsmodels provides comprehensive tools for statistical modeling, hypothesis testing, and statistical analysis.'
            },
            {
                'question': 'What is the curse of dimensionality in machine learning?',
                'options': [
                    'Too many features causing overfitting',
                    'Exponential growth of data space with features',
                    'Limited computational resources',
                    'Poor data quality'
                ],
                'correct': 1,
                'explanation': 'The curse of dimensionality refers to the exponential increase in data volume as dimensions (features) increase.'
            }
        ]
    elif level == 'Advanced':
        return [
            {
                'question': 'Which ensemble method combines multiple weak learners to create a strong learner?',
                'options': [
                    'Random Forest',
                    'Gradient Boosting',
                    'Bagging',
                    'Stacking'
                ],
                'correct': 1,
                'explanation': 'Gradient Boosting builds models sequentially, with each new model correcting errors of the previous ones.'
            },
            {
                'question': 'What is the primary advantage of using deep learning for image recognition?',
                'options': [
                    'Faster training',
                    'Automatic feature extraction',
                    'Better interpretability',
                    'Lower computational cost'
                ],
                'correct': 1,
                'explanation': 'Deep learning automatically learns hierarchical features from raw pixel data, eliminating manual feature engineering.'
            },
            {
                'question': 'Which technique is used to prevent overfitting in neural networks?',
                'options': [
                    'Increasing network size',
                    'Dropout regularization',
                    'Higher learning rate',
                    'More training data'
                ],
                'correct': 1,
                'explanation': 'Dropout randomly deactivates neurons during training, preventing the network from memorizing training data.'
            },
            {
                'question': 'What is the purpose of the bias-variance tradeoff in machine learning?',
                'options': [
                    'Balance model complexity and generalization',
                    'Optimize training time',
                    'Reduce computational cost',
                    'Improve data preprocessing'
                ],
                'correct': 0,
                'explanation': 'The bias-variance tradeoff helps find the sweet spot between underfitting (high bias) and overfitting (high variance).'
            },
            {
                'question': 'Which algorithm is best suited for natural language processing tasks?',
                'options': [
                    'Decision Trees',
                    'Support Vector Machines',
                    'Transformers',
                    'K-Means Clustering'
                ],
                'correct': 2,
                'explanation': 'Transformers, particularly models like BERT and GPT, have revolutionized NLP with their attention mechanisms.'
            }
        ]
    else:
        return get_beginner_questions()

def get_database_administrator_questions(level):
    """Generate Database Administrator specific questions based on level"""
    if level == 'Beginner':
        return [
            {
                'question': 'What does DBMS stand for?',
                'options': [
                    'Data Backup Management System',
                    'Database Management System',
                    'Data Base Machine System',
                    'Database Monitoring System'
                ],
                'correct': 1,
                'explanation': 'DBMS stands for Database Management System, which manages databases and provides interfaces to interact with them.'
            },
            {
                'question': 'Which language is used to interact with relational databases?',
                'options': [
                    'HTML',
                    'CSS',
                    'SQL',
                    'Python'
                ],
                'correct': 2,
                'explanation': 'SQL (Structured Query Language) is the standard language for interacting with relational databases.'
            },
            {
                'question': 'What is a primary key in a database table?',
                'options': [
                    'A duplicate value',
                    'A unique identifier',
                    'A foreign column',
                    'A NULL value'
                ],
                'correct': 1,
                'explanation': 'A primary key is a unique identifier for each record in a database table.'
            },
            {
                'question': 'Which SQL command is used to retrieve data from a table?',
                'options': [
                    'INSERT',
                    'UPDATE',
                    'SELECT',
                    'DELETE'
                ],
                'correct': 2,
                'explanation': 'SELECT is used to retrieve data from database tables.'
            },
            {
                'question': 'What does NULL represent in a database?',
                'options': [
                    'Zero',
                    'Blank space',
                    'Unknown value',
                    'Default value'
                ],
                'correct': 2,
                'explanation': 'NULL represents an unknown or missing value in a database.'
            }
        ]
    elif level == 'Intermediate':
        return [
            {
                'question': 'Which SQL clause is used to filter records?',
                'options': [
                    'GROUP BY',
                    'WHERE',
                    'ORDER BY',
                    'JOIN'
                ],
                'correct': 1,
                'explanation': 'WHERE clause is used to filter records based on specified conditions.'
            },
            {
                'question': 'Which JOIN returns only matching records from both tables?',
                'options': [
                    'LEFT JOIN',
                    'RIGHT JOIN',
                    'INNER JOIN',
                    'FULL JOIN'
                ],
                'correct': 2,
                'explanation': 'INNER JOIN returns only records that have matching values in both tables.'
            },
            {
                'question': 'What is the primary purpose of database indexing?',
                'options': [
                    'Store data',
                    'Improve query performance',
                    'Delete records',
                    'Backup data'
                ],
                'correct': 1,
                'explanation': 'Indexes are primarily used to improve the speed of data retrieval operations.'
            },
            {
                'question': 'Which command removes all rows from a table quickly?',
                'options': [
                    'DELETE',
                    'REMOVE',
                    'TRUNCATE',
                    'DROP'
                ],
                'correct': 2,
                'explanation': 'TRUNCATE removes all rows from a table quickly and is more efficient than DELETE for removing all data.'
            },
            {
                'question': 'What does the GROUP BY clause do in SQL?',
                'options': [
                    'Sorts data',
                    'Filters rows',
                    'Groups similar values',
                    'Deletes duplicates'
                ],
                'correct': 2,
                'explanation': 'GROUP BY groups rows that have the same values in specified columns into summary rows.'
            }
        ]
    elif level == 'Advanced':
        return [
            {
                'question': 'Which type of index defines the physical order of data in a table?',
                'options': [
                    'Non-clustered',
                    'Clustered',
                    'Unique',
                    'Composite'
                ],
                'correct': 1,
                'explanation': 'Clustered index determines the physical order of data in a table.'
            },
            {
                'question': 'What is database normalization?',
                'options': [
                    'Data duplication',
                    'Data organization to reduce redundancy',
                    'Data deletion',
                    'Data sorting'
                ],
                'correct': 1,
                'explanation': 'Normalization is the process of organizing data to reduce redundancy and improve data integrity.'
            },
            {
                'question': 'What causes a database deadlock?',
                'options': [
                    'Too many tables',
                    'Two transactions waiting on each other',
                    'Missing index',
                    'Duplicate data'
                ],
                'correct': 1,
                'explanation': 'Deadlock occurs when two or more transactions are waiting for each other to release locks.'
            },
            {
                'question': 'Which normal form removes partial dependencies?',
                'options': [
                    '1NF',
                    '2NF',
                    '3NF',
                    'BCNF'
                ],
                'correct': 1,
                'explanation': 'Second Normal Form (2NF) removes partial dependencies by ensuring all non-key attributes are fully dependent on the primary key.'
            },
            {
                'question': 'What is the purpose of database backup and recovery?',
                'options': [
                    'Improve performance',
                    'Protect against data loss',
                    'Reduce storage space',
                    'Speed up queries'
                ],
                'correct': 1,
                'explanation': 'Backup and recovery protect against data loss due to hardware failure, corruption, or human error.'
            }
        ]
    else:
        return get_beginner_questions()

def get_level_questions(level):
    """Get questions based on user level"""
    if level == 'Beginner':
        return get_beginner_questions()
    elif level == 'Intermediate':
        return get_intermediate_questions()
    elif level == 'Advanced':
        return get_advanced_questions()
    else:
        return get_beginner_questions()  # Default to beginner
