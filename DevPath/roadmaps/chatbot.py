"""
Chatbot system for role recommendations and user assistance
"""

class CareerChatbot:
    def __init__(self):
        self.role_descriptions = {
            'Frontend Developer': {
                'skills': ['HTML', 'CSS', 'JavaScript', 'React', 'Vue.js'],
                'description': 'Build user interfaces and web applications',
                'salary_range': '$60k - $120k',
                'career_path': 'Junior → Mid-level → Senior → Lead Developer'
            },
            'Backend Developer': {
                'skills': ['Python', 'Java', 'Node.js', 'Databases', 'APIs'],
                'description': 'Build server-side applications and systems',
                'salary_range': '$70k - $140k',
                'career_path': 'Junior → Mid-level → Senior → Tech Lead'
            },
            'Full Stack Developer': {
                'skills': ['Frontend', 'Backend', 'Databases', 'DevOps'],
                'description': 'Work across the entire technology stack',
                'salary_range': '$80k - $150k',
                'career_path': 'Junior → Mid-level → Senior → Full Stack Architect'
            },
            'Data Scientist': {
                'skills': ['Python', 'Machine Learning', 'Statistics', 'Data Visualization'],
                'description': 'Analyze data and build predictive models',
                'salary_range': '$90k - $180k',
                'career_path': 'Junior → Mid-level → Senior → Principal Data Scientist'
            },
            'Database Administrator': {
                'skills': ['SQL', 'Database Design', 'Performance Tuning', 'Backup/Recovery'],
                'description': 'Manage and optimize database systems',
                'salary_range': '$70k - $130k',
                'career_path': 'Junior → Mid-level → Senior → Database Architect'
            },
            'DevOps Engineer': {
                'skills': ['Cloud', 'CI/CD', 'Docker', 'Kubernetes', 'Monitoring'],
                'description': 'Automate deployment and infrastructure management',
                'salary_range': '$90k - $160k',
                'career_path': 'Junior → Mid-level → Senior → DevOps Architect'
            },
            'Web Developer': {
                'skills': ['HTML', 'CSS', 'JavaScript', 'CMS', 'E-commerce'],
                'description': 'Build websites and web applications',
                'salary_range': '$50k - $100k',
                'career_path': 'Junior → Mid-level → Senior → Web Development Lead'
            }
        }
        
        self.common_questions = {
            'what skills': 'skills',
            'salary': 'salary_range',
            'how much': 'salary_range',
            'career path': 'career_path',
            'what is': 'description',
            'describe': 'description'
        }

    def get_response(self, user_message):
        """Generate response based on user message"""
        user_message = user_message.lower().strip()
        
        # Greeting responses
        greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon']
        if any(greeting in user_message for greeting in greetings):
            return self.get_greeting_response()
        
        # Help request
        if 'help' in user_message or 'what can you do' in user_message:
            return self.get_help_response()
        
        # Role recommendations
        if 'recommend' in user_message or 'suggest' in user_message or 'which role' in user_message:
            return self.get_role_recommendation(user_message)
        
        # Specific role questions
        for role_name in self.role_descriptions.keys():
            if role_name.lower() in user_message:
                return self.get_role_info(role_name, user_message)
        
        # Skill-based recommendations
        if any(skill in user_message for skill in ['programming', 'coding', 'web', 'data', 'database']):
            return self.get_skill_based_recommendation(user_message)
        
        # Default response
        return self.get_default_response()

    def get_greeting_response(self):
        return """👋 Hello! I'm your Career Assistant Bot! 

I can help you:
• Find the perfect tech role for you
• Learn about different career paths
• Understand required skills and salaries
• Answer questions about tech careers

What would you like to know about?"""

    def get_help_response(self):
        return """🤖 I'm here to help you explore tech careers! 

You can ask me:
• "Which role is right for me?"
• "Tell me about frontend developers"
• "What skills do I need for data science?"
• "How much do backend developers make?"
• "What's the career path for full stack developers?"

What career question can I help with?"""

    def get_role_recommendation(self, user_message):
        """Recommend roles based on user interests"""
        if 'creative' in user_message or 'visual' in user_message or 'design' in user_message:
            return """🎨 Based on your creative interests, I recommend:

**Frontend Developer**
• Create beautiful user interfaces
• Work with design teams
• Use modern frameworks like React and Vue.js
• Salary range: $60k - $120k

**Web Developer**
• Build complete websites
• Work with CMS platforms
• Combine design and technical skills
• Salary range: $50k - $100k

Would you like to know more about either of these roles?"""
        
        elif 'data' in user_message or 'analytics' in user_message or 'numbers' in user_message:
            return """📊 Based on your interest in data, I recommend:

**Data Scientist**
• Analyze complex datasets
• Build machine learning models
• Create data visualizations
• Salary range: $90k - $180k

**Database Administrator**
• Manage database systems
• Optimize data performance
• Ensure data security
• Salary range: $70k - $130k

Would you like to learn more about data science or database roles?"""
        
        elif 'system' in user_message or 'server' in user_message or 'backend' in user_message:
            return """⚙️ Based on your system interests, I recommend:

**Backend Developer**
• Build server applications
• Design APIs and databases
• Work with system architecture
• Salary range: $70k - $140k

**DevOps Engineer**
• Automate deployments
• Manage cloud infrastructure
• Optimize system performance
• Salary range: $90k - $160k

Would you like to explore backend or DevOps careers?"""
        
        else:
            return """🚀 Here are some popular tech roles to consider:

**Full Stack Developer** - Work across entire stack ($80k - $150k)
**Frontend Developer** - Build user interfaces ($60k - $120k)  
**Backend Developer** - Build server systems ($70k - $140k)
**Data Scientist** - Analyze data ($90k - $180k)

What type of work interests you most?"""

    def get_role_info(self, role_name, user_message):
        """Provide specific information about a role"""
        if role_name not in self.role_descriptions:
            return f"I don't have information about {role_name}. Would you like me to tell you about available roles?"
        
        role_info = self.role_descriptions[role_name]
        
        # Determine what specific information the user wants
        for keyword, info_type in self.common_questions.items():
            if keyword in user_message:
                if info_type == 'skills':
                    return f"""💻 **{role_name} Required Skills:**

{', '.join(role_info['skills'])}

Want to know about salary or career path for this role?"""
                
                elif info_type == 'salary_range':
                    return f"""💰 **{role_name} Salary Range:**

{role_info['salary_range']}

This can vary based on experience, location, and company size."""
                
                elif info_type == 'career_path':
                    return f"""📈 **{role_name} Career Path:**

{role_info['career_path']}

Would you like to know about required skills?"""
                
                elif info_type == 'description':
                    return f"""📝 **{role_name} Role Description:**

{role_info['description']}

Would you like to know about skills or salary?"""
        
        # General role information
        return f"""🎯 **{role_name}**

**Description:** {role_info['description']}

**Key Skills:** {', '.join(role_info['skills'])}

**Salary Range:** {role_info['salary_range']}

**Career Path:** {role_info['career_path']}

What would you like to know more about?"""

    def get_skill_based_recommendation(self, user_message):
        """Recommend roles based on mentioned skills"""
        if 'web' in user_message or 'html' in user_message or 'css' in user_message:
            return self.get_role_info('Web Developer', 'tell me about web developer')
        elif 'data' in user_message:
            return self.get_role_info('Data Scientist', 'tell me about data scientist')
        elif 'database' in user_message or 'sql' in user_message:
            return self.get_role_info('Database Administrator', 'tell me about database administrator')
        elif 'frontend' in user_message:
            return self.get_role_info('Frontend Developer', 'tell me about frontend developer')
        elif 'backend' in user_message:
            return self.get_role_info('Backend Developer', 'tell me about backend developer')
        else:
            return self.get_role_recommendation(user_message)

    def get_default_response(self):
        return """🤔 I'm not sure I understand. Here's what I can help with:

• Role recommendations based on your interests
• Information about specific tech roles
• Salary and career path details
• Required skills for different positions

Try asking "What roles are available?" or "Tell me about frontend developers"!"""

# Global chatbot instance
chatbot = CareerChatbot()
