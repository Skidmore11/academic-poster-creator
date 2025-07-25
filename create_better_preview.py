#!/usr/bin/env python3
"""
Create better preview images that will definitely display correctly
"""

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_better_preview(template_name, output_path, width=800, height=600):
    """Create a better preview image that will definitely display."""
    try:
        # Create a new image with a solid background (no transparency)
        img = Image.new('RGB', (width, height), color='#ffffff')  # White background
        draw = ImageDraw.Draw(img)
        
        # Add a gradient-like background
        for y in range(height):
            # Create a subtle gradient from top to bottom
            r = int(255 - (y / height) * 20)  # Slight darkening
            g = int(255 - (y / height) * 20)
            b = int(255 - (y / height) * 30)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        # Add a border
        draw.rectangle([0, 0, width-1, height-1], outline='#3b82f6', width=3)
        
        # Add inner border
        draw.rectangle([10, 10, width-11, height-11], outline='#e5e7eb', width=1)
        
        # Add template name with better styling
        try:
            # Try to use a system font
            font = ImageFont.truetype("arial.ttf", 36)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Wrap text if it's too long
        wrapped_text = textwrap.fill(template_name, width=15)
        
        # Calculate text position (center)
        bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (width - text_width) // 2
        y = (height - text_height) // 2 - 30
        
        # Draw text with shadow for better visibility
        draw.text((x+3, y+3), wrapped_text, fill='#6b7280', font=font)
        draw.text((x, y), wrapped_text, fill='#1f2937', font=font)
        
        # Add a subtitle
        subtitle = "Template Preview"
        try:
            subtitle_font = ImageFont.truetype("arial.ttf", 18)
        except:
            subtitle_font = ImageFont.load_default()
        
        bbox_subtitle = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = bbox_subtitle[2] - bbox_subtitle[0]
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = y + text_height + 20
        
        draw.text((subtitle_x+2, subtitle_y+2), subtitle, fill='#9ca3af', font=subtitle_font)
        draw.text((subtitle_x, subtitle_y), subtitle, fill='#6b7280', font=subtitle_font)
        
        # Add some decorative elements
        # Top left corner accent
        draw.rectangle([20, 20, 60, 60], fill='#3b82f6', outline='#2563eb', width=2)
        
        # Bottom right corner accent
        draw.rectangle([width-60, height-60, width-20, height-20], fill='#3b82f6', outline='#2563eb', width=2)
        
        # Add a subtle pattern
        for i in range(0, width, 40):
            for j in range(0, height, 40):
                if (i + j) % 80 == 0:
                    draw.rectangle([i, j, i+2, j+2], fill='#e5e7eb')
        
        # Save the image with high quality
        img.save(output_path, 'PNG', optimize=False, quality=95)
        print(f"✅ Created better preview: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating better preview for {template_name}: {e}")
        return False

def main():
    """Main function to create better previews."""
    
    # Define the templates to fix
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
    
    print("🔄 Creating better preview images...")
    
    for template in templates_to_fix:
        # Create new better preview
        success = create_better_preview(template['name'], template['path'])
        if success:
            print(f"✅ Created better preview: {template['path']}")
        else:
            print(f"❌ Failed to create better preview: {template['path']}")
    
    print("🎉 Better preview creation complete!")

if __name__ == "__main__":
    main() 