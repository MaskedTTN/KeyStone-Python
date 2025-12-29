from keystone import LicenseValidator, validate_license, LicenseValidationError

def example_usage_limits():
    """Check usage against limits"""
    print("=" * 60)
    print("Example 9: Usage Limit Enforcement")
    print("=" * 60)
    
    license_key = "your-license-key-here"
    validator = LicenseValidator()
    
    try:
        info = validator.get_license_info(license_key)
        
        if not info or not info.is_valid:
            print("❌ Invalid license")
            return
        
        usage = info.usage
        within_limits = info.within_limits
        
        print("Usage Status:")
        for metric, status in within_limits.items():
            icon = "✅" if status else "❌"
            print(f"   {icon} {metric}: {'Within limits' if status else 'LIMIT EXCEEDED'}")
            
            if metric in usage:
                current = usage[metric].get('current', 0)
                limit = usage[metric].get('limit', 0)
                print(f"      Current: {current} / {limit}")
                
                if not status:
                    print(f"      ⚠️  Action required: Reduce usage or upgrade")
                    
    except LicenseValidationError as e:
        print(f"Error: {e}")
    print()

if __name__ == "__main__":  
    example_usage_limits()