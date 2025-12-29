from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_error_handling():
    """Demonstrate proper error handling"""
    print("=" * 60)
    print("Example 12: Error Handling")
    print("=" * 60)
    
    license_key = "invalid-key-12345"
    validator = LicenseValidator(timeout=5)
    
    try:
        info = validator.get_license_info(license_key)
        
        if info is None:
            print("❌ License not found")
            print("   Please check your license key")
        elif not info.is_valid:
            if info.is_expired:
                print("❌ License expired")
                print(f"   Expired on: {info.expires_at}")
                print("   Please renew your license")
            else:
                print("❌ License is inactive")
                print("   Please contact support")
        else:
            print("✅ License valid")
            
    except LicenseValidationError as e:
        error_msg = str(e)
        
        if "timed out" in error_msg:
            print("❌ Connection timeout")
            print("   Please check your internet connection")
        elif "Failed to connect" in error_msg:
            print("❌ Cannot reach license server")
            print("   Please check network connectivity")
        else:
            print(f"❌ Validation error: {e}")
            print("   Please contact support")
    print()

if __name__ == "__main__":  
    example_error_handling()