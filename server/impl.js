
const https = require('https');
const fs = require('fs');
const process = require('process');
exports.add = () => {

    let time = Date.now();
    var response = response_builder(time);
    return response;
}

exports.request = async () => {


    var id = randomInt();
    var base_url = 'https://jsonplaceholder.typicode.com/todos/';
    var full_url = base_url + id;
    let response = await get_request(full_url);

    return null;


}

exports.matrix_mul = (n) => {
    // Initialize random matrix without zeros
    var mat = initialize_random_mat(n);

    // Perform multiplication with itself
    var res = [];
    for (var i = 0; i < n; i++) {
        res[i] = []
        for (var j = 0; j < n; j++) {
            curres = 0
            for (var k = 0; k < n; k++) {
                curres = curres + (mat[i][k] * mat[k][j]);
            }
            res[i][j] = curres;
        }
    }
    return res

}

var write_file = (file_name, num_lines = 10000) => {

    var content = "";
    var time = new Date().getTime();
    // create random file content
    for (var i = 0; i < num_lines; i++) {
        var content = content + i + "hello baby. I love you" + time + "\n";
    }

    // make synchronized by blocking.
    fs.writeFileSync(file_name, content);
}

exports.io = async () => {

    var f_index = randomInt();
    var file_name = 'file_' + f_index + '.txt';
    write_file(file_name);
    //dummy return for the purpose of the unification.
    return null;

}
exports.write_thread_count = async () => {
    var file_name = 'thread_index.txt';
    var data = 0;
    try {
        if (fs.existsSync(file_name)) {
            data = fs.readFileSync(file_name);
        }
    }
    catch (err) {

    }
    data = parseInt(data) + 1;
    fs.writeFileSync(file_name, data);

    return data;
}
exports.memory_usage = async () => {

    var memory = process.memoryUsage();
    return memory.rss;
}

var get_request = (url) => {

    return new Promise((resolve, reject) => {
        https.get(url, (resp) => {
            resp.on('data', (d) => resolve(d));
            resp.on('error', (e) => reject(e));
        })
    }
    );
}
var randomInt = () => {
    const max = 1000;
    return Math.floor(Math.random() * max);
}
var write_rsponse = (callback) => {

    let time = Date.now();
    var respone = response_builder(time);
    callback(null, respone);
}
var response_builder = (str) => {

    var rsp = {};
    rsp.q_time = str;
    return JSON.stringify(rsp);
}
var response_builder_new = (start_time, end_time, additional_info) => {

    if (!additional_info) {
        additional_info = -1;
    }
    var rsp = {};
    rsp.server_start_time = start_time;
    rsp.server_end_time = end_time;
    rsp.additional_info = additional_info;
    return JSON.stringify(rsp);
}
exports.response_builder = response_builder;

exports.response_builder_new = response_builder_new;

var initialize_random_mat = (n) => {
    var mat = [];
    for (var i = 0; i < n; i++) {
        mat[i] = [];
        for (var j = 0; j < n; j++) {
            mat[i][j] = (Math.random() * (Number.MAX_VALUE - 1) + 1.0);
        }
    }
    return mat;
}

