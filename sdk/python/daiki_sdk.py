#!/usr/bin/env python3
"""
Daiki SDK Python version

Copyright 2025, DAIKI GmbH
All rights reserved
"""

import json
import random
import string
import urllib.request
import urllib.error
from typing import Optional, Dict, Any, Callable


class DaikiSDK:
    """Daiki SDK for Python applications."""
    
    def __init__(self, app_id: Optional[str] = None):
        self.endpoint = 'https://app.dai.ki/api/v1/events/'
        self.name = 'daiki.sdk.py'
        self.version = '1.0.0'
        self.app_id = app_id
    
    def _get_new_app_id(self) -> str:
        """Generate a new random app ID."""
        return ''.join(random.choices(string.hexdigits.lower(), k=20))
    
    def set_app_id(self, new_app_id: str) -> None:
        """Set the app ID."""
        self.app_id = new_app_id
    
    def _send_request(self, payload: Dict[str, Any], 
                     success_callback: Optional[Callable] = None,
                     failure_callback: Optional[Callable] = None) -> None:
        """Send HTTP request to the Daiki endpoint."""
        try:
            body = json.dumps(payload).encode('utf-8')
            
            # Create request
            req = urllib.request.Request(
                self.endpoint,
                data=body,
                headers={'Content-Type': 'application/json; charset=utf-8'},
                method='POST'
            )
            
            # Send request
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                if success_callback:
                    success_callback(response_data)
                else:
                    print(f"Success: {response_data}")
                    
        except urllib.error.URLError as e:
            error_msg = f"Request failed: {str(e)}"
            if failure_callback:
                failure_callback(error_msg)
            else:
                print(f"Error: {error_msg}")
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            if failure_callback:
                failure_callback(error_msg)
            else:
                print(f"Error: {error_msg}")
    
    def _send(self, event: str, params: Optional[Dict[str, Any]] = None,
             success_callback: Optional[Callable] = None,
             failure_callback: Optional[Callable] = None) -> None:
        """
        Send a tracking event.
        
        Example:
            daiki.send('some_event', {'some_param': 'some-value'})
        """
        if not self.app_id:
            error = ValueError('AppID is required. Please set the AppID using set_app_id() or app_started().')
            if failure_callback:
                failure_callback(error)
            else:
                raise error
        
        params = params or {}
        payload = {
            'event': event,
            'appID': self.app_id,
            'sdk': self.name,
            'version': self.version,
            'params': json.dumps(params)
        }
        
        self._send_request(payload, success_callback, failure_callback)
    
    def app_started(self, new_app_id: Optional[str] = None, 
                   params: Optional[Dict[str, Any]] = None,
                   success_callback: Optional[Callable] = None,
                   failure_callback: Optional[Callable] = None) -> None:
        """
        App started event.

        Example:
            daiki.app_started()
            daiki.app_started('my-app-123')
            daiki.app_started('my-app-123', {'user_id': 'user123'})
        """
        if new_app_id:
            self.app_id = new_app_id
        self._send('app_start', params, success_callback, failure_callback)
    
    def event(self, event: str, event_values: Optional[Dict[str, Any]] = None,
              success_callback: Optional[Callable] = None,
              failure_callback: Optional[Callable] = None) -> None:
        """
        Custom app event.

        Example:
            daiki.event("ai_chat_started", {"llm": "chatgpt-o4", "mode": "app"})
        """
        self._send(event, event_values, success_callback, failure_callback)
