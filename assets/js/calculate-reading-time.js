function ReadingTime(words_per_minute){
    const ps = document.querySelectorAll("p");
    console.log(ps);

    var count = 0;

    for (var i =0; i < ps.length; i++){
        count += ps[i].innerHTML.split(" ").length;
    }

    x = count / words_per_minute;
    x = String(x).split('.');
    
    minutes = x[0];
    y = x[1];
    y = parseInt(y);
    y = y * 0.60;
    y = Math.round(y);
    y < 30 ? y = 0 : y = 1
    minutes = parseInt(minutes) + y;

    console.log("Reading time:", minutes, minutes == 1 ? "minute" : "minutes");
}