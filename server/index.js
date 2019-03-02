const impl = require('./impl');
const provider = require('./provider');
const providerType = 'GCP';

exports.handler = async (event,context,callback) => {
    // TODO implement
    
    // Current UTC time
    var time = new Date().getTime();
    var cloudHandler = provider.getProvider(providerType,event,context,callback);
    var query = cloudHandler.getQueryParam("name");
    var response = null;
    switch(query){
        
        case "add":
            //response = await impl.add();
            response = String(time)
            break;
        case "request":
            response = await impl.request();
    }

    // write the response
    cloudHandler.writeResponse(response);
};
