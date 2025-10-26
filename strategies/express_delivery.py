"""
Express delivery strategy implementation.
Fast but expensive delivery option.
"""
from .delivery_strategy import DeliveryStrategy


class ExpressDelivery(DeliveryStrategy):
    """Express delivery - fast and guaranteed within 1 day."""
    
    # Constants for pricing calculation
    BASE_COST = 500
    COST_PER_KM = 25
    COST_PER_KG = 40
    DELIVERY_DAYS = 1
    
    def calculate_delivery(self, distance: float, weight: float) -> dict:
        """
        Calculate express delivery cost and time.
        More expensive but always delivered in 1 day.
        
        Args:
            distance: Distance in kilometers
            weight: Package weight in kilograms
            
        Returns:
            Dictionary with delivery cost and days
        """
        total_cost = (
            self.BASE_COST + 
            (distance * self.COST_PER_KM) + 
            (weight * self.COST_PER_KG)
        )
        
        return {
            'cost': round(total_cost, 2),
            'days': self.DELIVERY_DAYS
        }
    
    def get_name(self) -> str:
        """Return the name of this delivery method."""
        return "Express Delivery"
