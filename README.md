# Daiki SDK

A minimal Python and Javascript SDK for the Daiki AI Governance platform.

https://dai.ki

## Python

### Installation

Simply copy the `daiki_sdk.py` file to your project directory and import it.

### Quick Start

```python
from daiki_sdk import daiki

# Set your app ID and send app started event
daiki.app_started("your-app-id", {"user_id": "user123"})

# Send custom events
daiki.event("ai_chat_started", {"llm": "chatgpt-o4", "mode": "app"})
```

### API Reference

#### `DaikiSDK` Class

#### `set_app_id(new_app_id: str)`
Set the application ID.

#### `app_started(new_app_id: Optional[str] = None, params: Optional[Dict] = None, success_callback: Optional[Callable] = None, failure_callback: Optional[Callable] = None)`
Send an app started event. If `new_app_id` is provided, it will be set as the current app ID.

#### `event(event: str, event_values: Optional[Dict] = None, success_callback: Optional[Callable] = None, failure_callback: Optional[Callable] = None)`
Send a custom event.
Note that events are automatically grouped by the Daiki platform. Just make sure that equal events have the same name.

### Error Handling

The SDK will throw a `ValueError` if you try to send events without setting an app ID:

```python
from daiki_sdk import DaikiSDK

sdk = DaikiSDK()
daiki.app_started("my-app")

try:
    sdk.event("test_event", {"test": "value"})
except ValueError as e:
    print(f"Error: {e}")  # AppID is required. Please set the AppID using set_app_id() or app_started().
```

### Callbacks

You can provide success and failure callbacks for all event methods:

```python
def on_success(response):
    print(f"Event sent successfully: {response}")

def on_failure(error):
    print(f"Event failed: {error}")

daiki.event("test_event", {"data": "value"}, on_success, on_failure)
```

### Requirements

- Python 3.6+
- Standard library modules: `json`, `random`, `string`, `urllib.request`, `urllib.error`, `typing`

No external dependencies required.

## Daiki JavaScript SDK

### Installation

Include the SDK in your HTML page:

```html
<script src="daiki-sdk.js"></script>
```

### Quick Start

```javascript
// Initialize with app ID and send app started event
Daiki.appStarted("your-app-id", { "user_id": "user123" });

// Send custom events
Daiki.event("ai_chat_started", { "llm": "chatgpt-4", "mode": "app" });
```

### API Reference

#### `Daiki.setAppID(newAppID)`
Set the application ID.

#### `Daiki.appStarted(newAppID, params, successCallback, failureCallback)`
Send an app started event. If `newAppID` is provided, it will be set as the current app ID.

**Parameters:**
- `newAppID` (optional): New app ID to set
- `params` (optional): Additional parameters to send with the event
- `successCallback` (optional): Function called on successful request
- `failureCallback` (optional): Function called on failed request

#### `Daiki.event(event, eventValues, successCallback, failureCallback)`
Send a custom event.

**Parameters:**
- `event`: Event name
- `eventValues` (optional): Event parameters
- `successCallback` (optional): Function called on successful request
- `failureCallback` (optional): Function called on failed request

Note that events are automatically grouped by the Daiki platform. Just make sure that equal events have the same name.

### Error Handling

The SDK will throw an error if you try to send events without setting an app ID:

```javascript
try {
    Daiki.send("test_event", { "test": "value" });
} catch (error) {
    console.error("Error:", error.message); 
    // "AppID is required. Please set the AppID using Daiki.setAppID() or Daiki.appStarted()."
}
```

### Callbacks

You can provide success and failure callbacks for all event methods:

```javascript
function onSuccess(response) {
    console.log("Event sent successfully:", response);
}

function onFailure(error) {
    console.error("Event failed:", error);
}

Daiki.event("test_event", { "data": "value" }, onSuccess, onFailure);
```

### Usage Examples

#### Basic Setup
```html
<!DOCTYPE html>
<html>
<head>
    <script src="daiki-sdk.js"></script>
</head>
<body>
    <script>
        // Initialize the SDK
        Daiki.appStarted("my-app-123", { "user_id": "user123" });
    </script>
</body>
</html>
```

#### Tracking AI Interactions
```javascript
// Track AI chat started
Daiki.event("ai_chat_started", {
    "llm": "chatgpt-4",
    "mode": "app",
    "user_type": "premium"
});

// Track AI response received
Daiki.event("ai_response_received", {
    "response_time": 1500,
    "tokens_used": 250
});

// Track user feedback
Daiki.event("ai_feedback", {
    "rating": 5,
    "feedback_type": "thumbs_up"
});
```

#### Tracking User Actions
```javascript
// Track button clicks
document.getElementById("submit-btn").addEventListener("click", function() {
    Daiki.event("button_click", {
        "button_id": "submit",
        "page": "dashboard"
    });
});

// Track page views
Daiki.event("page_view", {
    "page": "settings",
    "referrer": "dashboard"
});
```

### Requirements

- Modern web browser with XMLHttpRequest support
- No external dependencies required

### Browser Support

The SDK works in all modern browsers that support:
- XMLHttpRequest
- JSON.stringify/parse
- ES5 JavaScript features 