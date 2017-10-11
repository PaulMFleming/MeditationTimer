var counter =  180;
var prepCounter = 10;
var t;
var isTimerOn = false;

var tone = document.getElementById("bell-one");
var ambient = document.getElementById("no-ambient");
var ambientSampler = document.getElementById("no-ambient");
var image = document.getElementById("noImage");

IMAGES = {
    "yinyang-image": "url(/static/media/images/yin-yang_stones.jpg)",
    "om-image": "url(/static/media/images/on_red_bg.jpg)",
    "buddha-image": "url(/static/media/images/lord-buddha.jpg)",
    "no-image": "url(none)",
}

PREP_TIMER={
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





function setBellOne() {
    tone.pause();
    tone.currentTime = 0;
    tone = document.getElementById("bell-one");
    tone.play();
    return tone
}

function setBellTwo() {
    tone.pause();
    tone.currentTime = 0;
    tone = document.getElementById("bell-two");
    tone.play();
    return tone
}

function setBellThree() {
    tone.pause();
    tone.currentTime = 0;
    tone = document.getElementById("bell-three");
    tone.play();
    return tone
}

function setBellFour() {
    tone.pause();
    tone.currentTime = 0;
    tone = document.getElementById("bell-four");
    tone.play();
    return tone
}

function setAmbientOne(){
    tone.pause();
    tone.currentTime = 0;
    ambientSampler.pause();
    ambientSampler.currentTime = 0;
    ambient = document.getElementById("ambient-one");
    ambientSampler = document.getElementById("ambient-one-sampler");
    ambientSampler.play();
    return ambient;
    return ambientSampler;
}

function setAmbientTwo(){
    tone.pause();
    tone.currentTime = 0;
    ambientSampler.pause();
    ambientSampler.currentTime = 0;
    ambient = document.getElementById("ambient-two");
    ambientSampler = document.getElementById("ambient-two-sampler");
    ambientSampler.play();
    return ambient;
    return ambientSampler;
}

function setAmbientThree(){
    tone.pause();
    tone.currentTime = 0;
    ambientSampler.pause();
    ambientSampler.currentTime = 0;
    ambient = document.getElementById("ambient-three");
    ambientSampler = document.getElementById("ambient-three-sampler");
    ambientSampler.play();
    return ambient;
    return ambientSampler;
}

function setNoAmbient(){
    tone.pause();
    tone.currentTime = 0;
    ambient.pause();
    ambient.currentTime = 0;
    ambient = document.getElementById("no-ambient");
    ambient.play();
    return ambient;
}

function setIntentionOne() {
    document.getElementById("intention").value;
}

function setImage(imageName) {
    $(".modal-content").css('background-image', IMAGES[imageName]);
}

function setTime(timeInSeconds) {
    counter = parseInt(MED_TIMER[timeInSeconds]);
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    console.log(counterDisplay);
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
}

function setPrepTime(prepTimeInSeconds) {
    prepCounter = parseInt(PREP_TIMER[prepTimeInSeconds]);
    prepCounterDisplay = moment.utc(prepCounter*1000).format('mm:ss');
    console.log(prepCounterDisplay);
    document.getElementById("text").value = prepCounterDisplay;
    return prepCounterDisplay;
    return prepCounter;
}

function noImage() {
    $("#no-image")
}