mongo <<EOF

use System3;

db.createCollection("Sites");

db.Sites.insert({    
    "NetworkPath" : "C:\\Program Files\\MongoDB\\Server\\4.4\\data", 
    "DocStoragePath" : "C:\\Program Files\\MongoDB\\Server\\4.4\\data\\docs", 
    "SiteId" : NumberInt(1)
});

db.createCollection("Users");
db.Users.insert({    
    "UserName" : "sohail", 
    "Password" : "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", 
    "Version" : NumberLong(1)
});


EOF