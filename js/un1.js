
                 function highlight(mynumber,text, from, to) {
                     const replacement = `<span s="${mynumber}" style="background-color: grey;">${text.slice(from, to)}</span>`;
                         //console.log(JSON.stringify(text.substring(0, from)));
                         //console.log(text.substring(0, to));
                         //return '<span s="'+String(mynumber)+'">'+(text.substring(0, from)).replaceAll("\n",'</span><span s="'+String(mynumber)+'">') + replacement +""+ (text.substring(to)).replaceAll("\n",'</span><span s="'+String(mynumber)+'">')+"</span>";
                         return '<span s="'+String(mynumber)+'">'+(text.substring(0, from)).replaceAll("\n",'</span><span s="'+String(mynumber)+'">')+"</span>" + replacement + '<span s="'+String(mynumber)+'">' +""+ (text.substring(to)).replaceAll("\n",'</span><span s="'+String(mynumber)+'">')+"</span>";
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
	//console.log(myid);
         const textElement = document.getElementById(myid); // Replace with your actual element ID
         const originalText = textElement.innerText;

         // Create a new SpeechSynthesisUtterance
         const utterance = new SpeechSynthesisUtterance(originalText);

         // Listen for the 'boundary' event to highlight words
         utterance.addEventListener('boundary', event => {
		 //console.log("hey");
             const { charIndex, charLength } = event;
                 textElement.innerHTML = highlight(mynumber,originalText, charIndex, charIndex + charLength);
                 });

                 // Start speaking the text
                 synth.speak(utterance);

                 // Helper function to highlight text

	//return false;
}
