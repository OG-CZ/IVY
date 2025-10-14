$(document).ready(function () {
  // display speak message
  function DisplayMessage(message) {
    const $msg = $(".siri-message");
    if ($msg.find("li").length) $msg.find("li:first").text(message);
    else $msg.text(message);
    if ($msg.textillate) $msg.textillate("start");
  }
  eel.expose(DisplayMessage);

  // display hood
  eel.expose(ShowHood);
  function ShowHood() {
    $("#Oval").attr("hidden", false);
    $("#SiriWave").attr("hidden", true);
  }

  eel.expose(senderText);
  function senderText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`;

      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }

  eel.expose(receiverText);
  function receiverText(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
      chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`;

      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
});
