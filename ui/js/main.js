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

  function PlayAssistant(message) {
    if (message != "") {
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.all_commands(message);
      $("#chatbox").val("");
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    }
  }

  // toogle fucntion to hide and display mic and send button
  function ShowHideButton(message) {
    if (message.length == 0) {
      $("#MicBtn").attr("hidden", false);
      $("#SendBtn").attr("hidden", true);
    } else {
      $("#MicBtn").attr("hidden", true);
      $("#SendBtn").attr("hidden", false);
    }
  }

  $("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    ShowHideButton(message);
  });

  // send button event handler
  $("#SendBtn").click(function () {
    let message = $("#chatbox").val();
    PlayAssistant(message);
  });

  // enter keyword
  $("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
      let message = $("#chatbox").val();
      PlayAssistant(message);
    }
  });
});
