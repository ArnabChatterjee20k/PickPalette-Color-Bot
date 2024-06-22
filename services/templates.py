template_single_best_palette = """
            I will provide you with a JSON set of color palettes used in various applications.
            Data: {info}

            Your task:
            1. Suggest a single color palette that best matches this description: {description}
            2. Choose colors ONLY from the given data. Do not suggest any colors not present in the input.
            3. The maximum size of the suggested palette is 7 colors.
            4. If no suitable palette is found, return an empty list.

            Rules:
            - Do not invent, modify, or suggest any colors not explicitly listed in the input data.
            - If the description doesn't match any palette well, choose the closest approximation from the available colors.
            - Ensure all suggested colors are exact matches to those in the input data.

            json Output format:
            {{"palette": ["color1", "color2", ...]}}

            Before responding, double-check that all colors in your suggested palette appear in the original input data.
            """

template_for_multiple_palettes = """
I will provide you with a single array of colors used in various applications.
Data: {info}

Your task:
1. Suggest 5 different color palettes that match this description: {description}
2. Choose colors ONLY from the given array. Do not suggest any colors not present in the input.
3. Each palette should have a minimum of 3 colors and a maximum of 7 colors.
4. If no suitable palettes can be formed, return an empty list for that palette.

Rules:
- Do not invent, modify, or suggest any colors not explicitly listed in the input array.
- Choose the best combinations of colors from the array that match the description.
- Ensure all suggested colors are exact matches to those in the input data.
- You may use a color multiple times within a palette if it's particularly suitable for the description.
- Try to make each of the 5 palettes distinct from one another.
- Output should be in json
JSON Output format:
{{
  "palette":[
        ["color1", "color2", ...],
        ["color1", "color2", ...],
        ["color1", "color2", ...],
        ["color1", "color2", ...],
        ["color1", "color2", ...]
    ]
}}

Before responding, double-check that:
1. All colors in your suggested palettes appear in the original input array.
2. Each palette size is 7 colors.
3. The chosen colors in each palette best represent the given description.
4. You have provided 5 distinct palettes.
"""

template_single_best_palette_color_theory = """
I will provide you with a JSON set of color palettes used in various applications.
Data: {info}

Your task:
1. Suggest a single color palette that best matches this description: {description}
2. Choose colors ONLY from the given data. Do not suggest any colors not present in the input.
3. The maximum size of the suggested palette is 7 colors.
4. If no suitable palette is found, return an empty list.

Rules:
- Utilize color theory principles, including color harmony (complementary, triad, tetrad) and color context (saturation, temperature, value).
- Do not invent, modify, or suggest any colors not explicitly listed in the input data.
- If the description doesn't match any palette well, choose the closest approximation from the available colors.
- Ensure all suggested colors are exact matches to those in the input data.
- output should be in json

json Output format:
{{"palette": ["color1", "color2", ...]}}

Before responding, double-check that all colors in your suggested palette appear in the original input data.

"""
template_for_multiple_palettes_color_theory = """
I will provide you with a single array of colors used in various applications.
Data: {info}

Your task:
1. Suggest 5 different color palettes that match this description: {description}
2. Choose colors ONLY from the given array. Do not suggest any colors not present in the input.
3. Each palette should have 7 colors.
4. If no suitable palettes can be formed, return an empty list for that palette.

Rules:
- Utilize color theory principles, including color harmony (complementary, triad, tetrad), monochromatic, and analogous schemes.
- Consider color context, including saturation, temperature, and value, to ensure cohesive and harmonious palettes.
- Do not invent, modify, or suggest any colors not explicitly listed in the input array.
- Choose the best combinations of colors from the array that match the description.
- Ensure all suggested colors are exact matches to those in the input data.
- You may use a color multiple times within a palette if it's particularly suitable for the description.
- Try to make each of the 5 palettes distinct from one another.

JSON Output format:
{{
  "palette":[
        ["color1", "color2", ...],
        ["color1", "color2", ...],
        ["color1", "color2", ...],
        ["color1", "color2", ...],
        ["color1", "color2", ...]
    ]
}}

Before responding, double-check that:
1. All colors in your suggested palettes appear in the original input array.
2. Each palette size is of 5 colors.
3. The chosen colors in each palette best represent the given description.
4. You have provided 5 distinct palettes.


"""