#!/usr/bin/env python
"""
Setup script for AI Chatbot configuration
"""

import os
import sys

def setup_openai_api():
    """Setup OpenAI API key for the chatbot"""
    print("🤖 AI Chatbot Setup")
    print("=" * 40)
    print()
    print("This script will help you configure the OpenAI API key for the AI chatbot.")
    print("You can get your API key from: https://platform.openai.com/api-keys")
    print()
    
    # Check if API key is already set
    current_key = os.environ.get('OPENAI_API_KEY')
    if current_key and current_key != 'your-openai-api-key-here':
        print(f"✅ OpenAI API key is already configured")
        return True
    
    print("Please enter your OpenAI API key:")
    print("(Press Enter to skip and use fallback responses)")
    api_key = input("OpenAI API Key: ").strip()
    
    if not api_key:
        print("⚠️  No API key provided. The chatbot will use fallback responses.")
        return False
    
    # Validate API key format (basic check)
    if not api_key.startswith('sk-'):
        print("⚠️  Warning: API key should start with 'sk-'")
        confirm = input("Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            print("Setup cancelled.")
            return False
    
    # Set environment variable for current session
    os.environ['OPENAI_API_KEY'] = api_key
    print("✅ OpenAI API key configured for current session")
    print()
    print("To make this permanent, add this to your environment variables:")
    print(f"export OPENAI_API_KEY='{api_key}'")
    print("Or add it to your .env file:")
    print(f"OPENAI_API_KEY={api_key}")
    
    return True

def test_ai_connection():
    """Test the AI connection"""
    print("\n🧪 Testing AI Connection...")
    
    try:
        from roadmaps.ai_chatbot import get_ai_response
        response = get_ai_response("Hello, can you help me with tech careers?")
        
        if response and len(response) > 10:
            print("✅ AI connection successful!")
            print(f"Sample response: {response[:100]}...")
            return True
        else:
            print("⚠️  AI connection test failed - using fallback responses")
            return False
            
    except Exception as e:
        print(f"❌ AI connection error: {e}")
        print("🔄 Falling back to local chatbot responses")
        return False

if __name__ == "__main__":
    try:
        # Add project root to Python path
        project_root = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, project_root)
        
        # Setup API key
        api_configured = setup_openai_api()
        
        # Test connection
        if api_configured:
            test_ai_connection()
        
        print("\n🎉 Setup complete!")
        print("The chatbot is ready to use.")
        if not api_configured:
            print("Note: Using fallback responses. Configure OpenAI API key for AI responses.")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're running this from the project directory.")
    except Exception as e:
        print(f"❌ Setup error: {e}")
