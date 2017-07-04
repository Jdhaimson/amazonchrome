const millenialTalk = ['umm, yes! 🙌', 'yes, please! 💁', 'Get me this now! 💣', 'preach 🙏', 'so hot 🔥🔥🔥'];
const randMillenial = Math.floor(Math.random() * millenialTalk.length);
const millenialInfo = millenialTalk[randMillenial];

$(function() {
    try {
    $.ajax({
        url: 'https://hidden-peak-93606.herokuapp.com/summer',
        type: 'GET',
        contentType: 'application/json',
        success: function(item) {
            renderView(item);
        },
        error: function(xhr, status, error) {
            console.log(status + '; ' + error);
            s3fallback();
        }
     });

    } catch(e) {
        console.log(e);
        s3fallback();
    }
});

function s3fallback() {
    $.ajax({
        dataType: "json",
        url: "https://s3.us-east-2.amazonaws.com/hipbuy/dress_results.json",
        success: function(data) {
            const pants = data;
            const randPant = Math.floor(Math.random() * pants.length);
            const pantInfo = pants[randPant];
            renderView(pantInfo);
        },
        error: function(xhr, status, error) {
            console.log(status + '; ' + error);
        }
    });
}

function renderView({imgurl, price, name, url}) {
    $(".image img").attr("src", imgurl);
    $(".description .price").text(price);
    $(".description .name").text(name);
    $(".buy-btn a").attr("href", url);
    $(".buy-btn a").text(millenialInfo);
}


// Add google analytics code
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-101972688-1']);
_gaq.push(['_trackPageview']);

(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = 'https://ssl.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();

document.onLoad = function() {
    function trackButton(e) {
        _gaq.push(['_trackEvent', e.target.id, 'clicked']);
    };

    var buttons = document.querySelectorAll('button');
    var button = $("#buy")[0];
    button.addEventListener('click', trackButton);
};
