# Skill: Fetch Trends

## Purpose
Retrieves trending topics from multiple supported social media platforms and regions. This skill enables persistent, autonomous agents to gather up-to-date, relevant topics for content generation, strategic planning, and cross-platform trend analysis within hierarchical swarms and policy-bounded autonomy.

## Usage Example
```json
{
	"platform": "TikTok",
	"region": "Global"
}
```
Returns:
```json
{
	"trends": [
		"Dance Challenges",
		"AI Filters",
		"Viral Memes"
	]
}
```

## Input Format
- `platform` (string): The social media platform to query (e.g., Twitter, TikTok, Instagram, YouTube, Reddit, etc.).
- `region` (string): The geographic region or market (e.g., US, EU, Global).

## Output Format
- `trends` (array of strings): List of trending topics for the specified platform and region.

## Best Practices
- Use current and supported platform/region values for best results.
- Extend the platform list as new social media sources are integrated.
- Combine with content generation skills to create timely, relevant posts.
- Validate trends for appropriateness and compliance with platform guidelines.
- Coordinate with Orchestrator and hierarchical swarm for managed, scalable execution.
- Follow BoardKit governance and exception management policies.
