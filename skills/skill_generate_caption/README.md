# Skill: Generate Caption

## Purpose
Generates contextually relevant captions and descriptions for social media content based on trending topics or provided prompts. This skill supports autonomous, persistent agents operating within policy-bounded autonomy and hierarchical swarms.

## Usage Example
```json
{
	"trend": "AI Art",
	"media_type": "video",
	"platform": "Instagram"
}
```
Returns:
```json
{
	"caption": "Discover the latest in AI-generated art! #AIArt #Innovation"
}
```

## Input Format
- `trend` (string): The trending topic or theme.
- `media_type` (string): Type of media (e.g., video, image, story).
- `platform` (string): Target social media platform.

## Output Format
- `caption` (string): Generated caption or description suitable for the platform and media type.

## Best Practices
- Ensure input trend and platform are up-to-date for relevance.
- Review generated captions for tone and compliance with platform guidelines.
- Use in combination with trend research and publishing skills for best results.
- Coordinate with Orchestrator and hierarchical swarm for scalable, managed execution.
- Follow BoardKit governance and exception management policies.
