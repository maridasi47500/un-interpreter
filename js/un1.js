
                 function highlight(text, from, to) {
                     const replacement = `</span><span s="${mynumber}" style="background-color: grey;">${text.slice(from, to)}`;
                         return '<span s="'+String(mynumber)+'">'+text.substring(0, from).replace(" ",'</span><span s="'+String(mynumber)+'">') + replacement + text.substring(to)+"</span>";
                         }
 const synth = window.speechSynthesis;

function myhighlight(mynumber) {

 if (!synth) {
     console.error('Text-to-speech not supported in this browser.');
         return false;
         }

         // Get the text element you want to highlight
         var myid;
         var ok;
	 myid="mysentence"+String(mynumber);
	console.log(myid);
         const textElement = document.getElementById(myid); // Replace with your actual element ID
         const originalText = textElement.innerText;

         // Create a new SpeechSynthesisUtterance
         const utterance = new SpeechSynthesisUtterance(originalText);

         // Listen for the 'boundary' event to highlight words
         utterance.addEventListener('boundary', event => {
		 console.log("hey");
             const { charIndex, charLength } = event;
                 textElement.innerHTML = highlight(originalText, charIndex, charIndex + charLength);
                 });

                 // Start speaking the text
                 synth.speak(utterance);

                 // Helper function to highlight text

	return false;
}
