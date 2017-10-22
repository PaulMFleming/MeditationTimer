var qoutes = [
    
    '<p>“Those who know do not speak. Those who speak do not know.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“When you are content to be simply yourself and don\'t compare or compete, everyone will respect you.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“When you are content to be simply yourself and don\'t compare or compete, everyone will respect you.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“The truth is not always beautiful, nor beautiful words the truth.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“A man with outward courage dares to die; a man with inner courage dares to live.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“Do you have the patience to wait until your mud settles and the water is clear?” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“If you understand others you are smart. \
    If you understand yourself you are illuminated. \
    If you overcome others you are powerful. \
    If you overcome yourself you have strength. \
    If you know how to be satisfied you are rich. \
    If you can act with vigor, you have a will. \
    If you don\'t lose your objectives you can be long-lasting. \
    If you die without loss, you are eternal.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“The flame that burns Twice as bright burns half as long.” \
    <br>― Lao Tzu, Te Tao Ching</p>',
    '<p>“A leader is best\
    When people barely know he exists\
    Of a good leader, who talks little,\
    When his work is done, his aim fulfilled,\
    They will say, “We did this ourselves.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“If you try to change it, you will ruin it. Try to hold it, and you will lose it.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“The wise man is one who, knows, what he does not know.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“To understand the limitation of things, desire them.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“Give evil nothing to oppose \
    and it will disappear by itself."\
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“If you realize that all things change, there is nothing you will try to hold on to. If you are not afraid of dying, there is nothing you cannot achieve.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“The further one goes, the less one knows.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“He who conquers others is strong; he who conquers himself is mighty" \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“When people see some things as beautiful,\
    other things become ugly.\
    When people see some things as good,\
    other things become bad.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“When there is no desire,\
    all things are at peace.” \
    <br>― Lao Tzu, Tao Te Ching</p>',
    '<p>“Knowing others is intelligence; \
    knowing yourself is true wisdom. \
    Mastering others is strength; \
    mastering yourself is true power.”  \
    <br>― Lao Tzu, Tao Te Ching</p>',
]

document.addEventListener("DOMContentLoaded", function() {
    newQuote();
  });

function newQuote() {
    var randonNumber = Math.floor(Math.random() * (qoutes.length));
    console.log(randonNumber);
    document.getElementById('quoteDisplay').innerHTML = qoutes[randonNumber];    
}
