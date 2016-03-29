var mongodb = require('mongodb');
var assert      = require('assert');
//We need to work with "MongoClient" interface in order to connect to a mongodb server.
var MongoClient = mongodb.MongoClient;

var exec = require('child_process').exec;
exec('mongod');
//exec('python ./classify.py');



// Connection URL. This is where your mongodb server is running.
var url = 'mongodb://localhost:27017/test';

var os = require("os");

pass="";
var findRecords = function(db, callback) {
   
   var cursor =db.collection('meta').find({"title":"The Incredible Hulk: Return of the Beast  [VHS]"}, {"asin":1,_id:0}).limit(1);
   cursor.each(function(err, doc) {
     assert.equal(err, null);
	 if (doc != null) {
		  
		  var arr =  JSON.stringify(doc).split(':');
          key = arr[1];
	      key = key.replace(/^"(.*)"}$/, '$1');
	      pass=key;
	      console.log(pass);
		  back(pass);
		  } 
        
   });
  


 
 var fs =require('fs');
 
 function back(pass){
      var cursor =db.collection('review').find({"asin":pass}, {"reviewText":1,_id:0});
      cursor.each(function(err, doc) {
      assert.equal(err, null);
      if (doc != null) {
		    var arr =  JSON.stringify(doc).split(':');
            var key = arr[1];
	        key = key.replace(/^"(.*)"}$/, '$1');
			console.log(key);
			key=key+"\n";
			fs.appendFile("temp.txt", key, callback,function(err) {
       if(err) {
                return console.log(err);
                     }

         });
			
	} 
	
	else {
         callback();
          }

 });
 
 //create socket connection	
 function callback(err,res){
var net = require('net');
var HOST = '127.0.0.1';
var PORT = 12345;
var client = new net.Socket();

client.connect(PORT, HOST, function() {
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);

});
 }
   
     } 
   
 };

 

   
   

MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);

  findRecords(db, function() {
      db.close();
  });
});   
		//Close connection
    

