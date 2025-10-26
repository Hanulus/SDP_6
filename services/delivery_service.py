"""
Delivery service context class.
Uses Strategy pattern to calculate deliveries with different strategies.
"""
from strategies.delivery_strategy import DeliveryStrategy


class DeliveryService:
    """
    Context class for Strategy pattern.
    Manages delivery calculation using selected strategy.
    """
    
    def __init__(self, strategy: DeliveryStrategy):
        """
        Initialize delivery service with a strategy.
        
        Args:
            strategy: Delivery strategy to use
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: DeliveryStrategy) -> None:
        """
        Change delivery strategy at runtime.
        This is the key feature of Strategy pattern!
        
        Args:
            strategy: New delivery strategy to use
        """
        self._strategy = strategy
        print(f"✓ Strategy changed to: {strategy.get_name()}")
    
    def calculate_order_delivery(self, distance: float, weight: float) -> dict:
        """
        Calculate delivery using current strategy.
        
        Args:
            distance: Delivery distance in kilometers
            weight: Order weight in kilograms
            
        Returns:
            Dictionary with cost and delivery days
        """
        self._print_order_info(distance, weight)
        
        result = self._strategy.calculate_delivery(distance, weight)
        
        self._print_result(result)
        
        return result
    
    def _print_order_info(self, distance: float, weight: float) -> None:
        """Print order information header."""
        print(f"\n{'='*50}")
        print(f"Delivery method: {self._strategy.get_name()}")
        print(f"Distance: {distance} km")
        print(f"Weight: {weight} kg")
    
    def _print_result(self, result: dict) -> None:
        """Print calculation result."""
        print(f"Cost: {result['cost']} KZT")
        print(f"Delivery time: {result['days']} days")
        print(f"{'='*50}")
