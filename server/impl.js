
const https = require('https');
exports.add =  ()=>{
    
    let time =  Date.now();
    var response = response_builder(time);
    return response;
}

exports.request = async ()=>{
    
    
    var id = randomInt();
    var base_url = 'https://jsonplaceholder.typicode.com/todos/';
    var full_url = base_url + id;
    let response = await get_request(full_url);
    
    return null;
    
    
}

exports.matrix_mul = (n)=>{
    // Initialize random matrix without zeros
    var mat = initialize_random_mat(n);

    // Perform multiplication with itself
    var res = [];
    for(var i=0;i<n;i++){
        res[i] = []
        for(var j=0;j<n;j++){
            curres = 0
            for(var k=0;k<n;k++){
                curres = curres + (mat[i][k] * mat[k][j]);
            }
             res[i][j] = curres;    
        }
    }
    return res

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
exports.response_builder = (str)=>{
    
    var rsp = {};
    rsp.q_time = str;
    return JSON.stringify(rsp);
}

var initialize_random_mat = (n)=>{
    var mat = [];
    for (var i = 0 ; i < n; i++) {
        mat[i] = [];
        for (var j = 0; j < n; j++) {
            mat[i][j] = (Math.random() * (Number.MAX_VALUE - 1) + 1.0);
        }
    }
    return mat;
}

