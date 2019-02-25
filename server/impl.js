
const https = require('https');
exports.add = async ()=>{
    
    let time =  Date.now();
    var respone = response_builder(time);
    return response;
}


exports.request = async()=>{
    
    
    var id = randomInt();
    var base_url = 'https://jsonplaceholder.typicode.com/todos/';
    var full_url = base_url + id;
    let response = await get_request(full_url);
    
    return null;
    
    
}

var get_request = (url)=>{
    
    return new Promise((resolve,reject)=>{
        https.get(url,(resp)=>{
            resp.on('data',(d)=>resolve(d));
            resp.on('error',(e)=>reject(e));
        })
    }
    );
}
var randomInt = ()=>{
    const max = 1000;
    return Math.floor(Math.random()*max);
}
var write_rsponse=(callback)=>{
    
    let time =  Date.now();
    var respone = response_builder(time);
    callback(null,respone);
}
var response_builder = (str)=>{
    
    var rsp = {};
    rsp.q_time = str;
    return JSON.stringify(rsp);
}