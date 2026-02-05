import pytest

# This test should fail until all skills are implemented with correct interfaces.
def test_skills_interface():
    # Example: skill_generate_caption should accept trend, media_type, platform
    # Simulate a call to the (not yet implemented) skill
    try:
        from skills.skill_generate_caption import generate_caption
        result = generate_caption(trend="AI Art", media_type="video", platform="Instagram")
        assert isinstance(result, dict) and "caption" in result
    except ImportError:
        pytest.fail("Skill 'generate_caption' not implemented or importable.")
    except Exception:
        pytest.fail("Skill 'generate_caption' interface does not match the spec.")
