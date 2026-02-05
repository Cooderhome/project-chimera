# Skill: Publish Video

## Purpose
Publishes generated or curated short-form videos to supported social media platforms. This skill enables persistent, autonomous agents to automate the final step of content delivery, ensuring timely and consistent posting within policy-bounded autonomy and hierarchical swarms.

## Usage Example
```json
{
	"video_path": "./output/my_video.mp4",
	"caption": "Check out the latest AI trends! #AI #Trends",
	"platform": "Instagram"
}
```
Returns:
```json
{
	"status": "success",
	"post_url": "https://instagram.com/p/abc123"
}
```

## Input Format
- `video_path` (string): Path to the video file to be published.
- `caption` (string): Caption or description to accompany the video.
- `platform` (string): Target social media platform (e.g., Instagram, TikTok, YouTube Shorts).

## Output Format
- `status` (string): Result of the publishing action (e.g., success, error).
- `post_url` (string, optional): URL to the published post if successful.

## Best Practices
- Ensure video files meet platform-specific requirements (format, length, aspect ratio).
- Review captions for compliance and engagement.
- Use with BoardKit governance and exception management policies.
- Coordinate with Orchestrator and hierarchical swarm for managed, scalable execution.
