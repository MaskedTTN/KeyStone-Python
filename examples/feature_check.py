from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_feature_flags():
    """Check if specific features are enabled"""
    print("=" * 60)
    print("Example 8: Feature Flag Checking")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        info = validator.get_license_info(license_key)
        
        if not info or not info.is_valid:
            print("❌ Invalid license")
            return
        
        features = info.features
        
        # Check individual features
        features_to_check = [
            "api_access",
            "advanced_analytics",
            "custom_branding",
            "priority_support"
        ]
        
        print("Feature Availability:")
        for feature in features_to_check:
            enabled = features.get(feature, {}).get('enabled', False)
            status = "✅ Enabled" if enabled else "❌ Disabled"
            print(f"   {feature}: {status}")
            
            if enabled:
                limit = features.get(feature, {}).get('limit')
                if limit:
                    print(f"      Limit: {limit}")
                    
    except LicenseValidationError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":  
    example_feature_flags()