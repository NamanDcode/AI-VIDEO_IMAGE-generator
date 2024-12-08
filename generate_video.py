import runwayml
import os
from db import Session, init_db
from models import GeneratedContent

runwayml.api_key = "key_a2f589938c53bfc7da0f91275eff9c19783b17f8ae14670c57e561db3a00ed216687bd263008b6a01d8f34f8cab12ff46f26cbc6c2e0e840d41e8604d7c1b57e"  

init_db()

def generate_video(prompt, num_videos=5):
    """
    Generate videos based on the given prompt using RunwayML's video generation API.

    Args:
        prompt (str): The text prompt for generating videos.
        num_videos (int): Number of videos to generate.

    Returns:
        list: List of paths where videos are saved.
    """
    videos = []
    os.makedirs("generated_videos", exist_ok=True)  # Ensure directory exists

    for i in range(1, num_videos + 1):
        # Placeholder for video generation API call
        print(f"Generating video {i} for prompt: {prompt}")
        
        # Example response from RunwayML API (you need to replace this with actual API integration)
        video_url = f"https://example.com/videos/{prompt}_video_{i}.mp4"
        
        # Save generated video to database
        db_session = Session()
        generated_content = GeneratedContent(
            type="video",
            prompt=prompt,
            content_url=video_url
        )
        db_session.add(generated_content)
        db_session.commit()
        db_session.close()
        
        videos.append(video_url)

    return videos

# Test the function with a prompt
if __name__ == "__main__":
    prompt = "batman drinking coffee"
    generated_videos = generate_video(prompt)
    for idx, video_url in enumerate(generated_videos, 1):
        print(f"Video {idx} saved at URL: {video_url}")
