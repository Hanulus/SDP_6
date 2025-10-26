"""
Main application demonstrating Strategy Pattern.
Shows how different delivery strategies can be switched at runtime.
"""
from strategies import StandardDelivery, ExpressDelivery, PickupDelivery
from services import DeliveryService


def main():
    """Main function demonstrating Strategy Pattern usage."""
    
    print("🚚 DELIVERY SYSTEM - STRATEGY PATTERN DEMONSTRATION\n")
    
    # Create delivery service with initial strategy
    delivery_service = DeliveryService(StandardDelivery())
    
    # Order parameters
    distance = 150  # kilometers
    weight = 5      # kilograms
    
    print(f"📦 Order details: {distance} km distance, {weight} kg weight\n")
    
    # Test all strategies with the same order
    
    # Strategy 1: Standard delivery
    delivery_service.calculate_order_delivery(distance, weight)
    
    # Strategy 2: Express delivery
    delivery_service.set_strategy(ExpressDelivery())
    delivery_service.calculate_order_delivery(distance, weight)
    
    # Strategy 3: Pickup delivery
    delivery_service.set_strategy(PickupDelivery())
    delivery_service.calculate_order_delivery(distance, weight)
    
    print_advantages()


def print_advantages():
    """Print advantages of Strategy Pattern."""
    print("\n✅ Strategy Pattern Advantages:")
    print("• Easy to add new delivery methods")
    print("• Can change strategy at runtime")
    print("• Each strategy is encapsulated in its own class")
    print("• Follows Open/Closed Principle")
    print("• Clean and maintainable code structure")


if __name__ == "__main__":
    main()
