"""
Pickup delivery strategy implementation.
Customer picks up the package themselves - cheapest option.
"""
from .delivery_strategy import DeliveryStrategy


class PickupDelivery(DeliveryStrategy):
    """Pickup delivery - customer collects package from pickup point."""
    
    # Constants for pricing calculation
    COST_PER_KG = 10  # Storage cost per kilogram
    DELIVERY_DAYS = 0  # Available immediately
    
    def calculate_delivery(self, distance: float, weight: float) -> dict:
        """
        Calculate pickup delivery cost.
        Cost only depends on weight (storage cost), not distance.
        
        Args:
            distance: Distance in kilometers (not used for pickup)
            weight: Package weight in kilograms
            
        Returns:
            Dictionary with delivery cost and days
        """
        storage_cost = weight * self.COST_PER_KG
        
        return {
            'cost': round(storage_cost, 2),
            'days': self.DELIVERY_DAYS
        }
    
    def get_name(self) -> str:
        """Return the name of this delivery method."""
        return "Pickup Point"
