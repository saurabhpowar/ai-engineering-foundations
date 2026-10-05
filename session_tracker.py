# Constants: written in ALL_CAPS by convention (PEP 8) because they shouldn't change
TARGET_MINUTES = 120
ELAPSED_MINUTES = 85


def calculate_progress(elapsed_minutes: int, target_minutes: int) -> dict:
    """
    Calculates study progress and returns a summary as a dictionary.
    """
    remaining_minutes = target_minutes - elapsed_minutes
    percentage_completed = round((elapsed_minutes / target_minutes) * 100, 1)

    if elapsed_minutes >= target_minutes:
        status = "completed"
    elif percentage_completed >= 50:
        status = "in_progress"
    else:
        status = "behind"

    return {
        "status": status,
        "remaining_minutes": remaining_minutes,
        "percentage_completed": percentage_completed,
    }


if __name__ == "__main__":
    result = calculate_progress(ELAPSED_MINUTES, TARGET_MINUTES)

    print("----- Study Session Summary -----")
    print(f"Elapsed minutes: {ELAPSED_MINUTES}")
    print(f"Target minutes: {TARGET_MINUTES}")
    print(f"Status: {result['status']}")
    print(f"Remaining minutes: {result['remaining_minutes']}")
    print(f"Percentage completed: {result['percentage_completed']}%")
    print("----------------------------------")

    """import this"""
