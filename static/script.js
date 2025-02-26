document.addEventListener("DOMContentLoaded", function () {
    const translationForm = document.getElementById("translationForm");
    const outputDiv = document.getElementById("outputDiv");

    translationForm.addEventListener("submit", function (e) {
        e.preventDefault();

        // Get the input sentence
        const sentenceInput = document.getElementById("sentence");
        const sentence = sentenceInput.value;

        // Perform your translation or transformation here
        const transformedSentence = transformSentence(sentence);

        // Display the result
        outputDiv.textContent = transformedSentence;
    });

    // Replace this function with your actual translation logic
    function transformSentence(sentence) {
        // Example transformation: Reverse the sentence
        return sentence.split("").join("");
    }
});
const SpeechRecognition =
 window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = false;

document.querySelector('#mic-icon').addEventListener('click', () => {
 recognition.start();
});

recognition.addEventListener('result', (e) => {
 let transcript = e.results[0][0].transcript;
 console.log(transcript);
});
const textToSpeech = async (text) => {
    const response = await fetch(`https://texttospeech.googleapis.com/v1/text:synthesize?key=YOUR_API_KEY`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        input: {
          text: text,
        },
        voice: {
          languageCode: 'en-US',
          ssmlGender: 'NEUTRAL',
        },
        audioConfig: {
          audioEncoding: 'MP3',
        },
      }),
    });
   
    const data = await response.json();
    const audioData = data.audioContent;
    const audioBlob = new Blob([audioData], { type: 'audio/mp3' });
    const audioUrl = URL.createObjectURL(audioBlob);
    return audioUrl;
   };
   const playAudio = (audioUrl) => {
    const audio = new Audio(audioUrl);
    audio.play();
   };
      



