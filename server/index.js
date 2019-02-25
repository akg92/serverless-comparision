const impl = require('impl');
const provider = require('require');
const providerType = 'Test';

exports.handler = async (event,context,callback) => {
    // TODO implement
    

    var cloudHandler = provider.getProvider(providerType,event,context,callback);
    var query = cloudHandler.getQueryParam("name");
    var response = null;
    switch(query){
        
        case "add":
            response = impl.add();
        case "request":
            response = impl.request();
    }

    // write the response
    cloudHandler.writeResponse(response);
};
