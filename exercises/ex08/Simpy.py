"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730460892"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initialize a new Simpy object."""
        self.values = values  
    
    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill our values array by mutating object called on."""
        # Start with an empty values list
        self.values = []
        # Loop for 'times' number of times
        i: int = 0
        while i < times:
            # Append value parameter to the values list
            self.values.append(value)