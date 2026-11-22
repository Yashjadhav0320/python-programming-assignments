# Initialize the student package and expose selected functions.
from .details import display_student
from .results import calculate_result

__all__ = ["display_student", "calculate_result"]
