"""
Real AI Chatbot integration using OpenAI API
"""

import os
import json
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# OpenAI API configuration
OPENAI_API_KEY = getattr(settings, 'OPENAI_API_KEY', None)
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

def get_ai_response(user_message, conversation_history=None):
    """Get response from OpenAI API"""
    if not OPENAI_API_KEY:
        return get_fallback_response(user_message)
    
    try:
        # Prepare system message for career guidance
        system_message = """You are a helpful Career Assistant Bot specializing in technology careers. 
        Your role is to help users explore different tech roles, understand required skills, 
        learn about salary expectations, and get career guidance.

        Key information to provide:
        - Frontend Development: HTML, CSS, JavaScript, React/Vue.js, $60k-$120k
        - Backend Development: Python, Java, Node.js, SQL/NoSQL, APIs, $70k-$140k  
        - Full Stack Development: Frontend + Backend skills, $80k-$150k
        - Data Science: Python, ML, Statistics, Pandas, TensorFlow, $90k-$180k
        - DevOps: Docker, Kubernetes, CI/CD, Cloud, $90k-$160k
        - Database Administrator: SQL, Database Design, Performance, $70k-$130k

        Always be helpful, professional, and provide specific, actionable advice.
        Keep responses concise but informative."""

        # Prepare messages
        messages = [
            {"role": "system", "content": system_message}
        ]
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # Make API request
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-3.5-turbo",
            "messages": messages,
            "max_tokens": 300,
            "temperature": 0.7
        }
        
        response = requests.post(OPENAI_API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
        
    except Exception as e:
        print(f"AI API Error: {e}")
        return get_fallback_response(user_message)

def get_fallback_response(user_message):
    """Fallback response when AI API is not available"""
    lower_message = user_message.lower()
    
    if 'hello' in lower_message or 'hi' in lower_message:
        return "Hello! I'm your Career Assistant Bot. I can help you explore tech careers like frontend, backend, data science, and more. What would you like to know?"
    elif 'frontend' in lower_message or 'web' in lower_message:
        return "Frontend development is perfect for creative people! You'll work with HTML, CSS, JavaScript, and frameworks like React to build user interfaces. Salary range: $60k-$120k. Interested in learning about the skills?"
    elif 'backend' in lower_message or 'server' in lower_message:
        return "Backend development focuses on server-side logic! You'll work with Python, Java, Node.js, databases, and APIs. Salary range: $70k-$140k. Want to know about required skills?"
    elif 'data science' in lower_message or 'data' in lower_message:
        return "Data science combines statistics, programming, and domain knowledge to extract insights from data. You'll use Python, machine learning, and visualization tools. Salary range: $90k-$180k."
    elif 'salary' in lower_message or 'how much' in lower_message:
        return "Tech salaries vary: Frontend ($60k-$120k), Backend ($70k-$140k), Full Stack ($80k-$150k), Data Science ($90k-$180k), DevOps ($90k-$160k). Which role interests you?"
    else:
        return "I can help you explore tech careers! Ask me about specific roles (frontend, backend, data science), skills, salaries, or career paths. What would you like to know?"
