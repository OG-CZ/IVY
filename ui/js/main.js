$(document).ready(function () {
  $(".text").textillate({
    loop: true,
    sync: false,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });

  // siri configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: 1,
    speed: "0.10",
    autostart: true,
  });

  // ivy message animation
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutUp",
      sync: true,
    },
  });

  // mic button click event
  $("#MicBtn").click(function (e) {
    // eel.play_assistant_sound();
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.all_commands()();
  });

  // key word detection
  function doc_keyUp(e) {
    if (e.key === "i" && (e.metaKey || e.ctrlKey)) {
      //   eel.playAssistantSound();
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.all_commands()();
    }
  }
  document.addEventListener("keyup", doc_keyUp, false);
});
