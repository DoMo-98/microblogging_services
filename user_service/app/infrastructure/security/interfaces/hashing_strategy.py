"""
HashingStrategy interface
"""

from abc import ABC, abstractmethod


class HashingStrategy(ABC):
    """
    HashingStrategy interface
    """

    @abstractmethod
    def hash(self, input_data: str) -> str:
        """
        Hash input data
        """
