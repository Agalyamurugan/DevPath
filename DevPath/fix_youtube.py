import re

# Read the file
with open('roadmaps/seed_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Define role-specific replacements (using raw strings to avoid quote issues)
replacements = [
    # Game Developer - Unity 3D
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","unity 3d game tutorial complete", 180\)', 
     r'yt_channel("Unity", "@unity", "Unity 3D game development tutorials", 180)'),
    
    # IT Support Specialist - Hardware
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","computer hardware basics tutorial", 140\)',
     r'yt_channel("PowerCert", "@PowerCert", "Computer hardware basics", 140)'),
    
    # IT Support Specialist - Operating Systems
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","operating systems tutorial windows linux", 160\)',
     r'yt_channel("Chris Titus Tech", "@christitustech", "Windows and Linux tutorials", 160)'),
    
    # IT Support Specialist - Networking
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","computer networking basics tutorial", 140\)',
     r'yt_channel("CertBros", "@CertBros", "Networking fundamentals", 140)'),
    
    # Database Administrator - SQL
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","SQL tutorial for beginners", 140\)',
     r'yt_channel("Joey Blue", "@joeyblue1", "SQL and database tutorials", 140)'),
    
    # Database Administrator - Database Design
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","database design normalization tutorial", 140\)',
     r'yt_channel("Alex The Analyst", "@AlexTheAnalyst", "Database design and SQL", 140)'),
    
    # Database Administrator - Backup/Recovery
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","database backup recovery tutorial", 120\)',
     r'yt_channel("Postgres Official", "@PostgreSQL", "PostgreSQL backup and recovery", 120)'),
    
    # System Administrator - Linux
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","linux system administration tutorial", 180\)',
     r'yt_channel("Learn Linux TV", "@LearnLinuxTV", "Linux system administration", 180)'),
    
    # System Administrator - Windows Server
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","windows server administration tutorial", 160\)',
     r'yt_channel("Windows Server", "@Windows", "Windows Server tutorials", 160)'),
    
    # QA Engineer - Testing Fundamentals
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","software testing tutorial for beginners", 140\)',
     r'yt_channel("Automation Step by Step", "@automationstepbystep", "Software testing basics", 140)'),
    
    # QA Engineer - Selenium
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","selenium test automation tutorial", 160\)',
     r'yt_channel("Automate Together", "@automate_together", "Selenium automation testing", 160)'),
    
    # QA Engineer - Playwright
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","playwright test automation tutorial", 120\)',
     r'yt_channel("Automation Step by Step", "@automationstepbystep", "Playwright E2E testing", 120)'),
    
    # UX/UI Designer - Design Fundamentals
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","design fundamentals tutorial", 140\)',
     r'yt_channel("Flux Academy", "@FluxAcademy", "Design fundamentals and UX", 140)'),
    
    # UX/UI Designer - Figma
    (r'yt_channel\("Tech Tutorials", "@freecodecamp", "Best programming tutorials","figma tutorial for beginners", 120\)',
     r'yt_channel("Figma", "@Figma", "Figma design tutorials", 120)'),
]

# Apply replacements
for old_pattern, new_text in replacements:
    content = re.sub(old_pattern, new_text, content)

# Write back
with open('roadmaps/seed_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements complete!')
