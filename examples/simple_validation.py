from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_simple_validation():
    """Basic license validation - just check if valid or not"""
    print("=" * 60)
    print("Example 1: Simple Validation")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    
    # Method 1: Using the convenience function
    if validate_license(license_key):
        print("✅ License is valid!")
    else:
        print("❌ License is invalid")
    
    # Method 2: Using the validator class
    validator = LicenseValidator()
    if validator.validate(license_key):
        print("✅ License is valid!")
    else:
        print("❌ License is invalid")
    print()

if __name__ == "__main__":
    example_simple_validation()