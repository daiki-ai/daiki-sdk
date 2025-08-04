/*!
 * Daiki SDK Javascript version
 *
 * Copyright 2025, DAIKI GmbH
 * All rights reserved
 */

(function (window, undefined) {
    
    var XHR = (function() {
      var that = {
        send: function(url, payload, successCallback, failureCallback) {
          var body = JSON.stringify(payload);
          
          var xhr = new XMLHttpRequest();
          if (successCallback) {
            xhr.onload = function() {
                if (successCallback) {
                  successCallback(xhr.response);
                }
                else {
                  console.debug(xhr.response);
                }
            };
          }
    
          if (failureCallback) {
            xhr.onerror = function() {
                if (failureCallback) {
                    failureCallback(xhr.response);
                  }
                  else {
                    console.error(xhr.response);
                  }
            };
          }
    
          xhr.open('POST', url);
          xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
          xhr.send(body);
        }
      };
      return that;
    })();
    
    var endpoint       = 'https://app.dai.ki/api/v1/events/';
    var name           = 'daiki.sdk.js';
    var version        = '1.0.0';
    var appID          = null;
    
    var getNewAppID = function() {
      var id = '';
      for (var i=0; i < 20; i++) {
        id += Math.floor(16*Math.random()).toString(16);
      }
      return id;
    };
    
    var Daiki = {
      /** Sets the app ID. */
      setAppID: function(newAppID) {
        appID = newAppID;
      },
      
      /** Send a tracking event.
        *
        * Example:
        * Daiki.send('some_event', { 'some_param': 'some-value' });
        */
      send: function(event, params, successCallback, failureCallback) {
        if (!appID) {
            var error = new Error('AppID is required. Please set the AppID using Daiki.setAppID() or Daiki.appStarted().');
            if (failureCallback) {
                failureCallback(error);
            }
            else {
                throw error;
            }
        }
        params = params || {}
        payload = {}
        payload['event'] = event
        payload['appID'] = appID
        payload['sdk'] = name
        payload['version'] = version
        payload['params'] = JSON.stringify(params)
        XHR.send(endpoint, payload, successCallback, failureCallback);
      },
      
      /**
       * App started event. 
       */
      appStarted: function(newAppID, params, successCallback, failureCallback) {
        appID = newAppID || appID;
        this.send('app_start', params, successCallback, failureCallback);
      },

      /**
       * Custom app event.
       */
      event: function(event, eventValues, successCallback, failureCallback) {
        this.send(event, eventValues, successCallback, failureCallback);
      }
    };
    
    window.Daiki = Daiki;
})(window);