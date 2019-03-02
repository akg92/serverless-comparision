const impl = require('./impl');
const provider = require('./provider');
const providerType = 'Test';

exports.handler = async (event,context,callback) => {
    // TODO implement
    
    // Current UTC time
    
    var cloudHandler = provider.getProvider(providerType,event,context,callback);
    var query = cloudHandler.getQueryParam("name");
    var start_time = new Date().getTime();
    //var q_time_response = impl.response_builder(time);
    var response=null; // reponse do a dummy reading. You can check the response incase of debugging required.
    var additional_info = null;
    switch(query){
        
        case "add":
            response = await impl.add();
            break;
        case "request":
            response = await impl.request();
            break;
        case "matmul":
            response = await impl.matrix_mul(100);
            break;
        case "io":
            response = await impl.io();
            break;
        case "memory":
            // do mat mul first
            response = await impl.matrix_mul(200);
            additional_info = await impl.memory_usage();
            break;
        case "container":
            additional_info = await impl.write_thread_count();
            break;// chumma :).
    }
    var end_time = new Date().getTime();
    /*
        New response.
        Format is {server_start_time:,server_end_time:}
    */
    response = impl.response_builder_new(start_time,end_time,additional_info);


    // write the response
    cloudHandler.writeResponse(response);
};
