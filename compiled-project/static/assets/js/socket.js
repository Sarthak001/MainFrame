$(document).ready(function () {

  const socket = io.connect('http://127.0.0.1:5000/');

 Terminal.applyAddon(fullscreen)
  Terminal.applyAddon(fit)
  Terminal.applyAddon(webLinks)
  Terminal.applyAddon(search)
  const term = new Terminal({
        cursorBlink: true,
        macOptionIsMeta: true,
        scrollback: true,
    });
      term.open(document.getElementById('terminal'));
      term.fit()
      term.write("Virtual console!!!\r\n")



  term.on('key', (key, ev) => {
    console.log("pressed key", key)
    console.log("event", ev)
    socket.emit("jspy",key)
  });


  socket.on('pyjs',function(output){
    console.log(output)
    term.write(output)
  });



  socket.on('conn',function(){
    ip = $('#ip').val()
    port = $('#port').val()
    user = $('#user').val()
    password = $('#passwd').val()
    var details = {

      'ip' : ip,
      'port' : port,
      'user' : user,
      'password' : password,
    };
    console.log(ip,port,user,password,details)

    socket.emit("conn",details)
  });








































});
