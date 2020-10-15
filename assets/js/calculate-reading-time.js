function ReadingTime(words_per_minute){
    const ps = document.querySelectorAll("p");
    const pres = document.querySelectorAll("pre");

    var count_p = 0;
    var count_pre = 0;

    for (var i =0; i < ps.length; i++){
        count_p += ps[i].innerHTML.split(" ").length;
    }
    for (var i =0; i < pres.length; i++){
        count_pre += pres[i].innerHTML.split(" ").length;
    }

    p_minutes = make_count(count_p,words_per_minute);
    pre_minutes = make_count(count_pre,words_per_minute);

    minutes = p_minutes + pre_minutes;

    console.log("Reading time:", minutes, minutes == 1 ? "minute" : "minutes");
    return minutes;
}

function make_count(count,words_per_minute){
    x = count / words_per_minute;
    x = String(x).split('.');
    
    minutes = x[0];
    y = x[1];
    y = parseInt(y);
    y = y * 0.60;
    y = Math.round(y);
    y < 30 ? y = 0 : y = 1
    minutes = parseInt(minutes) + y;
    return minutes;
}