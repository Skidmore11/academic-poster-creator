#!/usr/bin/env python3
"""
Template Configuration System
Defines font sizes and colors for specific templates.
"""

from pptx.enum.text import PP_ALIGN

# Premium template categorization
PREMIUM_TEMPLATES = [
    "Playground Template"  # Currently the only premium template
]

# New template categorization
NEW_TEMPLATES = [
    "Personal Blue Basic"
]

# Note: All templates that are NOT in COMING_SOON_TEMPLATES are automatically considered NEW

# Coming Soon template categorization
COMING_SOON_TEMPLATES = [
    "Grey Classic",  # Template that's uploaded but not yet ready
    "Space 3D Template",
    "Modern Blue Template", 
    "Grounded Template",
    "Pastel Template",
    "Playful Template"
]

# Template descriptions for user guidance
TEMPLATE_DESCRIPTIONS = {
    "Blue Template": {
        "title": "Professional Blue Template",
        "description": "A clean, professional template with a modern blue color scheme. Features balanced typography and clear section separation for presentations.",
        "choose_if": [
            "You want a professional, corporate look",
            "Your research has a formal, professional tone",
            "You prefer clean, minimalist design",
            "You need a template that works well with data-heavy content"
        ],
        "ideal_for": "Professional conferences, corporate presentations, and formal research showcases."
    },
    "Green Template": {
        "title": "Modern Green Template",
        "description": "A contemporary template with a fresh green color palette and left-aligned typography. Offers a modern, approachable feel while maintaining professional rigor.",
        "choose_if": [
            "You want a modern, fresh appearance",
            "Your research has an environmental or health focus",
            "You prefer left-aligned, easy-to-read layouts",
            "You want to stand out from traditional blue templates"
        ],
        "ideal_for": "Environmental studies, health sciences, and modern professional presentations."
    },

    "Headline Impact Template": {
        "title": "Headline Impact Template",
        "description": "A bold, modern poster template designed to foreground your key message right from the start. This layout is perfect when your research has a standout finding or clear take-home point you want your audience to remember.",
        "choose_if": [
            "You want to highlight a headline result or bold claim — the large title space ensures it catches attention immediately.",
            "Your work includes key visuals or data figures — two prominent, right-aligned figure boxes (labelled Figure 1 and Figure 2) allow you to showcase central findings without overwhelming the text.",
            "You’re presenting to a broad or mixed audience — the icon-accompanied sections (Introduction, Methods, Results, Discussion) help guide readers with varying levels of expertise.",
            "You need a visually engaging but compact format — perfect for conferences where quick impact matters."
        ],
        "ideal_for": "The layout supports a left-to-right flow, balancing visual storytelling with structured sections and a clean references/footer zone. A built-in QR code space allows for easy linking to full papers or project pages."
    },
    "Personal Blue Basic": {
        "title": "Personal Blue Basic Template",
        "description": "A clean, straightforward template with a professional blue color scheme. Perfect for researchers who want a simple, reliable layout that focuses on content without distracting design elements.",
        "choose_if": [
            "You want a simple, clean design that won't distract from your content",
            "You prefer traditional professional poster layouts",
            "You need a template that works well with any type of research",
            "You want something professional but not overly flashy"
        ],
        "ideal_for": "General professional presentations, thesis defenses, and research that benefits from a clean, traditional layout."
    },
    "Clean 5-Panel Flow Template": {
        "title": "Clean 5-Panel Flow Template",
        "description": "A structured 5-panel layout designed for clear information flow and logical progression. Perfect for research with distinct phases or sequential processes.",
        "choose_if": [
            "Your research has distinct phases or sequential steps",
            "You want a structured, easy-to-follow layout",
            "You have multiple key findings to present",
            "You prefer organized, systematic presentation"
        ],
        "ideal_for": "Process-based research, multi-phase studies, and research with clear sequential components."
    },
    "Cyan Flow Template": {
        "title": "Cyan Flow Template",
        "description": "A clean, modern layout featuring a central visual focal point alongside sections for flow, methods, and discussion. This design balances strong visual storytelling with clear research structure.",
        "choose_if": [
            "Your study includes a standout figure or visual element you want to highlight",
            "You want to guide the viewer through a logical flow of your research process",
            "You're presenting a methodology-driven or process-oriented project",
            "You prefer a layout that feels visual but still professional"
        ],
        "ideal_for": "Qualitative studies, intervention development, visual frameworks, and research that benefits from a strong narrative arc."
    },
    "Modular Impact": {
        "title": "Modular Impact Template",
        "description": "A vibrant and well-structured double-column layout with numbered sections, clear typography, and strong use of colour to guide the reader. Visuals are neatly arranged alongside text, with a dedicated space for figures, future work, and references.",
        "choose_if": [
            "You want a straightforward, linear narrative from background to conclusion",
            "Your poster includes multiple figures and you want them cleanly positioned",
            "You need clear visual sectioning with standout numbering",
            "You value a polished, conference-ready design with good hierarchy"
        ],
        "ideal_for": "Scientific posters with quantitative data, undergraduate or postgraduate project presentations, and any research requiring a clear, numbered progression."
    },
    "Emerald Headline Template": {
        "title": "Emerald Headline Template",
        "description": "A bold, modern layout with a high-impact headline space to draw immediate attention. This template balances graphic design with academic structure—featuring clear section headers, strong colour blocks, and a standout flowchart-style methods section.",
        "choose_if": [
            "You want to lead with a strong, engaging headline finding",
            "You need to visualise a multi-stage process (e.g. intervention phases, timelines)",
            "You’re aiming for a more contemporary, design-forward look",
            "You want to keep content brief and visual"
        ],
        "ideal_for": "Digital health, implementation research, or applied studies with a clear call to action. Perfect for drawing attention in competitive poster halls or when trying to communicate one clear message."
    }
}

# Template-specific configurations
TEMPLATE_CONFIGS = {
    "Blue Template": {
        "title": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Futura",
            "bold": True,
            "alignment": "center"
        },
        "subtitle": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "center"
        },
        "authors": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 48,    # ≤80 characters
                "medium": 38,   # 81-120 characters
                "long": 34,     # >120 characters
                "alignment": "middle"  # Middle alignment added
            },
            "subtitle": {
                "ratio": 0.6,   # 60% of title size
                "min_size": 32,  # Minimum size
                "alignment": "middle"  # Middle alignment added
            },
            "authors": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            },
            "affiliations": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            },
            "main_body": {
                "short": 18    # Fixed size for main body text
            },
            "references": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            }
        }
    },
    "Headline Impact Template": {
        "title": {
            "font_color": "#ffffff",  # White for strong contrast
            "font_family": "Intro Rust",
            "bold": True,
            "alignment": "left"
        },
        "subtitle": {
            "font_color": "#ffffff",  # White
            "font_family": "Intro Rust",
            "bold": False,
            "alignment": "center"
        },
        "authors": {
            "font_color": "#ffffff",
            "font_family": "Intro Rust",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#222222",
            "font_family": "Intro Rust",
            "bold": False,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#222222",
            "font_family": "Aptos",
            "bold": False,
            "alignment": "left",
            "font_size": 32
        },
        "references": {
            "font_color": "#ffffff",
            "font_family": "Aptos",
            "bold": False,
            "alignment": "left",
            "font_size": 24
        },
        "FigureDesc": {
            "font_color": "#222222",
            "font_family": "Aptos",
            "bold": False,
            "alignment": "left",
            "font_size": 32
        },
        "headline": {
            "font_color": "#ffffff",
            "font_family": "Intro Rust",
            "bold": True,
            "alignment": "left",
            "font_size": 125
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 88,    # ≤80 characters
                "medium": 66,   # 81-120 characters
                "long": 60,     # >120 characters
                "alignment": "left"
            },
            "subtitle": {
                "ratio": 0.6,   # 60% of title size
                "min_size": 28,  # Minimum size
                "alignment": "left"
            },
            "authors": {
                "short": 38,    # ≤80 characters
                "medium": 32,   # 81-160 characters
                "long": 24,     # >160 characters
                "extra_long": 22 # >250 characters
            },
            "affiliations": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            },
            "main_body": {
                "short": 28    # Fixed size for main body text
            }
        }
    },
    "Green Template": {
        "title": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Darker Grotesque",
            "bold": True,
            "alignment": "left"
        },
        "subtitle": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Darker Grotesque",
            "bold": False,
            "alignment": "left"
        },
        "authors": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Darker Grotesque",
            "bold": True,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Darker Grotesque",
            "bold": False,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Dark green text
            "font_family": "Darker Grotesque",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",  # Dark green text
            "font_family": "Darker Grotesque",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Dark green text
            "font_family": "Darker Grotesque",
            "bold": False,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 80,    # ≤80 characters
                "medium": 80,   # 81-120 characters
                "long": 60      # >120 characters
            },
            "subtitle": {
                "ratio": 0.8,  # 65% of title size
                "min_size": 40  # Minimum size
            },
            "authors": {
                "short": 44,    # ≤80 characters
                "medium": 40,   # 81-160 characters
                "long": 36      # >160 characters
            },
            "affiliations": {
                "short": 20,    # ≤80 characters
                "medium": 18,   # 81-160 characters
                "long": 16      # >160 characters
            },
            "main_body": {
                "short": 40    # Fixed size for main body text
            },
            "references": {
                "short": 30,    # ≤80 characters
                "medium": 26,   # 81-160 characters
                "long": 26      # >160 characters
            }
        }
    },
    "Personal Blue Basic": {
        "title": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Futura",
            "bold": True,
            "alignment": "left"
        },
        "subtitle": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": True,
            "alignment": "left"
        },
        "authors": {
            "font_color": "#FFFFFF",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#FFFFFF",
            "font_family": "Futura",
            "bold": False,
            "italic": True,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 60,    # ≤80 characters
                "medium": 60,   # 81-120 characters
                "long": 48,     # >120 characters
                "alignment": "middle"
            },
            "subtitle": {
                "ratio": 0.6,   # 60% of title size
                "min_size": 32,  # Minimum size
                "alignment": "middle"
            },
            "authors": {
                "short": 40,    # ≤80 characters
                "medium": 36,   # 81-160 characters
                "long": 32,     # >160 characters
                "extra_long": 28 # >250 characters
            },
            "affiliations": {
                "short": 24,    # ≤80 characters
                "medium": 24,   # 81-160 characters
                "long": 24,     # >160 characters
                "extra_long": 24 # >250 characters
            },
            "main_body": {
                "short": 36    # Fixed size for main body text
            },
            "references": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            }
        }
    },
    "Clean 5-Panel Flow Template": {
        "title": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Futura",
            "bold": True,
            "alignment": "center"
        },
        "subtitle": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "center"
        },
        "authors": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 48,    # ≤80 characters
                "medium": 38,   # 81-120 characters
                "long": 34,     # >120 characters
                "alignment": "center"
            },
            "subtitle": {
                "ratio": 0.6,   # 60% of title size
                "min_size": 32,  # Minimum size
                "alignment": "center"
            },
            "authors": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            },
            "affiliations": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            },
            "main_body": {
                "short": 18    # Fixed size for main body text
            },
            "references": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 13,     # >160 characters
                "extra_long": 11 # >250 characters
            }
        }
    },
    "Cyan Flow Template": {
        "title": {
            "font_color": "#05bbd6",  # Cyan text
            "font_family": "Aptos",
            "bold": True,
            "alignment": "center"
        },
        "subtitle": {
            "font_color": "#000000",  # Cyan text
            "font_family": "Aptos",
            "bold": False,
            "alignment": "center"
        },
        "authors": {
            "font_color": "#000000",
            "font_family": "Aptos",
            "bold": False,
            "alignment": "center"
        },
        "affiliations": {
            "font_color": "#000000",
            "font_family": "Aptos",
            "bold": False,
            "alignment": "center"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",  # Black text
            "font_family": "Aptos",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Black text
            "font_family": "Aptos",
            "bold": False,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 80,    # ≤80 characters
                "medium": 72,   # 81-120 characters
                "long": 60,     # >120 characters
                "alignment": "center"
            },
            "subtitle": {
                "ratio": 0.7,   # 70% of title size
                "min_size": 28,  # Minimum size
                "alignment": "center"
            },
            "authors": {
                "short": 40,    # ≤80 characters
                "medium": 36,   # 81-160 characters
                "long": 32,     # >160 characters
                "extra_long": 28, # >250 characters
                "alignment": "center"
            },
            "affiliations": {
                "short": 24,    # ≤80 characters
                "medium": 24,   # 81-160 characters
                "long": 20,     # >160 characters
                "extra_long": 16 # >250 characters
            },
            "main_body": {
                "short": 36    # Fixed size for main body text
            },
            "references": {
                "short": 32,    # ≤80 characters
                "medium": 28,   # 81-160 characters
                "long": 128,     # >160 characters
                "extra_long": 28 # >250 characters
            }
        }
    },
    "Modular Impact": {
        "title": {
            "font_color": "#FFFFFF",  # White text for dark backgrounds
            "font_family": "Futura",
            "bold": True,
            "alignment": "center"
        },
        "subtitle": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "center"
        },
        "authors": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Black text
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 56,    # ≤80 characters
                "medium": 46,   # 81-120 characters
                "long": 40,     # >120 characters
                "alignment": "center"
            },
            "subtitle": {
                "ratio": 0.65,  # 65% of title size
                "min_size": 30,  # Minimum size
                "alignment": "center"
            },
            "authors": {
                "short": 22,    # ≤80 characters
                "medium": 20,   # 81-160 characters
                "long": 18,     # >160 characters
                "extra_long": 16 # >250 characters
            },
            "affiliations": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 14,     # >160 characters
                "extra_long": 12 # >250 characters
            },
            "main_body": {
                "short": 22    # Fixed size for main body text
            },
            "references": {
                "short": 18,    # ≤80 characters
                "medium": 16,   # 81-160 characters
                "long": 14,     # >160 characters
                "extra_long": 12 # >250 characters
            }
        }
    },
    "Emerald Headline Template": {
        "title": {
            "font_color": "#000000",  # White text for dark backgrounds
            "font_family": "Poppins",
            "bold": True,
            "alignment": "left"
        },
        "subtitle": {
            "font_color": "#000000",  # Black text
            "font_family": "Poppins",
            "bold": False,
            "alignment": "left"
        },
        "authors": {
            "font_color": "#000000",
            "font_family": "Poppins",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#000000",
            "font_family": "Poppins",
            "bold": False,
            "italic": True,
            "alignment": "left"
        },
        "main_body_text": {  # Introduction, Methods, Results, etc.
            "font_color": "#000000",  # Black text
            "font_family": "Poppins",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#ffffff",  # Black text
            "font_family": "Poppins",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",  # Black text
            "font_family": "Poppins",
            "bold": False,
            "alignment": "left"
        },
        "headline": {
            "font_color": "#ffffff",  # White text for dark backgrounds
            "font_family": "Poppins",
            "bold": True,
            "alignment": "left"
        },
        "dynamic_font_sizes": {
            "title": {
                "short": 100,    # ≤80 characters
                "medium": 80,   # 81-120 characters
                "long": 60,     # >120 characters
                "alignment": "center"
            },
            "subtitle": {
                "ratio": 0.68,  # 68% of title size
                "min_size": 32,  # Minimum size
                "alignment": "center"
            },
            "authors": {
                "short": 44,    # ≤80 characters
                "medium": 44,   # 81-160 characters
                "long": 32,     # >160 characters
                "extra_long": 28 # >250 characters
            },
            "affiliations": {
                "short": 30,    # ≤80 characters
                "medium": 24,   # 81-160 characters
                "long": 20,     # >160 characters
                "extra_long": 16 # >250 characters
            },
            "main_body": {
                "short": 24    # Fixed size for main body text
            },
            "references": {
                "short": 20,    # ≤80 characters
                "medium": 20,   # 81-160 characters
                "long": 20,     # >160 characters
                "extra_long": 20 # >250 characters
            }
        }
    }
}

def is_premium_template(template_name):
    """
    Check if a template is premium.
    Returns True if the template is in the premium list.
    """
    return template_name in PREMIUM_TEMPLATES

def get_premium_templates():
    """
    Get list of all premium template names.
    """
    return PREMIUM_TEMPLATES.copy()

def add_premium_template(template_name):
    """
    Add a template to the premium list.
    Returns True if added, False if already exists.
    """
    if template_name not in PREMIUM_TEMPLATES:
        PREMIUM_TEMPLATES.append(template_name)
        return True
    return False

def remove_premium_template(template_name):
    """
    Remove a template from the premium list.
    Returns True if removed, False if not found.
    """
    if template_name in PREMIUM_TEMPLATES:
        PREMIUM_TEMPLATES.remove(template_name)
        return True
    return False

def is_new_template(template_name):
    """
    Check if a template is in the NEW_TEMPLATES list.
    """
    return template_name in NEW_TEMPLATES

def get_new_templates():
    """
    Get list of all new template names.
    Since all non-coming-soon templates are NEW, this function
    would need the full template list to filter properly.
    """
    # This is a placeholder - in practice, you'd pass the full template list
    # and filter out coming soon templates
    return []

def add_new_template(template_name):
    """
    Add a template to the new list.
    Since NEW is now automatic (not coming soon), this function
    would remove the template from coming soon list instead.
    """
    return remove_coming_soon_template(template_name)

def remove_new_template(template_name):
    """
    Remove a template from the new list.
    Since NEW is now automatic, this function
    would add the template to coming soon list instead.
    """
    return add_coming_soon_template(template_name)

def is_coming_soon_template(template_name):
    """
    Check if a template is in the coming soon list.
    Returns True if the template is in the coming soon list.
    """
    return template_name in COMING_SOON_TEMPLATES

def get_coming_soon_templates():
    """
    Get list of all coming soon template names.
    """
    return COMING_SOON_TEMPLATES.copy()

def add_coming_soon_template(template_name):
    """
    Add a template to the coming soon list.
    Returns True if added, False if already exists.
    """
    if template_name not in COMING_SOON_TEMPLATES:
        COMING_SOON_TEMPLATES.append(template_name)
        return True
    return False

def remove_coming_soon_template(template_name):
    """
    Remove a template from the coming soon list.
    Returns True if removed, False if not found.
    """
    if template_name in COMING_SOON_TEMPLATES:
        COMING_SOON_TEMPLATES.remove(template_name)
        return True
    return False

def get_template_config(template_name):
    """
    Get configuration for a specific template.
    Returns None if no specific config exists.
    """
    return TEMPLATE_CONFIGS.get(template_name, None)

def get_font_settings(template_name, section_type):
    """
    Get font settings for a specific template and section.
    Returns default settings if no template-specific config exists.
    """
    config = get_template_config(template_name)
    
    if not config:
        # Return default settings
        return get_default_font_settings(section_type)
    
    # Get section-specific settings
    if section_type == "headline":
        return config.get("headline", get_default_font_settings("headline"))
    if section_type == "title":
        return config.get("title", get_default_font_settings("title"))
    elif section_type == "subtitle":
        return config.get("subtitle", get_default_font_settings("subtitle"))
    elif section_type == "authors":
        return config.get("authors", get_default_font_settings("authors"))
    elif section_type == "affiliations":
        return config.get("affiliations", get_default_font_settings("affiliations"))
    elif section_type == "references":
        return config.get("references", get_default_font_settings("references"))
    elif section_type == "FigureDesc":
        return config.get("FigureDesc", get_default_font_settings("FigureDesc"))
    else:
        # Body sections (Introduction, Methods, Results, etc.)
        return config.get("main_body_text", get_default_font_settings("main_body_text"))

def get_dynamic_font_size_config(template_name, section_type):
    """
    Get dynamic font size configuration for a specific template and section.
    Returns None if no template-specific config exists.
    """
    config = get_template_config(template_name)
    if not config or "dynamic_font_sizes" not in config:
        return None
    
    dynamic_config = config["dynamic_font_sizes"]
    
    # Map section types to dynamic config keys
    section_mapping = {
        "title": "title",
        "subtitle": "subtitle",
        "authors": "authors",
        "affiliations": "affiliations",
        "main_body_text": "main_body",
        "references": "references"
    }
    
    config_key = section_mapping.get(section_type)
    if config_key and config_key in dynamic_config:
        return dynamic_config[config_key]
    
    return None

def get_default_dynamic_font_sizes():
    """
    Get default dynamic font size configuration.
    """
    return {
        "title": {
            "short": 48,    # ≤80 characters
            "medium": 38,   # 81-120 characters
            "long": 34      # >120 characters
        },
        "subtitle": {
            "ratio": 0.6,   # 60% of title size
            "min_size": 32  # Minimum size
        },
        "authors": {
            "short": 18,    # ≤80 characters
            "medium": 16,   # 81-160 characters
            "long": 13,     # >160 characters
            "extra_long": 11 # >250 characters
        },
        "affiliations": {
            "short": 18,    # ≤80 characters
            "medium": 16,   # 81-160 characters
            "long": 13,     # >160 characters
            "extra_long": 11 # >250 characters
        },
        "main_body": {
            "short": 18    # Fixed size for main body text
        },
        "references": {
            "short": 18,    # ≤80 characters
            "medium": 16,   # 81-160 characters
            "long": 13,     # >160 characters
            "extra_long": 11 # >250 characters
        }
    }

def get_default_font_settings(section_type):
    """
    Get default font settings for each section type.
    """
    defaults = {
        "headline": {
            "font_color": "#ffffff",
            "font_family": "Intro Rust",
            "bold": True,
            "alignment": "center",
            "font_size": 125
        },
        "title": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": True,
            "alignment": "center"
        },
        "subtitle": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "center"
        },
        "authors": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "affiliations": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "main_body_text": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "references": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        },
        "FigureDesc": {
            "font_color": "#000000",
            "font_family": "Futura",
            "bold": False,
            "alignment": "left"
        }
    }
    
    return defaults.get(section_type, defaults["main_body_text"])

def hex_to_rgb(hex_color):
    """
    Convert hex color to RGB tuple.
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_alignment_constant(alignment_string):
    """
    Convert alignment string to PowerPoint alignment constant.
    """
    alignment_map = {
        "left": PP_ALIGN.LEFT,
        "center": PP_ALIGN.CENTER,
        "right": PP_ALIGN.RIGHT,
        "justify": PP_ALIGN.JUSTIFY
    }
    return alignment_map.get(alignment_string.lower(), PP_ALIGN.LEFT)

def is_blue_template(template_path):
    """
    Check if the template is the Blue Template.
    """
    import os
    template_name = os.path.basename(template_path)
    return template_name == "Blue Template.pptx" or "Blue Template" in template_name

def get_template_description(template_name):
    """
    Get description for a specific template.
    Returns None if no description exists.
    """
    return TEMPLATE_DESCRIPTIONS.get(template_name, None)

def get_all_template_descriptions():
    """
    Get all template descriptions.
    """
    return TEMPLATE_DESCRIPTIONS.copy() 