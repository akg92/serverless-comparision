const impl = require('./impl');
const provider = require('./provider');
const providerType = 'Test';

exports.handler = async (event,context,callback) => {
    // TODO implement
    

    var cloudHandler = provider.getProvider(providerType,event,context,callback);
    var query = cloudHandler.getQueryParam("name");
    var response = null;
    switch(query){
        
        case "add":
            response = await impl.add();
            break;
        case "request":
            response = await impl.request();
    }

    // write the response
    cloudHandler.writeResponse(response);
};
