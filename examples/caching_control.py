from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_caching():
    """Demonstrate cache usage and control"""
    print("=" * 60)
    print("Example 10: Caching Control")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    
    # Create validator with custom cache duration (5 minutes)
    validator = LicenseValidator(cache_duration=300)
    
    # First call - hits API
    print("First validation (hits API)...")
    info1 = validator.get_license_info(license_key, use_cache=True)
    if info1:
        print(f"✅ Result: {info1.tier}")
    
    # Second call - uses cache
    print("\nSecond validation (uses cache)...")
    info2 = validator.get_license_info(license_key, use_cache=True)
    if info2:
        print(f"✅ Result: {info2.tier} (from cache)")
    
    # Force fresh API call
    print("\nForced validation (bypasses cache)...")
    info3 = validator.get_license_info(license_key, use_cache=False)
    if info3:
        print(f"✅ Result: {info3.tier} (fresh from API)")
    
    # Clear cache
    print("\nClearing cache...")
    validator.clear_cache()
    print("✅ Cache cleared")
    print()

if __name__ == "__main__":  
    example_caching()