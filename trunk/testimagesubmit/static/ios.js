function getpicture(callback) {
   // fakely redirect webview to a natively known url. Since the native part will intercept this and prevent
   // the actual naviation, the location won't change and we are able to delegate the call the native part
   document.location = 'native://getpicture/' + callback;
}


