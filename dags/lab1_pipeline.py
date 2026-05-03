"""A simple Airflow DAG for lab 1.

The pipeline generates a small list of numbers, validates it, calculates
basic statistics, and prints a short report to the task logs.
"""

from __future__ import annotations

from statistics import mean

import pendulum
from airflow.decorators import dag, task


@dag(
    dag_id="lab1_pipeline",
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["lab1", "docker-compose"],
    description="Generate numbers and calculate basic statistics.",
)
def lab1_pipeline():
    """Build a small but non-trivial lab pipeline."""

    @task
    def generate_numbers() -> list[int]:
        """Return a deterministic list of integers for the next steps."""
        return [4, 8, 15, 16, 23, 42]

    @task
    def validate_numbers(numbers: list[int]) -> list[int]:
        """Ensure the pipeline input is not empty and contains integers."""
        if not numbers:
            raise ValueError("The input list must not be empty.")

        if not all(isinstance(number, int) for number in numbers):
            raise TypeError("All input values must be integers.")

        return numbers

    @task
    def calculate_statistics(numbers: list[int]) -> dict[str, float]:
        """Calculate a few basic descriptive statistics."""
        return {
            "count": float(len(numbers)),
            "sum": float(sum(numbers)),
            "min": float(min(numbers)),
            "max": float(max(numbers)),
            "mean": float(mean(numbers)),
        }

    @task
    def build_report(statistics_data: dict[str, float]) -> str:
        """Create a readable one-line report for the logs."""
        return (
            "Lab 1 pipeline completed successfully. "
            f"Count={statistics_data['count']:.0f}, "
            f"Sum={statistics_data['sum']:.0f}, "
            f"Min={statistics_data['min']:.0f}, "
            f"Max={statistics_data['max']:.0f}, "
            f"Mean={statistics_data['mean']:.2f}"
        )

    @task
    def print_report(report: str) -> None:
        """Write the final report to the Airflow task log."""
        print(report)

    numbers = generate_numbers()
    validated_numbers = validate_numbers(numbers)
    statistics_data = calculate_statistics(validated_numbers)
    report = build_report(statistics_data)
    print_report(report)


lab1_pipeline()
