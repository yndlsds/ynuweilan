//left side accordion
$(function() {
    $('#nav-accordion').dcAccordion({
        eventType: 'click',
        autoClose: true,
        saveState: true,
        disableLink: true,
        speed: 'slow',
        showCount: false,
        autoExpand: true,
        classExpand: 'dcjq-current-parent'
    });
});

var Script = function () {
    //  menu auto scrolling
    jQuery(".leftside-navigation .sub-menu > a").click(function () {
        var o = ($(this).offset());
        diff = 80 - o.top;
        if(diff>0)
            $(".leftside-navigation").scrollTo("-="+Math.abs(diff),500);
        else
            $(".leftside-navigation").scrollTo("+="+Math.abs(diff),500);
    });
 
    $('.sidebar-toggle-box .fa-bars').click(function (e) {
        $(".leftside-navigation").niceScroll({
            cursorcolor:"#1FB5AD",
            cursorborder:"0px solid #fff",
            cursorborderradius:"0px",
            cursorwidth:"3px"
        });

        $('#sidebar').toggleClass('hide-left-bar');
        if($('#sidebar').hasClass('hide-left-bar')){
            $(".leftside-navigation").getNiceScroll().hide();
        }
        $(".leftside-navigation").getNiceScroll().show();
        $('#main-content').toggleClass('merge-left');
        e.stopPropagation();
        if( $('#container').hasClass('open-right-panel')){
            $('#container').removeClass('open-right-panel')
        }
        if( $('.right-sidebar').hasClass('open-right-bar')){
            $('.right-sidebar').removeClass('open-right-bar')
        }

        if( $('.header').hasClass('merge-header')){
            $('.header').removeClass('merge-header')
        }
    });
    $('.toggle-right-box .fa-bars').click(function (e) {
        $('#container').toggleClass('open-right-panel');
        $('.right-sidebar').toggleClass('open-right-bar');
        $('.header').toggleClass('merge-header');

        e.stopPropagation();
    });

    $('.header,#main-content,#sidebar').click(function () {
       if( $('#container').hasClass('open-right-panel')){
           $('#container').removeClass('open-right-panel')
       }
        if( $('.right-sidebar').hasClass('open-right-bar')){
            $('.right-sidebar').removeClass('open-right-bar')
        }

        if( $('.header').hasClass('merge-header')){
            $('.header').removeClass('merge-header')
        }
    });

    /*Slim Scroll*/
    $(function () {
        $('.event-list').slimscroll({
            height: '305px',
            wheelStep: 20
        });
        $('.conversation-list').slimscroll({
            height: '360px',
            wheelStep: 35
        });
        $('.to-do-list').slimscroll({
            height: '300px',
            wheelStep: 35
        });
        $(".leftside-navigation").niceScroll({
            cursorcolor:"#1FB5AD",
            cursorborder:"0px solid #fff",
            cursorborderradius:"0px",
            cursorwidth:"3px"
        });

        $(".leftside-navigation").getNiceScroll().resize();
        if($('#sidebar').hasClass('hide-left-bar')){
            $(".leftside-navigation").getNiceScroll().hide();
        }
        $(".leftside-navigation").getNiceScroll().show();

        $(".right-stat-bar").niceScroll({
            cursorcolor:"#1FB5AD",
            cursorborder:"0px solid #fff",
            cursorborderradius:"0px",
            cursorwidth:"3px"
        });
    });

    // tool tips
    $('.tooltips').tooltip();

    // popovers
    $('.popovers').popover();   

    /*==Collapsible==*/
    $(function() {
        $('.widget-head').click(function(e)
        {
            var widgetElem = $(this).children('.widget-collapse').children('i');

            $(this)
                .next('.widget-container')
                .slideToggle('slow');
            if ($(widgetElem).hasClass('ico-minus')) {
                $(widgetElem).removeClass('ico-minus');
                $(widgetElem).addClass('ico-plus');
            }
            else
            {
                $(widgetElem).removeClass('ico-plus');
                $(widgetElem).addClass('ico-minus');
            }
            e.preventDefault();
        });
    });
}();