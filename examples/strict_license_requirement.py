from keystone import LicenseValidator, validate_license, LicenseValidationError
import sys

def example_require_license():
    """Require valid license or exit application"""
    print("=" * 60)
    print("Example 4: Strict License Requirement")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        # This will raise an exception if license is invalid
        info = validator.require_license(license_key)
        print("✅ License verified successfully!")
        print(f"   Running with {info.tier} tier access")
        
        # Continue with application logic...
        print("   Application starting...")
        
    except LicenseValidationError as e:
        print(f"❌ License validation failed: {e}")
        print("   Application cannot start without valid license")
        sys.exit(1)
    print()

if __name__ == "__main__":
    example_require_license()