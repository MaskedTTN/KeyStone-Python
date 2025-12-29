from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_startup_check():
    """Complete startup validation flow"""
    print("=" * 60)
    print("Example 11: Application Startup Check")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    print("Starting application...")
    print("Validating license...\n")
    
    try:
        # Require valid license
        info = validator.require_license(license_key)
        
        # Show license info
        print(f"✅ License validated successfully")
        print(f"   Tier: {info.tier}")
        print(f"   Expires: {info.expires_at}")
        
        # Check expiry warning
        if info.days_until_expiry <= 30:
            print(f"\n⚠️  License expires in {info.days_until_expiry} days")
        
        # Check seats
        seats = info.seats
        used = seats.get('used', 0)
        total = seats.get('total', 0)
        print(f"\n📊 Seats: {used}/{total} used")
        
        # Check critical features
        features = info.features
        if features.get('api_access', {}).get('enabled'):
            print("✅ API access enabled")
        
        print("\n🚀 Application ready!")
        return True
        
    except LicenseValidationError as e:
        print(f"\n❌ Startup failed: {e}")
        print("   Please contact support or renew your license")
        return False
    print()

if __name__ == "__main__":  
    example_startup_check()