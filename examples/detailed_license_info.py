from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_detailed_info():
    """Get and display detailed license information"""
    print("=" * 60)
    print("Example 2: Detailed License Information")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        info = validator.get_license_info(license_key)
        
        if not info:
            print(f"License key '{license_key}' not found")
            return
        
        print(f"License Status: {'✅ Valid' if info.is_valid else '❌ Invalid'}")
        print(f"Tier: {info.tier}")
        print(f"Active: {info.is_active}")
        print(f"Expired: {info.is_expired}")
        print(f"Starts: {info.starts_at}")
        print(f"Expires: {info.expires_at}")
        print(f"Days until expiry: {info.days_until_expiry}")
        print(f"\nSeats: {info.seats}")
        print(f"Features: {info.features}")
        print(f"Usage: {info.usage}")
        print(f"Within Limits: {info.within_limits}")
        print(f"Metadata: {info.metadata}")
        
    except LicenseValidationError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":
    example_detailed_info()