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
});
