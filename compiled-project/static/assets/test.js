$(document).ready(function (){
    let iv = "THis is a   R454"
    let key = "This is a key123"
    let KEY = CryptoJS.enc.Utf8.parse(key.toString());
    let IV = CryptoJS.enc.Utf8.parse(iv.toString())

    function encrypto(message,KEY,IV){
        let e_text = CryptoJS.AES.encrypt(message, KEY, { iv: IV});
        return e_text
    };
    function decrypto(message,KEY,IV){
        let d_text = CryptoJS.AES.decrypt(message, KEY, { iv: IV });
        var f_text = d_text.toString(CryptoJS.enc.Utf8)
        return f_text
    };
    var test = encrypto("hello",KEY,IV);
    console.log(test.toString());
    var e = test.toString()
    var test2 = decrypto(e,KEY,IV);
    console.log(test2);
});