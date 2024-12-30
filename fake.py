import random
import subprocess
from datetime import datetime, timedelta

# Path to the repository
REPO_PATH = "/Users/mbardan/code/AI/insanely-fast-whisper"  # Update this with the actual repo path

# Commit messages aligned with repo logic
COMMIT_MESSAGES = [
    "Optimized processing speed",
    "Refactored model inference pipeline",
    "Fixed memory leak in streaming mode",
    "Updated documentation for new features",
    "Improved batch processing performance",
    "Added support for additional languages",
    "Refined error handling in transcription module",
    "Cleaned up unused imports and code",
    "Enhanced logging for better debugging",
    "Bug fixes for edge cases in ASR engine",
]

def generate_fake_commits(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        # Generate 3-5 commits per week
        for _ in range(random.randint(3, 5)):
            commit_date = current_date + timedelta(days=random.randint(0, 6))
            if commit_date > end_date:
                break

            # Random commit message
            commit_message = random.choice(COMMIT_MESSAGES)

            # Format the commit date
            commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

            # Create a dummy file to commit
            filename = f"dummy_{commit_date.strftime('%Y%m%d%H%M%S')}.txt"
            filepath = f"{REPO_PATH}/{filename}"
            with open(filepath, "w") as f:
                f.write("Dummy file for fake commit\n")

            # Stage and commit the file with a fake date
            subprocess.run(["git", "-C", REPO_PATH, "add", filename])
            subprocess.run([
                "git", "-C", REPO_PATH, "commit", "-m", commit_message,
                "--date", commit_date_str
            ])

        # Move to the next week
        current_date += timedelta(days=7)

# Generate commits for the specified period
start_date = datetime(2024, 6, 1)
end_date = datetime(2024, 12, 31)
generate_fake_commits(start_date, end_date)