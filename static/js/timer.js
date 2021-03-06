//
// Custom script to control the Meditation Timer and 
// it's various components
//

// set variables
var counter =  180;
var prepCounter = 10;
var t;
var isTimerOn = false;

var tone = document.getElementById("bell-one");
var ambient = document.getElementById("no-ambient");
var ambientSampler = document.getElementById("no-ambient");
var image = document.getElementById("noImage");


IMAGES = {
    "yinyang-image": "url(https://imom-assets.s3.amazonaws.com/static/media/images/yin-yang_stones.jpg)",
    "om-image": "url(https://imom-assets.s3.amazonaws.com/static/media/images/on_red_bg.jpg)",
    "buddha-image": "url(https://imom-assets.s3.amazonaws.com/static/media/images/lord-buddha.jpg)",
    "no-image": "url(none)",
}

PREP_TIMER = {
    "tenSec": "10",
    "thirtySec": "30",
    "sixtySec": "60",
}
MED_TIMER = {
    "threeMin": "180",
    "fiveMin": "300",
    "sevenMin": "420",
    "tenMin": "600",
    "thirteenMin": "720",
    "fifteenMin": "900",
}

BELLS = {
    "bellOne": "bell-one",
    "bellTwo": "bell-two",
    "bellThree": "bell-three",
    "bellFour": "bell-four",
}

AMBIENT = {
    "ambientOne": "ambient-one",
    "ambientTwo": "ambient-two",
    "ambientThree": "ambient-three",
    "noAmbient": "no-ambient",
}

AMBIENT_SAMPLER = {
    "ambientOne": "ambient-one-sampler",
    "ambientTwo": "ambient-two-sampler",
    "ambientThree": "ambient-three-sampler",
    "noAmbient": "no-ambient",
}

// functions to control the timer itself
function prepCountdown() {
    document.getElementById("text").value = moment.utc(prepCounter*1000).format('mm:ss');
    prepCounter--;
    t = setTimeout("prepCountdown();", 1000);

    if (prepCounter < 0) {
        isTimerOn = false;
        stopMe();
        startMe();
    }
}

function startMe() {
    tone.pause();
    tone.currentTime = 0;
    if (!isTimerOn) {
      isTimerOn = true;
      tone.play();
      ambient.play();
      countdown();
    }
}

function countdown() {
    document.getElementById("text").value = moment.utc(counter*1000).format('mm:ss');
    console.log(counter);
    counter--;
    t = setTimeout("countdown();", 1000);

    if (counter < 0) {
      stopMe();
      tone.play();
      showDiaryEntryButton();
    }
}

function stopMe() {
    ambient.pause();
    isTimerOn = false;
    clearTimeout(t);
}

function resetMe() {
    ambient.pause();
    ambient.currentTime = 0;
    isTimerOn = false;
    clearTimeout(t);
    counter = 0;
    document.getElementById("text").value = moment.utc(counter*1000).format('mm:ss');
}

function playTone() {
    tone.play();
}

// Time control functions for the timer
function setPrepTime(prepTimeInSeconds) {
    prepCounter = parseInt(PREP_TIMER[prepTimeInSeconds]);
    prepCounterDisplay = moment.utc(prepCounter*1000).format('mm:ss');
    console.log(prepCounterDisplay);
    document.getElementById("text").value = prepCounterDisplay;
    return prepCounterDisplay;
}

function setTime(timeInSeconds) {
    counter = parseInt(MED_TIMER[timeInSeconds]);
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    console.log(counterDisplay);
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
}

// Audio element control functions for the timer
function setBell(bellSound) {
    tone.pause();
    tone.currentTime = 0;
    tone = document.getElementById(BELLS[bellSound]);
    playTone();
    return tone;
}

function setAmbient(ambientSound) {
    tone.pause();
    tone.currentTime = 0;
    ambientSampler.pause();
    ambientSampler.currentTime = 0;
    ambient = document.getElementById(AMBIENT[ambientSound]);
    ambientSampler = document.getElementById(AMBIENT_SAMPLER[ambientSound]);
    ambientSampler.play();
    return ambient;
}

// functions that control setting the backgrounds in the timer
function setImage(imageName) {
    $(".modal-content").css('background-image', IMAGES[imageName]);
} 

$('.user-uploaded-image').click(function(){
    var src = $(this).attr('src');
    $('.modal-content').css('background-image', 'url('+src+')');
    
    })

    // function to toggle visibility of the write in your diary button
function showDiaryEntryButton() {
    $(".hide-buttons").removeClass('hidden');
}

