
class Base{

    getQueryParam(paramName){
        return null;
    }

    writeResponse(response){
        
    }

    createResponse(){
        var time = Date.now();
        var response = {} ;
        response.q_time = time;
        return JSON.stringify(response);
    }
}


/*
    Aws code goes here.
*/
class AWS extends Base {


    constructor(event,context,callback){
        super();
        this.event = event;
        this.context = context;
        this.callback  = callback;
    }
    writeResponse(response){
        if(!response){
            response = createResponse();
        }
        this.callback(response);
    }

    getQueryParam(paramName){
        //implement the quer prame
        return this.event.params.querystring[paramName];
    }
}
/*
  Azure code goes here.
*/
class Azure extends Base {

    constructor(context,request){
        super();
        this.context = context;
        this.request = request;
    }

    getQueryParam(paramName){
        // Return the required Query Parameter
        return this.request.query.paramName;
    } 

    writeResponse(response){
        // Response being sent as a JSON string in the body part of the actual response
         if(!response){
            response = this.createResponse();
        }
        this.context.res = {
            body: response
        }
    }

}

/*
    Test code goes here
*/

class TestProvider extends Base{

    constructor(req,res){
        super();
        this.req = req;
        this.res = res;
    }
    getQueryParam(paramName){
        return  this.req.query[paramName];
    }
    writeResponse(response){
        
        if(!response){
            response = this.createResponse();
        }
        this.res.send(response);

    }
    
}


exports.getProvider=(providerType,param1,param2,param3)=>{

    switch(providerType){

        case "AWS":
            return new AWS(param1,param2,param3);
        case "Azure":
            return new Azure(param1,param2);
        default:
            return new TestProvider(param1,param2);
    }
}