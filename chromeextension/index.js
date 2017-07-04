const millenialTalk = ['umm, yes! 🙌', 'yes, please! 💁', 'Get me this now! 💣', 'preach 🙏', 'so hot 🔥🔥🔥'];
const randMillenial = Math.floor(Math.random() * millenialTalk.length);
const millenialInfo = millenialTalk[randMillenial];

$.ajax({
    dataType: "json",
    url: "https://s3.us-east-2.amazonaws.com/hipbuy/dress_results.json",
    success: function(data) {
        const pants = data;
        const randPant = Math.floor(Math.random() * pants.length);
        const pantInfo = pants[randPant];

        $(function() {
            $(".image img").attr("src", pantInfo.imgurl);
            $(".description .price").text(pantInfo.price);
            $(".description .name").text(pantInfo.name);
            $(".buy-btn a").attr("href", pantInfo.url);
            $(".buy-btn a").text(millenialInfo);
        });
    },
    error: function(xhr, status, error) {
        console.log(status + '; ' + error);
    }
});


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
