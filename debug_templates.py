#!/usr/bin/env python3
"""
Debug script to test template loading functionality
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_template_loading():
    """Test template loading step by step"""
    print("🔍 Testing template loading...")
    
    # Test 1: Check if template_configs can be imported
    try:
        import template_configs
        print("✅ template_configs imported successfully")
    except Exception as e:
        print(f"❌ Error importing template_configs: {e}")
        return
    
    # Test 2: Check if template library folder exists
    template_folder = 'template_library'
    if os.path.exists(template_folder):
        print(f"✅ Template folder exists: {template_folder}")
    else:
        print(f"❌ Template folder not found: {template_folder}")
        return
    
    # Test 3: List all .pptx files
    pptx_files = [f for f in os.listdir(template_folder) if f.endswith('.pptx')]
    print(f"✅ Found {len(pptx_files)} .pptx files")
    for f in pptx_files[:3]:  # Show first 3
        print(f"   - {f}")
    
    # Test 4: Test template_configs functions
    try:
        from template_configs import is_premium_template, is_coming_soon_template, is_new_template
        print("✅ template_configs functions imported successfully")
        
        # Test with a sample template name
        sample_name = "Bi-Simple Template"
        print(f"   Testing with '{sample_name}':")
        print(f"     - is_premium: {is_premium_template(sample_name)}")
        print(f"     - is_coming_soon: {is_coming_soon_template(sample_name)}")
        print(f"     - is_new: {is_new_template(sample_name)}")
        
    except Exception as e:
        print(f"❌ Error testing template_configs functions: {e}")
        return
    
    # Test 5: Test the full load_template_library function
    try:
        import app
        templates = app.load_template_library()
        print(f"✅ load_template_library() returned {len(templates)} templates")
        
        if templates:
            print("   First template:")
            for key, value in templates[0].items():
                print(f"     {key}: {value}")
        else:
            print("   No templates returned!")
            
    except Exception as e:
        print(f"❌ Error in load_template_library(): {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_template_loading() 