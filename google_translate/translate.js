/**
 * Created by hkh on 2017-06-23.
 */
const token = require('google-translate-token');
const http = require('http');
const Queue = require('sync-queue');
const querystring = require('querystring');
const fs = require('fs');
const lineReader = require('readline').createInterface({
    // input: fs.createReadStream('short_en.txt')
    input: fs.createReadStream('caption_list_en.txt')
});
const writter = fs.createWriteStream('translated_short_ko.txt', {
    flags: 'a'
});
const url_prefix = "http://translate.google.com/translate_a/single?client=t&sl=en&tl=ko&dt=at&ie=UTF-8&oe=UTF-8";
const DELAY_MILLIS = 200;

var linenum = 1;
var queue = new Queue();
lineReader.on('line', function(line){
    if (linenum > 2410) {
        queue.place(function(){
            translate(line.trim());
        });
    }
    linenum++;
});

var translate = function(text) {
    token.get(text).then(function(result){
        var tk=result['value'];
        var escaped_text = querystring.escape(text);
        var url = url_prefix+"&tk="+tk+"&q="+escaped_text;
        var data = "";
        // console.log(url);
        http.get(url, function(res){
            res.setEncoding('utf8');
            res.on('data', function (chunk) {
                data += chunk;
            });
            res.on('end', function() {
                extract_result(data);
            });
        });
    });
};

var extract_result = function(data){
    try {
        var jsondata = JSON.parse(data);
        var nbest = jsondata[jsondata.length-1][0][2];
        var ko_text = nbest[0][0];
        console.log(ko_text);
        writter.write(ko_text+"\n");

    } catch (e) {
        console.log(e);
        writter.write("[error]\n")
    }

    setTimeout(function(){
        queue.next();
    }, DELAY_MILLIS);
};