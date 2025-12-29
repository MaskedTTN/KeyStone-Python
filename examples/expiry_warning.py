from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_expiry_warnings():
    """Warn users about upcoming license expiry"""
    print("=" * 60)
    print("Example 6: Expiry Warning System")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        info = validator.get_license_info(license_key)
        
        if not info or not info.is_valid:
            print("❌ Invalid license")
            return
        
        days_left = info.days_until_expiry
        
        if days_left == 0:
            print("🚨 URGENT: Your license expires today!")
        elif days_left <= 7:
            print(f"⚠️  WARNING: Your license expires in {days_left} days")
            print("   Please renew soon to avoid service interruption")
        elif days_left <= 30:
            print(f"ℹ️  Notice: Your license expires in {days_left} days")
        else:
            print(f"✅ License active ({days_left} days remaining)")
            
    except LicenseValidationError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":
    example_expiry_warnings()