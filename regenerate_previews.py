#!/usr/bin/env python3
"""
Script to regenerate problematic preview images
"""

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_placeholder_preview(template_name, output_path, width=800, height=600):
    """Create a placeholder preview image for a template."""
    try:
        # Create a new image with a light background
        img = Image.new('RGB', (width, height), color='#f8f9fa')
        draw = ImageDraw.Draw(img)
        
        # Add a border
        draw.rectangle([0, 0, width-1, height-1], outline='#dee2e6', width=2)
        
        # Add template name
        try:
            # Try to use a system font
            font = ImageFont.truetype("arial.ttf", 32)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Wrap text if it's too long
        wrapped_text = textwrap.fill(template_name, width=20)
        
        # Calculate text position (center)
        bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        # Draw text with shadow
        draw.text((x+2, y+2), wrapped_text, fill='#6c757d', font=font)
        draw.text((x, y), wrapped_text, fill='#495057', font=font)
        
        # Add a subtitle
        subtitle = "Template Preview"
        try:
            subtitle_font = ImageFont.truetype("arial.ttf", 16)
        except:
            subtitle_font = ImageFont.load_default()
        
        bbox_subtitle = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = bbox_subtitle[2] - bbox_subtitle[0]
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = y + text_height + 20
        
        draw.text((subtitle_x, subtitle_y), subtitle, fill='#6c757d', font=subtitle_font)
        
        # Save the image
        img.save(output_path, 'PNG', optimize=True)
        print(f"✅ Created placeholder preview: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating placeholder for {template_name}: {e}")
        return False

def main():
    """Main function to regenerate problematic previews."""
    
    # Define the problematic templates
    templates_to_fix = [
        {
            'name': 'Personal Blue Basic',
            'path': 'template_library/available/Personal Blue Basic_preview.png'
        },
        {
            'name': 'Playground Template', 
            'path': 'template_library/coming_soon/Playground Template_preview.png'
        }
    ]
    
    print("🔄 Regenerating problematic preview images...")
    
    for template in templates_to_fix:
        if os.path.exists(template['path']):
            # Backup the original file
            backup_path = template['path'] + '.backup'
            try:
                os.rename(template['path'], backup_path)
                print(f"📦 Backed up original: {backup_path}")
            except Exception as e:
                print(f"⚠️ Could not backup {template['path']}: {e}")
        
        # Create new placeholder
        success = create_placeholder_preview(template['name'], template['path'])
        if success:
            print(f"✅ Regenerated: {template['path']}")
        else:
            print(f"❌ Failed to regenerate: {template['path']}")
    
    print("🎉 Preview regeneration complete!")

if __name__ == "__main__":
    main() 