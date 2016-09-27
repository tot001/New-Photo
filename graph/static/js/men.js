window.onload = function () {
    new TabSwitch('tab');


//home_img
    var home_img = document.createElement('img');
    home_img.src = "../static/images/home_img.jpg";
    $(".home_img").append(home_img);

    if (home_img) {
        $(window).scroll(function () {
            $(window).scrollTop(0);
        })
    }
    $('.home_img').click(function () {
        $(this).fadeOut(500);
        $(window).unbind('scroll');
        setCookie('one', 'display', 1);
    });

    var one = GetCookie('one');
    if (one == "display") {
        $(window).unbind('scroll');
        $('.home_img').remove();
    }


//flatbtn
    $('.flatbtn').click(function () {
       $('#nav').toggle();
    });





    // $('.iload').height($('.iload').width()-10);

//diandian
    var bx_top = ($('.slide').first().height() - 10) + 'px';
    $('.bx-pager').css('top', bx_top);

//zan&cai
    Andstep("#cai", "cai2.png",".cai",'cai');
    Andstep('#zan', "zan2.png",".zan",'zan');


//lean_overlay
    $('.lazy').click(function () {
        var id = $(this).attr("id");
        $('#lean_overlay').css('display','table');
        var img = $('#' + id)[0].src;
        $("#car_img").attr('src', img);
    });

    $('#lean_overlay').click(function () {
        $(this).toggle();
    });


//lazy
    $(function () {
        $("img.lazy").lazyload({
            event: "scrollstop",
            effect: "fadeIn",
            skip_invisible: true,
        });
    });

//list grid
    (function () {
         // function animate(item, x, y, index) {
         //     dynamics.animate(item, {
         //         translateX: x,
         //         translateY: y,
         //         opacity: 1
         //     }, {
         //         type: dynamics.spring,
         //         duration: 800,
         //         frequency: 150,
         //         delay: 100
         //     });
         // }


         window.addEventListener('resize', function () {
             minigrid('.grid', '.grid-item',6);
         });
     })();


//totop
    $(this).scroll(function () {
        if ($(this).scrollTop() > 80) {
            $('.gtop').animate({opacity: 0.5}, 0);
        }
        else {
            $('.gtop').animate({opacity: 0}, 0);
        }
    });

    $('.gtop').bind({
        click: function () {
            $(this).animate({'scrollTop': 0}, 100);
        }
    });






//ajax
    var page=1;
    var listY=0,Y=0,EY=0;

    $(".widget-photos").delegate("ul.list","touchstart",
        function (event) {
            listY=event.touches[0].clientY;
            console.log(listY)
        });

    $(".widget-photos").delegate("ul.list","touchmove",
        function (event) {
            var Y=event.touches[0].clientY-listY;
             EY=parseInt(String(Y).match(/\d+/g));
            console.log(EY);
            return EY;
        });

    $(".widget-photos").delegate("ul.list","touchend",
        function () {
            console.log("nnn"+EY);
            page+=1;
            if (EY<=20){
                $('.lazy').click(function () {
                    var id = $(this).attr("id");
                    $('#lean_overlay').css('display','table');
                    var img = $('#' + id)[0].src;
                    $("#car_img").attr('src', img);
                });
            }else{
                $.ajax({
                    type:"GET",
                    url:"/ajaxindex/?page="+page,
                    dataType:"html",
                    timeout: 2000,
                    cache:false,
                    success:function (data) {
                        var list_= $('.list').html();
                        $('.list').html(list_+data);
                        minigrid('.grid', '.grid-item',6);
                    },
                    error:function () {
                        $('.bot').show(function () {
                            $(this).html("以到底！")
                        });
                    }
                });
            }
        });


    $('.tca').one('click',function () {
        $.ajax({
            type: "GET",
            url: "/ajaxindex/?page=1" ,
            dataType: "html",
            timeout: 2000,
            cache: false,
            success:function (data) {
                $('.list').html(data);
                minigrid('.grid', '.grid-item',6);
                $(function () {
                    $("img.lazy").lazyload({
                        event: "scrollstop",
                        effect: "fadeIn",
                        skip_invisible: true
                    });
                });
            }
        })
    })



};




//xuanxiang
function TabSwitch(id) {
    var _this = this;
    var oDiv = document.getElementById(id);
    this.aBtn = oDiv.getElementsByTagName('ol');
    this.aDiv = oDiv.getElementsByTagName('div');

    for (var i = 0; i < this.aBtn.length; i++) {
        this.aBtn[i].index = i;
        this.aBtn[i].onclick = function () {
            _this.fnBtn(this);
        }
    }
}
TabSwitch.prototype.fnBtn = function (oBtn) {
    for (var i = 0; i < this.aBtn.length; i++) {
        this.aBtn[i].className = 'tab-hd-con';
        this.aDiv[i].style.display = "none";
    }
    $(oBtn).addClass("tab-active");
    this.aDiv[oBtn.index].style.display = 'block';
};

//Cookie
function setCookie(name, value, daysToLive) {
    var oDate = new Date();
    var cookie = name + "=" + encodeURIComponent(value);
    if (typeof daysToLive === "number")
        cookie += "; max-age=" + (daysToLive * 60 * 60 * 24);
    document.cookie = cookie;
}

function GetCookie(c_name) {
    var all = document.cookie;
    if (all.length > 0) {
        c_start = all.indexOf(c_name + '=');
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

//Andstep
function Andstep(Aid,url,Classname,zc) {
    var Ocai = document.getElementsByClassName(Aid);
    for (var i = 1; i <= Ocai.length; i++) {
        $(Aid + [i]).click(function () {
            var tt = parseInt($(this).next().html());
            $(this).next().html(tt + 1);
            $(this).css('background', function () {
                return "url(../static/images/" + url + ")" + "center no-repeat";
            });
            $(this).unbind('click');
        });
    }
    $(Classname).click(function () {
        var id = $(this).attr('id');
        var tt = $('#' + id).next().html();
        var str=id.match(/\d+/g);
        $.get("/"+zc+"/?id=" + str + "&count="+tt+"")
    })
}





