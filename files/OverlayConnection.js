// Original Script by AwakenedDragons from Image On Command. Website: 'https://www.awakeneddragons.com',
var Overlay = {
  Listen: function() {
    this.socket = new WebSocket(API_Socket);
    //---------------------------------
    // Open Event
    //---------------------------------
    this.socket.onopen = function() {
      // Format your Authentication Information
      var auth = {
        author: `GreatNate`,
        website: 'www.twitch.com/GreatisNate',
        api_key: API_Key,
        events: ['ev1Image','ev2Image','ev3Image']
      };
      // Send your Data to the server
      Overlay.socket.send(JSON.stringify(auth));
    }

    //---------------------------------
    // Error Event
    //---------------------------------
    this.socket.onerror = function(error) {
      // Something went terribly wrong... Respond?!
      console.log('Error: ' + error);
    }

    //---------------------------------
    // Message Event
    //---------------------------------
    this.socket.onmessage = function(message) {
      var json = JSON.parse(message.data);
      var args = JSON.parse(json.data);
      document.getElementById(json.event).src = args.srclink
      document.getElementById(json.event).height = args.height
      // You have received new data now process it
      console.log(message);
    }

    //---------------------------------
    // Close Event
    //---------------------------------
    this.socket.onclose = function() {
      // Connection has been closed by you or the server
      console.log('Connection Closed!');
    }
  }
}

//---------------------------------
// API KEY Check
//---------------------------------
if (typeof API_Key === "undefined") {
  throw new Error("API Key not loaded or missing.");
}

// Start Script
Overlay.Listen();