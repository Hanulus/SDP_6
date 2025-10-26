"""
Abstract base class for all delivery strategies.
Defines the interface that all concrete strategies must implement.
"""
from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    """
    Abstract delivery strategy class.
    All concrete delivery strategies must inherit from this class.
    """
    
    @abstractmethod
    def calculate_delivery(self, distance: float, weight: float) -> dict:
        """
        Calculate delivery cost and time.
        
        Args:
            distance: Distance in kilometers
            weight: Package weight in kilograms
            
        Returns:
            Dictionary with 'cost' and 'days' keys
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """
        Get the name of the delivery method.
        
        Returns:
            String with delivery method name
        """
        pass
