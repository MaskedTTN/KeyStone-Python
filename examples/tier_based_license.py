from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_tier_gating():
    """Check license tier before enabling premium features"""
    print("=" * 60)
    print("Example 3: Tier-Based Feature Gating")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    # Check if user has pro tier or higher
    if validator.check_tier(license_key, "pro"):
        print("✅ Pro features unlocked!")
        print("   - Advanced analytics")
        print("   - Priority support")
        print("   - API access")
    else:
        print("❌ Pro tier required for these features")
        print("   Please upgrade your license")
    
    # Alternative: Get info and check tier manually
    try:
        info = validator.get_license_info(license_key)
        if info:
            if info.tier in ["pro", "premium"]:
                print("\n✅ Advanced features available")
            elif info.tier == "basic":
                print("\n⚠️  Basic tier - limited features")
    except LicenseValidationError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":
    example_tier_gating()