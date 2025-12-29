from keystone import LicenseValidator, validate_license, LicenseValidationError
import sys

def example_require_minimum_tier():
    """Require a specific tier or higher"""
    print("=" * 60)
    print("Example 5: Require Minimum Tier")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        # Require at least "pro" tier
        info = validator.require_license(license_key, min_tier="pro")
        print("✅ Pro tier verified!")
        print(f"   Current tier: {info.tier}")
        print("   Starting premium features...")
        
    except LicenseValidationError as e:
        print(f"❌ License check failed: {e}")
        print("   Pro tier or higher required")
        sys.exit(1)
    print()

if __name__ == "__main__":
    example_require_minimum_tier()