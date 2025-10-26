"""
Standard delivery strategy implementation.
Cheap but slow delivery option.
"""
from .delivery_strategy import DeliveryStrategy


class StandardDelivery(DeliveryStrategy):
    """Standard delivery - affordable and reliable."""
    
    # Constants for pricing calculation
    BASE_COST = 200
    COST_PER_KM = 10
    COST_PER_KG = 20
    BASE_DAYS = 3
    DAYS_PER_100KM = 1
    
    def calculate_delivery(self, distance: float, weight: float) -> dict:
        """
        Calculate standard delivery cost and time.
        Formula: base_cost + (distance * rate) + (weight * rate)
        
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
        
        delivery_days = self.BASE_DAYS + int(distance / 100)
        
        return {
            'cost': round(total_cost, 2),
            'days': delivery_days
        }
    
    def get_name(self) -> str:
        """Return the name of this delivery method."""
        return "Standard Delivery"
