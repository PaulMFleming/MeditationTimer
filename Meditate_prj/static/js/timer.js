var counter =  moment.utc(180*1000).format('mm:ss');
var t;
var isTimerOn = false;

var tone = document.getElementById("bell-one");;


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

function startMe() {
    tone.pause();
    tone.currentTime = 0;
    if (!isTimerOn) {
      isTimerOn = true;
      tone.play();
      countdown();
    }
}

function stopMe() {
    isTimerOn = false;
    clearTimeout(t);
}

function resetMe() {
    isTimerOn = false;
    clearTimeout(t);
    counter = 0;
    document.getElementById("text").value = counter;
}

function setThreeMin() {
    counter = 180;
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
}

function setFiveMin() {
    counter = 300;
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
}

function setSevenMin() {
    counter = 420;
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
}

function setTenMin() {
    counter = 600;
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
}

function setThirteenMin() {
    counter = 780;
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
}

function setFifteenMin() {
    counter = 900;
    counterDisplay = moment.utc(counter*1000).format('mm:ss');
    document.getElementById("text").value = counterDisplay;
    return counterDisplay;
    return counter;
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
