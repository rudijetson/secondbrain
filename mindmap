import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_mind_map(topic):
    prompt = f"""
    Generate a comprehensive mind map for "{topic}". The mind map should adhere to the following guidelines:

    1. Start with the topic as the central idea, using a single # at the beginning.

    2. Break down the topic into main categories or pillars, using ## for each category.

    3. Further break down each main category into subcategories or detailed information, using ### for each subcategory.

    4. Provide relevant details, examples, or explanations for each subcategory, using - for each point.

    5. Aim for a comprehensive yet concise mind map that captures the essential information about the topic.

    6. The mind map should be suitable for an exploratory learning approach, allowing users to navigate and discover different aspects of the topic.

    Please use the specified Markdown formatting to create the mind map.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",  # Use the correct and most up-to-date model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Markdown-formatted mind maps."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the Markdown-formatted content
    mind_map_markdown = response.choices[0].message.content
    return mind_map_markdown

# Example usage
topic = "GTM-Strategy"
file_title = topic.replace(" ", "_")

# Generate the mind map
mind_map = generate_mind_map(topic)

# Save the generated mind map to a Markdown file
with open(f"{file_title}_Mind_Map.md", "w") as file:
    file.write(mind_map)

print(f"Mind map for '{topic}' saved to {file_title}_Mind_Map.md")
