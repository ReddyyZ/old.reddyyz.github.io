const proxyurl = "https://cors-anywhere.herokuapp.com/";

async function getClap(){

    var x = await fetch(proxyurl + 'http://claps-reddyyz.000webhostapp.com/');

    return await x.text();
}

async function clap(article){
    return await fetch('https://claps-reddyyz.000webhostapp.com/like.php?article='+article,{
        mode: 'no-cors'
    });
}