from keystone import LicenseValidator, validate_license, LicenseValidationError
import sys

from simple_validation import example_simple_validation
from detailed_license_info import example_detailed_info
from tier_based_license import example_tier_gating
from strict_license_requirement import example_require_license
from min_tier import example_require_minimum_tier
from expiry_warning import example_expiry_warnings
from seat_mgmt import example_seat_management
from feature_check import example_feature_flags
from usage_limit import example_usage_limits
from caching_control import example_caching
from app_startup_check import example_startup_check
from error_handling import example_error_handling


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("KeyStone Library - Complete Examples")
    print("=" * 60 + "\n")
    
    # Uncomment the examples you want to run:
    
    example_simple_validation()
    example_detailed_info()
    example_tier_gating()
    example_require_license()
    example_require_minimum_tier()
    example_expiry_warnings()
    example_seat_management()
    example_feature_flags()
    example_usage_limits()
    example_caching()
    example_startup_check()
    example_error_handling()
    
    print("\n" + "=" * 60)
    print("Examples complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    # Quick test if license key provided as argument
    if len(sys.argv) > 1:
        license_key = sys.argv[1]
        print(f"\nTesting license: {license_key}\n")
        
        validator = LicenseValidator()
        try:
            info = validator.get_license_info(license_key)
            if info and info.is_valid:
                print("✅ License is valid!")
                print(f"   Tier: {info.tier}")
                print(f"   Expires: {info.expires_at}")
            else:
                print("❌ License is invalid or not found")
        except LicenseValidationError as e:
            print(f"❌ Error: {e}")
    else:
        # Run all examples
        main()