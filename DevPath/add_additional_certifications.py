#!/usr/bin/env python
"""
Script to add additional free certifications to all existing roles.
"""

import os
import sys
import django

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from roadmaps.models import CertificationRecommendation, Role
from roadmaps.additional_certifications import ADDITIONAL_CERTIFICATIONS

def add_certifications_to_all_roles():
    """Add additional free certifications to all roles"""
    roles = Role.objects.all()
    
    for role in roles:
        print(f"Adding certifications to {role.name}...")
        
        for cert_data in ADDITIONAL_CERTIFICATIONS:
            # Create certification recommendation for this role
            CertificationRecommendation.objects.update_or_create(
                role=role,
                platform=cert_data["platform"],
                title=cert_data["title"],
                description=cert_data["description"],
                url=cert_data["url"],
                difficulty_level=cert_data["difficulty_level"],
                duration=cert_data["duration"],
                rating=cert_data["rating"],
                is_paid=cert_data["is_paid"],
                price=cert_data["price"],
                provider=cert_data["provider"],
                prerequisites=cert_data["prerequisites"],
                order=cert_data["order"],
            )
            print(f"  - Added {cert_data['title']} from {cert_data['platform']}")

if __name__ == "__main__":
    add_certifications_to_all_roles()
    print("Additional certifications added successfully!")
