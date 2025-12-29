from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_seat_management():
    """Check available seats and enforce seat limits"""
    print("=" * 60)
    print("Example 7: Seat Management")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        info = validator.get_license_info(license_key)
        
        if not info or not info.is_valid:
            print("❌ Invalid license")
            return
        
        seats = info.seats
        total = seats.get('total', 0)
        used = seats.get('used', 0)
        available = total - used
        
        print(f"Seat Information:")
        print(f"   Total seats: {total}")
        print(f"   Used seats: {used}")
        print(f"   Available: {available}")
        
        if available > 0:
            print(f"\n✅ Can add {available} more user(s)")
        else:
            overage_allowed = seats.get('overage_allowed', False)
            if overage_allowed:
                print("\n⚠️  All seats used, but overage is allowed")
                overage_price = seats.get('overage_price_per_seat', 0)
                print(f"   Additional seat cost: ${overage_price}/seat")
            else:
                print("\n❌ All seats used. Upgrade required for more users")
                
    except LicenseValidationError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":  
    example_seat_management()