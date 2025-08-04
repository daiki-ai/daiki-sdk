#!/usr/bin/env python3
"""
Example usage of the Daiki Python SDK
"""

from daiki_sdk import DaikiSDK


def success_callback(response):
    print(f"✅ Success: {response}")


def failure_callback(error):
    print(f"❌ Error: {error}")


def main():
    # Create a new instance
    daiki = DaikiSDK("my-app-123")

    # Example 1: Set app ID and send app started event
    print("=== Example 1: App Started Event ===")
    daiki.app_started("my-app-123", {"user_id": "user123"}, success_callback, failure_callback)
    
    # Example 2: Send custom event
    print("\n=== Example 2: Custom Event ===")
    daiki.event("ai_chat_started", {"llm": "chatgpt-o4", "mode": "app"}, success_callback, failure_callback)
    
    # Example 3: Error handling - trying to send without app ID
    print("\n=== Example 3: Error handling ===")
    # Create a new instance without app ID to demonstrate error
    test_sdk = DaikiSDK()
    
    try:
        test_sdk.event("test_event", {"test": "value"})
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    # Example 4: Using set_app_id method
    print("\n=== Example 4: Using set_app_id ===")
    test_sdk.set_app_id("another-app-456")
    test_sdk.event("test_event", {"test": "value"}, success_callback, failure_callback)


if __name__ == "__main__":
    main() 