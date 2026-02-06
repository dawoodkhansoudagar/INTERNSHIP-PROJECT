let recognition;
let isListening = false;
let isSpeaking = false;

function sendText() {
    const input = document.getElementById("textInput");
    const responseDiv = document.getElementById("response");
    const text = input.value.trim();

    if (!text) {
        responseDiv.innerText = "Please type something first 🙂";
        return;
    }

    responseDiv.innerText = "Thinking...";

    fetch(`http://127.0.0.1:5000/text?query=${encodeURIComponent(text)}`)
        .then(res => {
            if (!res.ok) {
                throw new Error("Server error");
            }
            return res.json();
        })
        .then(data => {
            console.log("Text response:", data); 
            responseDiv.innerText = data.response;
            speak(data.response); 
        })
        .catch(err => {
            console.error(err);
            responseDiv.innerText = "Backend not running";
        });

    input.value = ""; 
}



function startVoice() {
    const responseDiv = document.getElementById("response");
    const micBtn = document.getElementById("micBtn");
    const micIcon = document.getElementById("micIcon");

    if (!('webkitSpeechRecognition' in window)) {
        responseDiv.innerText = "Voice not supported in this browser";
        return;
    }

    if (isListening) return;

    recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    isListening = true;
    micBtn.classList.add("listening");
    micIcon.src = "../Front-End-For-ALL-Projects/img/microphone.png";

    responseDiv.innerText = "Listening...";

    recognition.onresult = function (event) {
        const spokenText = event.results[0][0].transcript;
        responseDiv.innerText = "You said: " + spokenText;

        recognition.stop();
        isListening = false;
        micBtn.classList.remove("listening");
        micIcon.src = "../Front-End-For-ALL-Projects/img/microphone.png";

        fetch(`http://127.0.0.1:5000/text?query=${encodeURIComponent(spokenText)}`)
            .then(res => res.json())
            .then(data => {
                responseDiv.innerText = data.response;
                speak(data.response);
            });
    };

    recognition.onerror = function () {
        resetMic();
        responseDiv.innerText = "Mic error or permission denied";
    };

    recognition.start();
}



function speak(text) {
    if (!('speechSynthesis' in window)) {
        console.log("Speech synthesis not supported");
        return;
    }

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = 1;
    utterance.pitch = 1;
    utterance.volume = 1;

    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);
}


function stopAll() {
    resetMic();
    document.getElementById("response").innerText = "Cancelled";
}


function resetMic() {
    if (recognition) recognition.stop();
    window.speechSynthesis.cancel();

    isListening = false;
    isSpeaking = false;

    const micBtn = document.getElementById("micBtn");
    const micIcon = document.getElementById("micIcon");

    micBtn.classList.remove("listening");
    micIcon.src = "../Front-End-For-ALL-Projects/img/microphone.png"; 
}
