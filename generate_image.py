from openai import OpenAI
import os
from db import Session, init_db
from models import GeneratedContent

# Initialize OpenAI client
client = OpenAI(api_key="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")

# Initialize DB
init_db()

def generate_image(prompt, num_images=5):
    images = []
    for _ in range(num_images):
        response = client.images.generate(
            model="dall-e-3",  # Use the latest DALL-E model
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"  # Increased image size
        )
        
        # Extract the image URL
        image_url = response.data[0].url
        images.append(image_url)
        
        # Save generated image to database
        db_session = Session()
        generated_content = GeneratedContent(
            type="image",
            prompt=prompt,
            content_url=image_url
        )
        db_session.add(generated_content)
        db_session.commit()
        db_session.close()
    
    return images

# Test the function with a prompt
if __name__ == "__main__":
    # Create directory to save images if it doesn't exist
    os.makedirs("generated_images", exist_ok=True)
    
    prompt = "A motivational quote with a sunset background"
    generated_images = generate_image(prompt)
    
    # Print image URLs
    for idx, img_url in enumerate(generated_images, 1):
        print(f"Image {idx} URL: {img_url}")
