"""
Seed dataset for initial gamified roadmaps.

This is intentionally small and curated so users can start immediately.
Unlock logic is handled by `roadmaps/views.py`:
  - Step unlocked by previous step completion (based on required resources)
  - Step completed when all required resources for that step are completed
"""


def yt_channel(channel_name: str, channel_id: str, description: str = "", estimated_minutes: int = 120) -> dict:
    """Return a direct YouTube channel URL instead of search results"""
    return {
        "resource_type": "youtube",
        "title": f"YouTube: {channel_name}",
        "description": description or f"Best YouTube channel for {channel_name}",
        "url": f"https://www.youtube.com/{channel_id}",
        "estimated_minutes": estimated_minutes,
    }


SEED_ROLES = [
    {
        "name": "Junior Software Developer/Engineer",
        "slug": "junior-software-developer",
        "summary": "Write code, fix bugs, and build working features with a learning mindset.",
        "description": "You will learn core programming fundamentals, debugging practices, version control, and algorithmic thinking.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Python fundamentals",
                "description": "Learn the basics of Python syntax and program flow.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Python Tutorial",
                        "url": "https://docs.python.org/3/tutorial/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Corey Schafer Python Tutorials", "@coreyms", "High-quality Python tutorials", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Python for Everybody",
                        "description": "University of Michigan's comprehensive Python course",
                        "url": "https://www.coursera.org/learn/python",
                        "difficulty_level": "Beginner",
                        "duration": "3 months",
                        "rating": 4.8,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Charles Severance",
                        "order": 1
                    },
                    {
                        "platform": "youtube",
                        "title": "Python Tutorial for Beginners",
                        "description": "Complete Python programming tutorial series for free",
                        "url": "https://www.youtube.com/playlist?list=PL-osi7n2yp6ZcJ8d7UD5pQ",
                        "difficulty_level": "Beginner",
                        "duration": "8 hours",
                        "rating": 4.7,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Corey Schafer",
                        "order": 2
                    }
                ]
            },
            {
                "level": "Intermediate", 
                "order": 2,
                "title": "Git + everyday workflow",
                "description": "Learn branching/merging concepts and a practical Git workflow.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Atlassian Git Tutorials",
                        "url": "https://www.atlassian.com/git/tutorials",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Git Tutorial Series", "@TechWorldwithNana", "Git and DevOps tutorials", 120),
                ],
                "course_recommendations": [
                    {
                        "platform": "udemy",
                        "title": "Git Complete Course",
                        "description": "Master Git and GitHub from scratch",
                        "url": "https://www.udemy.com/course/git-complete/",
                        "difficulty_level": "Beginner to Intermediate",
                        "duration": "8 hours",
                        "rating": 4.7,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Jason Taylor",
                        "order": 1
                    },
                    {
                        "platform": "coursera",
                        "title": "Version Control with Git",
                        "description": "Learn Git workflows and best practices",
                        "url": "https://www.coursera.org/learn/git",
                        "difficulty_level": "Intermediate",
                        "duration": "1 month",
                        "rating": 4.5,
                        "is_paid": False,
                        "instructor": "Atlassian",
                        "order": 2
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Algorithms thinking",
                "description": "Build intuition for problem solving with data structures and algorithms.",
                "required_resources": [
                    {
                        "resource_type": "course",
                        "title": "MIT OCW: Introduction to Algorithms",
                        "url": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/",
                        "estimated_minutes": 240,
                    },
                    yt_channel("Introduction to Algorithms", "@mitocw", "MIT OpenCourseWare algorithms", 200),
                ],
            },
        ],
    },
    {
        "name": "Web Developer",
        "slug": "web-developer",
        "summary": "Build websites and web apps (frontend, backend, or both).",
        "description": "You’ll learn the building blocks of the web, JavaScript interaction, and how browsers/web platforms work.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "HTML foundations",
                "description": "Learn semantic HTML and how pages are structured.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN Learn: HTML",
                        "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Web Dev Simplified", "@WebDevSimplified", "HTML and web development tutorials", 120),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "JavaScript for the web",
                "description": "Learn core JS and how it powers interactive web experiences.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN Learn: JavaScript",
                        "url": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript",
                        "estimated_minutes": 160,
                    },
                    yt_channel("JavaScript Mastery", "@JavaScriptMastery", "JavaScript and modern web development", 160),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Web APIs",
                "description": "Learn how the browser exposes features through Web APIs.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN Learn: Client-side Web APIs",
                        "url": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Web Dev Simplified", "@WebDevSimplified", "Web APIs and JavaScript tutorials", 180),
                ],
            },
        ],
    },
    {
        "name": "Full Stack Developer",
        "slug": "full-stack-developer",
        "summary": "Work on both frontend and backend development end-to-end.",
        "description": "You’ll learn how to build backend features with Django, handle forms, and expose APIs with Django REST Framework.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Django basics",
                "description": "Build your first Django app and understand request/response.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Django Tutorial (official docs)",
                        "url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
                        "estimated_minutes": 160,
                    },
                    yt_channel("Programming with Mosh", "@programmingwithmosh", "Python and Django backend tutorials", 150),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Forms and validation",
                "description": "Learn how to collect and validate user input using Django forms.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Django Forms (official docs)",
                        "url": "https://docs.djangoproject.com/en/stable/topics/forms/",
                        "estimated_minutes": 140,
                    },
                    yt_channel("Programming with Mosh", "@programmingwithmosh", "Django forms and validation", 120),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "APIs with DRF",
                "description": "Build REST endpoints and serialize data for frontends/mobile apps.",
                "required_resources": [
                    {
                        "resource_type": "course",
                        "title": "Django REST Framework Quickstart",
                        "url": "https://www.django-rest-framework.org/tutorial/quickstart/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("TechWorld with Nana", "@TechWorldwithNana", "Django REST API tutorials", 170),
                ],
            },
        ],
    },
    {
        "name": "Data Analyst",
        "slug": "data-analyst",
        "summary": "Analyze datasets and turn data into decisions.",
        "description": "You’ll learn SQL fundamentals, use Python data tools, and interpret/communicate results.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "SQL foundations",
                "description": "Learn SELECT queries, filtering, joins, and aggregation.",
                "required_resources": [
                    {
                        "resource_type": "course",
                        "title": "Mode SQL Tutorial",
                        "url": "https://mode.com/sql-tutorial/",
                        "estimated_minutes": 160,
                    },
                    yt_channel("Joey Blue", "@joeyblue1", "SQL and database tutorials for beginners", 150),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Pandas and data wrangling",
                "description": "Learn how to load, clean, and transform data with pandas.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Pandas Getting Started",
                        "url": "https://pandas.pydata.org/docs/getting_started/index.html",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Keith Galli", "@KeithGalli", "Pandas data analysis tutorials", 170),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Data visualization with Python",
                "description": "Communicate insights using plots and charting best practices.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Matplotlib Tutorials",
                        "url": "https://matplotlib.org/stable/tutorials/index.html",
                        "estimated_minutes": 160,
                    },
                    yt_channel("NeuralNine", "@NeuralNine", "Data visualization with Python", 160),
                ],
            },
        ],
    },
    {
        "name": "Cybersecurity Analyst",
        "slug": "cybersecurity-analyst",
        "summary": "Protect systems from security threats and investigate vulnerabilities.",
        "description": "You’ll learn common web/app risks, practice hands-on security basics, and understand cybersecurity frameworks.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "OWASP Top 10",
                "description": "Understand common security risks and how they show up in real apps.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "OWASP Top 10",
                        "url": "https://owasp.org/www-project-top-ten/",
                        "estimated_minutes": 90,
                    },
                    yt_channel("NetworkChuck", "@NetworkChuck", "Cybersecurity basics and tutorials", 90),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Hands-on security practice",
                "description": "Follow beginner paths and learn by doing (labs/challenges).",
                "required_resources": [
                    {
                        "resource_type": "course",
                        "title": "TryHackMe Paths",
                        "url": "https://tryhackme.com/paths",
                        "estimated_minutes": 240,
                    },
                    yt_channel("John Hammond", "@_JohnHammond", "TryHackMe and security walkthroughs", 240),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Cybersecurity frameworks",
                "description": "Learn structured approaches for security governance and risk management.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "NIST Cybersecurity Framework",
                        "url": "https://www.nist.gov/cyberframework",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Professor Messer", "@professormesser", "NIST framework and security", 120),
                ],
            },
        ],
    },
    {
        "name": "Game Developer",
        "slug": "game-developer",
        "summary": "Develop software specifically for gaming platforms.",
        "description": "You’ll learn core game development concepts, scripting, and how to build playable interactive experiences.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Build your first 2D game",
                "description": "Learn the basic loop: scenes, nodes, input, and gameplay logic.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Godot: First 2D Game",
                        "url": "https://docs.godotengine.org/en/stable/getting_started/first_2d_game/index.html",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Godot Engine", "@GodotEngineOfficial", "Godot 2D game development", 180),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "GDScript basics",
                "description": "Learn scripting fundamentals for game behavior.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Godot: GDScript Basics",
                        "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html",
                        "estimated_minutes": 160,
                    },
                    yt_channel("HeartBeast", "@uheartbeast", "GDScript and Godot scripting", 160),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "First 3D game",
                "description": "Extend skills from 2D to 3D and learn core 3D patterns.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Godot: First 3D Game",
                        "url": "https://docs.godotengine.org/en/stable/tutorials/3d/your_first_3d_game/index.html",
                        "estimated_minutes": 200,
                    },
                    yt_channel("BornCG", "@BornCG", "Godot 3D game development", 200),
                ],
            },
        ],
    },
    {
        "name": "Technical Support/Support Engineer (L1/L2)",
        "slug": "technical-support-l1-l2",
        "summary": "Troubleshoot issues and help users resolve problems.",
        "description": "You’ll learn fundamentals of networking and OS basics, then build practical debugging/troubleshooting habits.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "HTTP status codes & web troubleshooting",
                "description": "Understand what common HTTP responses mean during real issues.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN: HTTP Status Codes",
                        "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status",
                        "estimated_minutes": 60,
                    },
                    yt_channel("Codecademy", "@codecademy", "HTTP status codes and web basics", 60),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Linux fundamentals",
                "description": "Learn the basics of navigating and using Linux systems.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Linux Journey",
                        "url": "https://linuxjourney.com/",
                        "estimated_minutes": 140,
                    },
                    yt_channel("Chris Titus Tech", "@christitustech", "Linux command line basics", 140),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Networking basics for support",
                "description": "Understand core networking concepts so you can explain fixes clearly.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Cisco Networking Basics",
                        "url": "https://www.cisco.com/site/us/en/learn/networking.html",
                        "estimated_minutes": 120,
                    },
                    yt_channel("CertBros", "@CertBros", "Networking fundamentals", 120),
                ],
            },
        ],
    },
    {
        "name": "DevOps Engineer (Trainee)",
        "slug": "devops-engineer-trainee",
        "summary": "Automate workflows, manage deployments, and build reliable pipelines.",
        "description": "You’ll learn container basics, CI/CD workflows, and how orchestration works at a high level.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Docker fundamentals",
                "description": "Understand containers and how to run apps consistently.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Docker: Get Started",
                        "url": "https://docs.docker.com/get-started/",
                        "estimated_minutes": 150,
                    },
                    yt_channel("TechWorld with Nana", "@TechWorldwithNana", "Docker containerization tutorials", 150),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "GitHub Actions",
                "description": "Learn CI workflows to test/build/deploy automatically.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "GitHub Actions: Quickstart",
                        "url": "https://docs.github.com/en/actions/quickstart",
                        "estimated_minutes": 120,
                    },
                    yt_channel("GitHub", "@GitHub", "GitHub Actions CI/CD workflows", 120),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Kubernetes basics",
                "description": "Understand core concepts behind orchestration.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Kubernetes Basics (official docs)",
                        "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/",
                        "estimated_minutes": 200,
                    },
                    yt_channel("Hussein Nasser", "@hnasr", "Kubernetes and infrastructure", 200),
                ],
            },
        ],
    },
    {
        "name": "Database Administrator (Trainee)",
        "slug": "database-administrator-trainee",
        "summary": "Manage, secure, and maintain databases.",
        "description": "You’ll learn core database concepts, SQL practice, and how to think about reliability and backups.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "SQL essentials",
                "description": "Build confidence with SELECTs, filtering, joins, and grouping.",
                "required_resources": [
                    {
                        "resource_type": "course",
                        "title": "Mode SQL Tutorial",
                        "url": "https://mode.com/sql-tutorial/",
                        "estimated_minutes": 160,
                    },
                    yt_channel("Alex The Analyst", "@AlexTheAnalyst", "SQL for data analysts", 160),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Indexing & query performance",
                "description": "Learn the basics of indexes and query plans at a conceptual level.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "PostgreSQL: Indexes",
                        "url": "https://www.postgresql.org/docs/current/indexes.html",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Postgres Official", "@PostgreSQL", "PostgreSQL indexing tutorials", 120),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Backup & recovery mindset",
                "description": "Understand backup strategies and recovery concepts.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "PostgreSQL: Backup and restore",
                        "url": "https://www.postgresql.org/docs/current/backup.html",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Postgres Official", "@PostgreSQL", "PostgreSQL backup and recovery", 120),
                ],
            },
        ],
    },
    {
        "name": "Network/System Engineer (Trainee)",
        "slug": "network-system-engineer-trainee",
        "summary": "Work with networking infrastructure, servers, and security fundamentals.",
        "description": "You’ll learn core networking, practical OS knowledge, and secure remote access concepts.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "TCP/IP fundamentals",
                "description": "Learn how packets, sockets, and protocols relate in practice.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Beej: Guide to Network Programming",
                        "url": "https://beej.us/guide/bgnet/",
                        "estimated_minutes": 160,
                    },
                    yt_channel("PowerCert", "@PowerCert", "TCP/IP networking tutorials", 160),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Linux administration basics",
                "description": "Learn everyday server tasks and command-line fundamentals.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Linux Journey",
                        "url": "https://linuxjourney.com/",
                        "estimated_minutes": 140,
                    },
                    yt_channel("Learn Linux TV", "@LearnLinuxTV", "Linux administration", 140),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Secure SSH access",
                "description": "Understand how SSH works and common configuration options.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "OpenSSH Manual",
                        "url": "https://www.openssh.com/manual.html",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Chris Greer", "@ChrisGreer", "SSH and security best practices", 120),
                ],
            },
        ],
    },
    {
        "name": "Automation Tester",
        "slug": "automation-tester",
        "summary": "Automate testing to improve reliability and speed.",
        "description": "You’ll learn browser automation basics, build tests with pytest, and practice modern end-to-end testing patterns.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Selenium basics",
                "description": "Learn how to automate browsers and interact with web elements.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Selenium Documentation",
                        "url": "https://www.selenium.dev/documentation/",
                        "estimated_minutes": 140,
                    },
                    yt_channel("Automate Together", "@automate_together", "Selenium automation testing", 140),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "pytest (test runner)",
                "description": "Learn how to write and run test suites with pytest.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "pytest: Getting Started",
                        "url": "https://docs.pytest.org/en/stable/getting-started.html",
                        "estimated_minutes": 100,
                    },
                    yt_channel("AnthonyWritesCode", "@anthonywritescode", "pytest testing tutorials", 100),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Playwright for E2E tests",
                "description": "Use a modern automation framework for end-to-end testing workflows.",
                "required_resources": [
                    {
                        "resource_type": "course",
                        "title": "Playwright: Intro",
                        "url": "https://playwright.dev/docs/intro",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Automation Step by Step", "@automationstepbystep", "Playwright E2E testing", 120),
                ],
            },
        ],
    },
    {
        "name": "UI/UX Designer",
        "slug": "ui-ux-designer",
        "summary": "Design the user interface and user experience.",
        "description": "You’ll learn essential design tooling, creative problem framing, and accessibility best practices.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Figma fundamentals",
                "description": "Learn the basics of designing screens and components.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Figma Learn",
                        "url": "https://help.figma.com/hc/en-us/sections/14219042676889-Figma-Learn",
                        "estimated_minutes": 120,
                    },
                    yt_channel("Figma", "@Figma", "Figma design tutorials", 120),
                ],
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Design thinking",
                "description": "Practice a structured way to understand users and define problems.",
                "required_resources": [
                    {
                        "resource_type": "article",
                        "title": "Stanford d.school: Design Thinking (Bootleg)",
                        "url": "https://dschool.stanford.edu/resources/design-thinking-bootleg",
                        "estimated_minutes": 90,
                    },
                    yt_channel("AJ&Smart", "@AJSmartDesign", "Design thinking process", 90),
                ],
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Accessibility (WCAG basics)",
                "description": "Learn accessibility fundamentals so designs work for everyone.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "W3C: Intro to Accessibility",
                        "url": "https://www.w3.org/WAI/intro-accessibility/",
                        "estimated_minutes": 120,
                    },
                    yt_channel("A11y Camp", "@a11ycamp", "WCAG accessibility tutorial basics", 120),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "Frontend Developer",
        "slug": "frontend-developer",
        "summary": "Create beautiful, responsive user interfaces that users love to interact with.",
        "description": "You will master HTML, CSS, JavaScript, and modern frontend frameworks to build stunning web applications.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "HTML & CSS fundamentals",
                "description": "Learn the building blocks of web pages and how to style them beautifully.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN Web Docs: HTML Basics",
                        "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML",
                        "estimated_minutes": 180,
                    },
                    {
                        "resource_type": "docs",
                        "title": "MDN Web Docs: CSS Basics",
                        "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS",
                        "estimated_minutes": 240,
                    },
                    yt_channel("HTML CSS Tutorials", "@TraversyMedia", "Web development tutorials", 180),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "HTML, CSS, and Javascript for Web Developers",
                        "description": "Johns Hopkins University's comprehensive web development course",
                        "url": "https://www.coursera.org/learn/html-css-javascript",
                        "difficulty_level": "Beginner",
                        "duration": "5 weeks",
                        "rating": 4.7,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Yaakov Chaikin",
                        "order": 1
                    },
                    {
                        "platform": "youtube",
                        "title": "JavaScript Complete Tutorial",
                        "description": "Comprehensive JavaScript tutorial series for free",
                        "url": "https://www.youtube.com/playlist?list=PLWKhmJXUksC4Yt3c_iE0U",
                        "difficulty_level": "Beginner to Advanced",
                        "duration": "12 hours",
                        "rating": 4.8,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Traversy Media",
                        "order": 2
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "JavaScript & DOM manipulation",
                "description": "Add interactivity and dynamic behavior to web pages using JavaScript.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN Web Docs: JavaScript Guide",
                        "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
                        "estimated_minutes": 300,
                    },
                    yt_channel("JavaScript Mastery", "@JavaScriptMastery", "JavaScript tutorials", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "youtube",
                        "title": "JavaScript DOM Manipulation Tutorial",
                        "description": "Learn JavaScript DOM manipulation with practical examples",
                        "url": "https://www.youtube.com/playlist?list=PL4oUd9U2wPA2pJvM8M6nT",
                        "difficulty_level": "Intermediate",
                        "duration": "6 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Web Dev Simplified",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Web APIs",
                "description": "Learn how the browser exposes features through Web APIs.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "MDN Web APIs",
                        "url": "https://developer.mozilla.org/en-US/docs/Web/API",
                        "estimated_minutes": 200,
                    },
                    yt_channel("Web Dev Simplified", "@WebDevSimplified", "Web APIs and async JavaScript", 140),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "Backend Developer",
        "slug": "backend-developer",
        "summary": "Build robust server-side applications, APIs, and database systems.",
        "description": "You will learn server-side programming, database design, API development, and system architecture.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Python basics for backend",
                "description": "Master Python fundamentals with a focus on backend development.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Python Tutorial",
                        "url": "https://docs.python.org/3/tutorial/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Backend Development", "@TraversyMedia", "Backend development tutorials", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Python for Everybody",
                        "description": "University of Michigan's comprehensive Python course",
                        "url": "https://www.coursera.org/learn/python",
                        "difficulty_level": "Beginner",
                        "duration": "3 months",
                        "rating": 4.8,
                        "is_paid": False,
                        "instructor": "Charles Severance",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Django web framework",
                "description": "Learn to build web applications using Django framework.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Django Tutorial",
                        "url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
                        "estimated_minutes": 240,
                    },
                    yt_channel("Django Tutorials", "@coreyms", "Django web framework tutorials", 180),
                ],
                "course_recommendations": [
                    {
                        "platform": "youtube",
                        "title": "Django Tutorial for Beginners",
                        "description": "Complete Django web framework tutorial series",
                        "url": "https://www.youtube.com/playlist?list=PL-osi7n2yp6ZcJ8d7UD5pQ",
                        "difficulty_level": "Beginner to Intermediate",
                        "duration": "10 hours",
                        "rating": 4.7,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Corey Schafer",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "APIs with DRF",
                "description": "Build REST endpoints and serialize data for frontends/mobile apps.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Django REST Framework Tutorial",
                        "url": "https://www.django-rest-framework.org/tutorial/quickstart/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Corey Schafer", "@coreyms", "Django REST API tutorial", 160),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "Data Scientist",
        "slug": "data-scientist",
        "summary": "Extract insights from data using statistics, machine learning, and visualization.",
        "description": "You will learn data analysis, machine learning, statistical modeling, and data visualization techniques.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Python for data science",
                "description": "Learn Python libraries essential for data science: NumPy, Pandas, Matplotlib.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Python Data Science Handbook",
                        "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
                        "estimated_minutes": 300,
                    },
                    yt_channel("Python Data Science", "@sentdex", "Data science tutorials", 180),
                ],
                "course_recommendations": [
                    {
                        "platform": "youtube",
                        "title": "Python for Data Science Tutorial",
                        "description": "Complete Python data science tutorial series",
                        "url": "https://www.youtube.com/playlist?list=PL-osi7n2yp6ZcJ8d7UD5pQ",
                        "difficulty_level": "Beginner",
                        "duration": "12 hours",
                        "rating": 4.8,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Corey Schafer",
                        "order": 1
                    },
                    {
                        "platform": "khan",
                        "title": "Statistics and Probability",
                        "description": "Free statistics and probability course",
                        "url": "https://www.khanacademy.org/math/statistics-probability",
                        "difficulty_level": "Beginner",
                        "duration": "Self-paced",
                        "rating": 4.5,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Khan Academy",
                        "order": 2
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Statistics & probability",
                "description": "Understand statistical concepts and probability theory for data analysis.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Khan Academy: Statistics",
                        "url": "https://www.khanacademy.org/math/statistics-probability",
                        "estimated_minutes": 240,
                    },
                    yt_channel("StatQuest", "@statquest", "Statistics and probability", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "youtube",
                        "title": "Statistics with Python Tutorial",
                        "description": "Learn statistics using Python with free tutorials",
                        "url": "https://www.youtube.com/playlist?list=PL-osi7n2yp6ZcJ8d7UD5pQ",
                        "difficulty_level": "Intermediate",
                        "duration": "8 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "StatQuest",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Data visualization with Python",
                "description": "Communicate insights using plots and charting best practices.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Matplotlib Documentation",
                        "url": "https://matplotlib.org/stable/contents.html",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Data Daft", "@DataDaft", "Data visualization with Python", 140),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "DevOps Engineer",
        "slug": "devops-engineer",
        "summary": "Bridge development and operations through automation, CI/CD, and cloud infrastructure.",
        "description": "You will learn containerization, infrastructure as code, CI/CD pipelines, and cloud platforms.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Linux & command line",
                "description": "Master Linux fundamentals and command-line operations essential for DevOps.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Linux Journey",
                        "url": "https://linuxjourney.com/",
                        "estimated_minutes": 200,
                    },
                    yt_channel("Linux Command Line", "@DistroTube", "Linux and command line", 180),
                ],
                "course_recommendations": [
                    {
                        "platform": "youtube",
                        "title": "Linux Command Line Tutorial",
                        "description": "Complete Linux command line tutorial for beginners",
                        "url": "https://www.youtube.com/playlist?list=PL-osi7n2yp6ZcJ8d7UD5pQ",
                        "difficulty_level": "Beginner",
                        "duration": "6 hours",
                        "rating": 4.7,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Corey Schafer",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Docker & containers",
                "description": "Learn containerization basics and how to build and manage Docker containers.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Docker Documentation",
                        "url": "https://docs.docker.com/get-started/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("TechWorld with Nana", "@TechWorldwithNana", "Docker and DevOps", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "youtube",
                        "title": "Docker Tutorial for Beginners",
                        "description": "Complete Docker container tutorial series",
                        "url": "https://www.youtube.com/playlist?list=PL-osi7n2yp6ZcJ8d7UD5pQ",
                        "difficulty_level": "Beginner to Intermediate",
                        "duration": "8 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "FreeCodeCamp",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Kubernetes basics",
                "description": "Understand core concepts behind orchestration.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Kubernetes Documentation",
                        "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/",
                        "estimated_minutes": 200,
                    },
                    yt_channel("TechWorld with Nana", "@TechWorldwithNana", "Kubernetes tutorials", 160),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "Cybersecurity Analyst",
        "slug": "cybersecurity-analyst",
        "summary": "Protect systems, networks, and data from cyber threats and attacks.",
        "description": "You will learn security fundamentals, threat analysis, vulnerability assessment, and security tools.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Security fundamentals",
                "description": "Learn core cybersecurity concepts and terminology.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "NIST Cybersecurity Framework",
                        "url": "https://www.nist.gov/cyberframework",
                        "estimated_minutes": 180,
                    },
                    yt_channel("NetworkChuck", "@NetworkChuck", "Cybersecurity fundamentals", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Google Cybersecurity Professional Certificate",
                        "description": "Launch your career in cybersecurity",
                        "url": "https://www.coursera.org/professional-certificates/google-cybersecurity",
                        "difficulty_level": "Beginner",
                        "duration": "6 months",
                        "rating": 4.7,
                        "is_paid": False,
                        "price": "Free/month",
                        "instructor": "Google",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Network security",
                "description": "Understand network protocols and how to secure network infrastructure.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Cisco Networking Basics",
                        "url": "https://www.cisco.com/c/en/us/training-events/training-certifications/training-certifications.html",
                        "estimated_minutes": 200,
                    },
                    yt_channel("Professor Messer", "@professormesser", "Network security", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "comptia",
                        "title": "CompTIA Network+ Training",
                        "description": "Comprehensive Network+ certification training materials",
                        "url": "https://www.comptia.org/training/network",
                        "difficulty_level": "Intermediate",
                        "duration": "Self-paced",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "CompTIA",
                        "order": 1
                    }
                ]
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "Game Developer",
        "slug": "game-developer",
        "summary": "Create engaging games and interactive experiences using game engines and programming.",
        "description": "You will learn game development fundamentals, game engines, physics, and game design principles.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Game development basics",
                "description": "Understand game loops, sprites, and basic game mechanics.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Unity Learn",
                        "url": "https://learn.unity.com/",
                        "estimated_minutes": 200,
                    },
                    yt_channel("Unity", "@unity", "Unity game development basics", 180),
                ],
                "course_recommendations": [
                    {
                        "platform": "udemy",
                        "title": "Unity Game Development: Make 2D & 3D Games",
                        "description": "Complete game development course",
                        "url": "https://www.udemy.com/course/unity-game-development/",
                        "difficulty_level": "Beginner to Advanced",
                        "duration": "51 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Jonathan Weinberger",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "2D game with Unity",
                "description": "Build a complete 2D game using Unity engine.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Unity 2D Documentation",
                        "url": "https://docs.unity3d.com/Packages/com.unity.2d.documentation@latest",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Code Monkey", "@CodeMonkeyUnity", "Unity 2D game development", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Game Design and Development with Unity 2020",
                        "description": "Michigan State University's game development course",
                        "url": "https://www.coursera.org/specializations/game-design-development",
                        "difficulty_level": "Beginner to Intermediate",
                        "duration": "6 months",
                        "rating": 4.8,
                        "is_paid": False,
                        "price": "Free/month",
                        "instructor": "Brian Winn",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "First 3D game",
                "description": "Extend skills from 2D to 3D and learn core 3D patterns.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Unity 3D Documentation",
                        "url": "https://docs.unity3d.com/Manual/index.html",
                        "estimated_minutes": 220,
                    },
                    yt_channel("Unity", "@unity", "Unity 3D game development tutorials", 180),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "IT Support Specialist",
        "slug": "it-support-specialist",
        "summary": "Provide technical assistance and support for computer systems, networks, and software.",
        "description": "You will learn troubleshooting, customer service, system administration, and network fundamentals.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Computer hardware basics",
                "description": "Understand computer components and how they work together.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "PC Building Guide",
                        "url": "https://www.tomshardware.com/reviews/build-your-own-pc,4130.html",
                        "estimated_minutes": 160,
                    },
                    yt_channel("PowerCert", "@PowerCert", "Computer hardware basics", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Google IT Support Professional Certificate",
                        "description": "Launch your career in IT support",
                        "url": "https://www.coursera.org/professional-certificates/google-it-support",
                        "difficulty_level": "Beginner",
                        "duration": "5 months",
                        "rating": 4.8,
                        "is_paid": False,
                        "price": "Free/month",
                        "instructor": "Google",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Operating systems",
                "description": "Learn Windows, macOS, and Linux administration basics.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Windows Administration",
                        "url": "https://docs.microsoft.com/en-us/windows-server/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Chris Titus Tech", "@christitustech", "Windows and Linux tutorials", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "microsoft",
                        "title": "Windows Server Administration",
                        "description": "Learn Windows Server management",
                        "url": "https://docs.microsoft.com/en-us/learn/windows-server/",
                        "difficulty_level": "Intermediate",
                        "duration": "Self-paced",
                        "rating": 4.6,
                        "is_paid": False,
                        "instructor": "Microsoft",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Networking basics for support",
                "description": "Understand core networking concepts so you can explain fixes clearly.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Networking Basics",
                        "url": "https://www.cisco.com/c/en/us/training-events/training-certifications/training-certifications.html",
                        "estimated_minutes": 200,
                    },
                    yt_channel("CertBros", "@CertBros", "Networking fundamentals", 140),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "Database Administrator",
        "slug": "database-administrator",
        "summary": "Manage, maintain, and optimize database systems for performance and reliability.",
        "description": "You will learn database design, SQL, performance tuning, backup strategies, and database security.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "SQL fundamentals",
                "description": "Learn SQL syntax and database concepts.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "SQL Tutorial",
                        "url": "https://www.w3schools.com/sql/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Joey Blue", "@joeyblue1", "SQL and database tutorials", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "SQL for Data Science",
                        "description": "University of California's SQL course",
                        "url": "https://www.coursera.org/learn/sql-for-data-science",
                        "difficulty_level": "Beginner",
                        "duration": "4 weeks",
                        "rating": 4.5,
                        "is_paid": False,
                        "instructor": "Sadie St. Lawrence",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Database design",
                "description": "Learn normalization, indexing, and query optimization.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Database Design Tutorial",
                        "url": "https://www.guru99.com/database-design.html",
                        "estimated_minutes": 160,
                    },
                    yt_channel("Alex The Analyst", "@AlexTheAnalyst", "Database design and SQL", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "udemy",
                        "title": "SQL Database Administration",
                        "description": "Complete database administration course",
                        "url": "https://www.udemy.com/course/database-administration/",
                        "difficulty_level": "Intermediate",
                        "duration": "8 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Imtiaz Ahmad",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Backup & recovery mindset",
                "description": "Understand backup strategies and recovery concepts.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Database Backup Strategies",
                        "url": "https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-strategies-sql-server",
                        "estimated_minutes": 140,
                    },
                    yt_channel("Postgres Official", "@PostgreSQL", "PostgreSQL backup and recovery", 120),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "System Administrator",
        "slug": "system-administrator",
        "summary": "Manage and maintain computer systems, servers, and network infrastructure.",
        "description": "You will learn system administration, scripting, security, and infrastructure management.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Linux administration",
                "description": "Learn Linux system administration fundamentals.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Linux System Administration",
                        "url": "https://www.redhat.com/en/topics/linux",
                        "estimated_minutes": 200,
                    },
                    yt_channel("Learn Linux TV", "@LearnLinuxTV", "Linux system administration", 180),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Linux for System Administrators",
                        "description": "Learn Linux administration skills",
                        "url": "https://www.coursera.org/learn/linux-system-administration",
                        "difficulty_level": "Beginner",
                        "duration": "4 weeks",
                        "rating": 4.7,
                        "is_paid": False,
                        "instructor": "Various",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Windows Server",
                "description": "Learn Windows Server administration and Active Directory.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Windows Server Documentation",
                        "url": "https://docs.microsoft.com/en-us/windows-server/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Windows Server", "@Windows", "Windows Server tutorials", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "microsoft",
                        "title": "Windows Server Administration",
                        "description": "Learn Windows Server management",
                        "url": "https://docs.microsoft.com/en-us/learn/windows-server/",
                        "difficulty_level": "Intermediate",
                        "duration": "Self-paced",
                        "rating": 4.6,
                        "is_paid": False,
                        "instructor": "Microsoft",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Secure SSH access",
                "description": "Understand how SSH works and common configuration options.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "SSH Documentation",
                        "url": "https://www.ssh.com/ssh/",
                        "estimated_minutes": 120,
                    },
                    yt_channel("SSH Tutorial", "@CybersecurityTV", "SSH security", 100),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "QA Engineer",
        "slug": "qa-engineer",
        "summary": "Ensure software quality through testing, automation, and quality assurance processes.",
        "description": "You will learn testing methodologies, automation frameworks, and quality assurance best practices.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Testing fundamentals",
                "description": "Learn software testing concepts and methodologies.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "ISTQB Foundation",
                        "url": "https://www.istqb.org/",
                        "estimated_minutes": 160,
                    },
                    yt_channel("Automation Step by Step", "@automationstepbystep", "Software testing basics", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Software Testing and Automation",
                        "description": "University of Minnesota's testing course",
                        "url": "https://www.coursera.org/learn/software-testing-automation",
                        "difficulty_level": "Beginner",
                        "duration": "4 weeks",
                        "rating": 4.6,
                        "is_paid": False,
                        "instructor": "Various",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Test automation",
                "description": "Learn automated testing with Selenium and other tools.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Selenium Documentation",
                        "url": "https://www.selenium.dev/documentation/",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Automate Together", "@automate_together", "Selenium automation testing", 160),
                ],
                "course_recommendations": [
                    {
                        "platform": "udemy",
                        "title": "Selenium WebDriver with Python",
                        "description": "Complete test automation course",
                        "url": "https://www.udemy.com/course/selenium-webdriver-with-python/",
                        "difficulty_level": "Intermediate",
                        "duration": "24 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Let's Kode It",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Playwright for E2E tests",
                "description": "Use a modern automation framework for end-to-end testing workflows.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Playwright Documentation",
                        "url": "https://playwright.dev/docs/intro",
                        "estimated_minutes": 140,
                    },
                    yt_channel("Automation Step by Step", "@automationstepbystep", "Playwright E2E testing", 120),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
    {
        "name": "UX/UI Designer",
        "slug": "ux-ui-designer",
        "summary": "Create intuitive and beautiful user interfaces and experiences.",
        "description": "You will learn design principles, user research, prototyping, and modern design tools.",
        "steps": [
            {
                "level": "Beginner",
                "order": 1,
                "title": "Design fundamentals",
                "description": "Learn color theory, typography, and design principles.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Design Principles",
                        "url": "https://www.interaction-design.org/literature/topics/design-principles",
                        "estimated_minutes": 180,
                    },
                    yt_channel("Flux Academy", "@FluxAcademy", "Design fundamentals and UX", 140),
                ],
                "course_recommendations": [
                    {
                        "platform": "coursera",
                        "title": "Google UX Design Professional Certificate",
                        "description": "Launch your career in UX design",
                        "url": "https://www.coursera.org/professional-certificates/google-ux-design",
                        "difficulty_level": "Beginner",
                        "duration": "6 months",
                        "rating": 4.8,
                        "is_paid": False,
                        "price": "Free/month",
                        "instructor": "Google",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Intermediate",
                "order": 2,
                "title": "Figma & prototyping",
                "description": "Learn to create interactive prototypes and designs using Figma.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "Figma Documentation",
                        "url": "https://www.figma.com/files/",
                        "estimated_minutes": 160,
                    },
                    yt_channel("Figma", "@Figma", "Figma design tutorials", 120),
                ],
                "course_recommendations": [
                    {
                        "platform": "udemy",
                        "title": "Figma UI UX Design Essentials",
                        "description": "Complete Figma design course",
                        "url": "https://www.udemy.com/course/figma-ui-ux-design-essentials/",
                        "difficulty_level": "Beginner to Intermediate",
                        "duration": "12 hours",
                        "rating": 4.6,
                        "is_paid": False,
                        "price": "Free",
                        "instructor": "Daniel Walter Scott",
                        "order": 1
                    }
                ]
            },
            {
                "level": "Advanced",
                "order": 3,
                "title": "Accessibility (WCAG basics)",
                "description": "Learn accessibility fundamentals so designs work for everyone.",
                "required_resources": [
                    {
                        "resource_type": "docs",
                        "title": "W3C: Intro to Accessibility",
                        "url": "https://www.w3.org/WAI/intro-accessibility/",
                        "estimated_minutes": 120,
                    },
                    yt_channel("A11y Camp", "@a11ycamp", "WCAG accessibility tutorial basics", 120),
                ],
            },
        ],
        "certification_recommendations": [
            {
                "platform": "freecodecamp",
                "title": "freeCodeCamp Python Certification",
                "description": "Validate your Python programming skills with this comprehensive free certification.",
                "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
                "difficulty_level": "Intermediate",
                "duration": "300 hours",
                "rating": 4.8,
                "is_paid": False,
                "price": "Free",
                "provider": "freeCodeCamp",
                "prerequisites": "Basic programming knowledge",
                "order": 1
            },
            {
                "platform": "khan",
                "title": "Khan Academy Computer Programming Certificate",
                "description": "Free certificate covering programming fundamentals and computer science concepts.",
                "url": "https://www.khanacademy.org/computing/computer-programming",
                "difficulty_level": "Beginner",
                "duration": "Self-paced",
                "rating": 4.6,
                "is_paid": False,
                "price": "Free",
                "provider": "Khan Academy",
                "prerequisites": "Basic computer literacy",
                "order": 2
            }
        ]
    },
]

