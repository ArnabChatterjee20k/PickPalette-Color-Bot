from typing import List, Dict
import math

def categorize_colors(colors: List[str]) -> Dict[str, str]:
    categorized_colors = {
        "primary": None,
        "secondary": None,
        "tertiary": None,
        "background": None,
        "text": None,
        "accent": None,
    }

    # Sort colors by perceived brightness
    sorted_colors = sorted(colors, key=lambda color: calculate_brightness(color))

    # Assign background color
    categorized_colors["background"] = sorted_colors[0]  # Darkest color

    # Function to find the most visually pleasing combination of colors
    def find_best_combination(categories: List[str], remaining_colors: List[str]) -> None:
        if not remaining_colors or not categories:
            return
        category = categories.pop(0)
        best_color = max(remaining_colors, key=lambda color: calculate_color_distance(color, categorized_colors))
        categorized_colors[category] = best_color
        new_remaining_colors = [color for color in remaining_colors if color != best_color]
        find_best_combination(categories, new_remaining_colors)

    # Calculate color distances and assign colors
    remaining_colors = sorted_colors[1:]
    find_best_combination(['primary', 'secondary', 'tertiary'], remaining_colors)

    # Assign text color
    text_colors = [color for color in sorted_colors if color not in categorized_colors.values()]
    if text_colors:
        categorized_colors["text"] = find_contrasting_color(categorized_colors["background"], text_colors)

    # Assign accent color
    accent_colors = [color for color in sorted_colors if color not in categorized_colors.values()]
    if accent_colors:
        categorized_colors["accent"] = accent_colors[-1]  # Assign the lightest remaining color as accent
    elif sorted_colors:
        # If no colors are left, use the lightest color from all colors as accent
        categorized_colors["accent"] = sorted_colors[-1]

    return categorized_colors

def calculate_brightness(color: str) -> float:
    r, g, b = [int(color[i:i+2], 16) for i in (1, 3, 5)]
    return (r * 299 + g * 587 + b * 114) / 1000

def calculate_color_distance(color: str, categorized_colors: Dict[str, str]) -> float:
    return max(
        (get_color_distance(color, cat_color)
         for cat_color in categorized_colors.values()
         if cat_color is not None),
        default=0
    )

def get_color_distance(color1: str, color2: str) -> float:
    r1, g1, b1 = [int(color1[i:i+2], 16) for i in (1, 3, 5)]
    r2, g2, b2 = [int(color2[i:i+2], 16) for i in (1, 3, 5)]
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def find_contrasting_color(base_color: str, sorted_colors: List[str]) -> str:
    r, g, b = [int(base_color[i:i+2], 16) for i in (1, 3, 5)]
    brightness = (r * 299 + g * 587 + b * 114) / 1000

    return max(
        (color for color in sorted_colors if color != base_color),
        key=lambda color: abs(brightness - calculate_brightness(color)),
        default=sorted_colors[0] if sorted_colors else base_color
    )

# Test the function
print(categorize_colors(['#32363d', '#636d88', '#e3e4e6', '#f46652', '#726565']))