

window.onload = function () {

    // Wait 2 seconds (2000ms) then hide the message
setTimeout(function() {
    let msg = document.getElementById('msg-alert');
    if(msg){
        msg.style.display='none';
    }
}, 2000);
}
