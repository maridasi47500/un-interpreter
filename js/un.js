function getDayName(date) {
	return date.toLocaleString(undefined, {weekday:'long'});
}

function getMonthName(date) {
	return date.toLocaleString(undefined, {month:'long'});
}


$(function(){
	if($(".audio_language_list [name='language']").length > 0){
	$(".audio_language_list [name='language']").change(function(){
		$.ajax({url:("/getenregistrement/"+$(".audio_language_list")[0].dataset.someeventid+"?l="+$(this).val().replace(".mp3","")),

		success:function(data){
			console.log(data);
			var speakers=data.speakers;
			var hey = $('.speaker-list');
			var myspeaker;
			for (var i = 0;i<speakers.length;i++){
			    myspeaker=speakers[i];
			    hey.append(`<tr class="speaker" id="position-0" data-position="0"><td lang="en">Start recording</td><td class="speaker-actions"><ul class="list-inline"><li aria-live=""><button data-eventid="${myspeaker["event_id"]}" class="jumptotime player-control btn btn-link" title="Play at this point in the recording"><span class="play" data-label="Play at this point in the recording"><i class="fa fa-play-circle-o fa-lg">&nbsp;</i><span class="sr-only">Play at this point in the recording</span></span><span class="pause" data-label="Pause" style="display: none;"><i class="fa fa-pause-circle-o fa-lg">&nbsp;</i><span class="sr-only">Pause</span></span></button></li>   <li><a class="share-link modalbox btn btn-link" role="button" title="Share a link to this point in the recording" href="./?guid=public/61.0060/C863C522-8B84-4FFC-A5C2-CE2A4EFFEBBB_15h02&amp;position=0&amp;channel=FRENCH" data-target="#linkto-0"><i class="fa fa-link fa-lg">&nbsp;</i><span class="sr-only">Share a link to this point in the recording</span></a>   <div class="linktoseconds" id="linkto-0" style="display: none;"><p>Copy the following link to have a direct access to this point in the recording:</p><label for="directLink-0">Direct link</label><br><textarea id="directLink-0" class="direct-link">https://conf.unog.ch/digitalrecordings/index.html?guid=public/61.0060/C863C522-8B84-4FFC-A5C2-CE2A4EFFEBBB_15h02&amp;position=0&amp;channel=ORIGINAL</textarea>   </div></li>   <li><button class="download_chunk btn btn-link" title="Download this speech" data-chunk-download-link="/dr/public/61.0060/C863C522-8B84-4FFC-A5C2-CE2A4EFFEBBB_15h02/chunks/snippet_lCURLANGs0-00t0-17.mp3" href="/dr/public/61.0060/C863C522-8B84-4FFC-A5C2-CE2A4EFFEBBB_15h02/chunks/snippet_lCURLANGs0-00t0-17.mp3"><i class="fa fa-download fa-lg">&nbsp;</i><span class="sr-only">Download this speech</span></button></li></ul></td><td> `);
			}
			
		}});
	});

	}
	if($("[id=language1]").length > 0 && window.location.search.includes("?l=")){
		$("[id=language1]").val(window.location.search.split("?l=")[1]);
	}
const playIconContainer = $('.play-icon');
let state = 'play',playicon="&#9658;",pauseicon="&#x23f8;";
playIconContainer.html(playicon);
playIconContainer.click(function(){
	var someaudio=$($(this)[0].parentElement).children("audio")[0];
	  if(state === 'play') {
		  someaudio.play();
		      state = 'pause';
		  $(this).html(pauseicon);
		    } else {
		  someaudio.pause();
			        state = 'play';
		  $(this).html(playicon);

			      }
$(".jumptotime .play").show();
$(".jumptotime .pause").hide();
});
const audio = $('audio');
$(".jumptotime .play").show();
$(".jumptotime .pause").hide();

	audio.on('loadedmetadata', function() {
var calculateTime = (secs)=> {
  const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
      const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
        }
		//display audio duration
          var durationContainer = $($(this)[0].parentElement).children('.duration')[0];
          durationContainer.textContent = calculateTime($(this)[0].duration);
		//seek slider max
          var seekSlider = $($(this)[0].parentElement).children('.seek-slider')[0];
		seekSlider.max=Math.floor($(this)[0].duration);
	});
var allSeekSlider=$(".seek-slider");
var calculateTime = (secs)=> {
  const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
      const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
        }
allSeekSlider.on('input', function() {
var calculateTime = (secs)=> {
  const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
      const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
        }
          var currentTimeContainer = $($(this)[0].parentElement).children('.current-time')[0];
	  currentTimeContainer.textContent = calculateTime($(this)[0].value);
          var tempsrestantContainer = $($(this)[0].parentElement).children('.temps-restant')[0];
	  tempsrestantContainer.textContent = calculateTime($(this)[0].max - $(this)[0].value);
	 
});
allSeekSlider.on('change', function() {
var calculateTime = (secs)=> {
  const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
      const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
        }
          var myaudio= $($(this)[0].parentElement).children('audio')[0];
          var currentTimeContainer = $($(this)[0].parentElement).children('.current-time')[0];
          var tempsrestantContainer = $($(this)[0].parentElement).children('.temps-restant')[0];
	  myaudio.currentTime=$(this)[0].value;
	  currentTimeContainer.textContent = calculateTime($(this)[0].value);
	  tempsrestantContainer.textContent = calculateTime($(this)[0].max - $(this)[0].value);

	if (!myaudio.paused){
		 $(this)[0].value = Math.floor(myaudio.currentTime);
		  currentTimeContainer.textContent = calculateTime($(this)[0].value);
		  myaudio.style.setProperty('--seek-before-width', `${$(this)[0].value / $(this)[0].max * 100}%`);


	}
});
audio.on('timeupdate', function() {
var calculateTime = (secs)=> {
  const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
      const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
        return `${minutes}:${returnedSeconds}`;
        }
          var seekSlider = $($(this)[0].parentElement).children('.seek-slider')[0];
	  seekSlider.value = Math.floor($(this)[0].currentTime);
          var currentTimeContainer = $($(this)[0].parentElement).children('.current-time')[0];
          var tempsrestantContainer = $($(this)[0].parentElement).children('.temps-restant')[0];
	  currentTimeContainer.textContent = calculateTime($(this)[0].currentTime);
	  tempsrestantContainer.textContent = calculateTime(seekSlider.max - $(this)[0].currentTime);
});
const volumeSlider = $('.volume-slider');


volumeSlider.on('input', function() {
	  var value = $(this)[0].value;
var outputContainer = $($(this)[0].parentElement).children('.volume-output')[0];

	  outputContainer.textContent = value;
          var myaudio= $($(this)[0].parentElement).children('audio')[0];
	  myaudio.volume = value / 100;
});
audio.each(function(){
	$(this)[0].load();

});
$(".jumptotime").click(function(){

	var time=$(this)[0].parentElement.parentElement.parentElement.parentElement.children[3].innerHTML.replaceAll("\n\t","").replaceAll("\t","").replaceAll("\n","").replaceAll(" ","").split(":");
	var seconds=Number(time[0])*3600+Number(time[1])*60+Number(time[0]);
	var someaudio=$("audio[data-eventid="+$(this)[0].dataset.eventid+"]")[0];




	//if (state === "play"){

if(state === "pause" && $(this).children(".play")[0].style.display === "none"){
		  someaudio.pause();
			        state = 'play';
		                  $(playIconContainer).html(playicon);
$(".jumptotime .play").show();
$(".jumptotime .pause").hide();
}else if ($(".jumptotime .pause[style*=\"display:block\"]").length > 0){
	someaudio.currentTime=seconds;
		                  someaudio.play();
		                      state = 'pause';
		                  $(playIconContainer).html(pauseicon);
$(".jumptotime .play").show();
$(".jumptotime .pause").hide();

$(this).children(".play").hide();
$(this).children(".pause").show();
} else {
	someaudio.currentTime=seconds;
	

		                  someaudio.play();
		                      state = 'pause';
		                  $(playIconContainer).html(pauseicon);
$(".jumptotime .play").show();
$(".jumptotime .pause").hide();

$(this).children(".play").hide();
$(this).children(".pause").show();
}
	
});

//#const displayAudioDuration = () => {
//          var durationContainer = $(this).children('.duration');
//          durationContainer.textContent = calculateTime(audio.duration);
//          }


// Create a date
 var d = new Date();
	var today=d;
 // Set to first of month
 d.setDate(1);
 // Create string
 console.log(`The first of ${getMonthName(d)} was a ${getDayName(d)}.`);
	$("#date_range_preselect").val("this_month");
		var todaystr=today.toISOString().split("T")[0]
		var dstr=d.toISOString().split("T")[0]

	$("#date_from").val(d);
	$("#date_to").val(todaystr);
	$("#date_from").change(function(){
	$("#date_range_preselect").val("custom");
	});
	$("#date_to").change(function(){
	$("#date_range_preselect").val("custom");
	});
	$("#date_range_preselect").change(function(){
 var d = new Date();
	var today=d;
 // Set to first of month
 d.setDate(1);
	var yesterday = today;

	//
	yesterday.setDate(yesterday.getDate() - 1);
                var my_date_from=Date.parse(Date.parse(date_from.value)).toDateString();
                var my_date_to=Date.parse(Date.parse(date_to.value)).toDateString();
		var todaystr=today.toISOString().split("T")[0]
		var yesterdaystr=yesterday.toISOString().split("T")[0]
		if (my_date_from === "today"){
		date_from.value=todaystr;
		date_to.value=todaystr;
	}else if (my_date_from === "today"){
		date_from.value=yesterdaystr;
		date_to.value=yesterdaystr;

		}
	});




});
