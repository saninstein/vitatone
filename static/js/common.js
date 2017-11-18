$(document).ready(function() {

	//Preloader
	setTimeout(function(){
		$('#preloader').fadeOut('slow',function(){$(this).remove();});
	}, 1000);

	// Img
	$("img, a").on("dragstart", function(event) { event.preventDefault(); });

	// MatchHeight
	$('.advantages-item, .norma-item, .try-more-item, .candy-item, .multivitamins .vitamin-item, .wrap.main-page .top-section .descr-list ul li').matchHeight();

	// Menu Toggle
	$('.main-menu-toggle').click(function() {
		$(this).toggleClass("on");
		$('.main-menu').slideToggle('slow');
	});



	// Menu
	if($(window).width() > 767 ) {
		$('.main-menu ul').superfish({
			cssArrows: false,
			delay: 200
		});
	} else {
		// $('.menu-item-has-children a').click(function() {
		// 	$(this).parent('li').find('ul').slideToggle('slow');
		// 	return false;
		// });
	}

	$(window).resize(function() {
		if( $(window).width() > 767 ) {
			$('.main-menu ul').superfish({
				cssArrows: false,
				delay: 200
			});
		} else {
			$('.main-menu ul').superfish('destroy');

			// $('.menu-item-has-children a').click(function() {
			// 	return false;
			// });

		}
		
	});

	$('.menu-item-has-children span').click(function() {
		if ($(window).width() <= 767) {
			$(this).parent('li').find('ul').slideToggle('slow');
			console.log('click');
			return false;
		}
	});

	$('.footer-menu ul').superfish();

	// Popup
	$('.call-popup').magnificPopup({
		type:"inline",
        mainClass: 'mfp-fade',
        showCloseBtn: true,
        closeBtnInside: true,
        removalDelay: 300,
        callbacks: {open: function() {$('#navbar').css('padding-right', '17px');},close: function() {$('#navbar').css('padding-right', '0px');}}

	});

	// Book Slider
	$('.book-slider').owlCarousel({
		loop: true,
		margin: 0,
		nav: true,
		autoplay: false,
		items: 1,
		navText: ["",""],
		dots: false,
		animateIn: 'fadeIn',
		animateOut: 'fadeOut',
		responsive:{
			0:{
	            nav: false
	        },
	        768:{
	            items: 1
	        }
	    }
	});

	$('.book-slider').on('changed.owl.carousel',function(property){
    	var current = property.item.index;
    	if (current == 4) {
    		$('.masha-logo').fadeIn();
    	} else {
    		$('.masha-logo').fadeOut();
    	}
	});

	// Slider
	$('.advices-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		autoplay: false,
		items: 1,
		navText: ["",""],
		dots: false,
		mouseDrag: false,
		touchDrag: false,
		responsive:{
			0:{
	            nav: false,
	            dots: true
	        },
	        992:{
	            items: 1
	        }
	    }
	});

	$('.candy-slider, .multi-slider, .ukach-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		autoplay: false,
		items: 1,
		navText: ["",""],
		dots: false,
		responsive:{
			0:{
	            //nav: false,
	            //dots: true
	        },
	        768:{
	            
	        }
	    }
	});

	$('.toys-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		autoplay: false,
		items: 4,
		navText: ["",""],
		dots: false,
		responsive:{
			0:{
	            items: 1
	        },
	        480:{
	            items: 2
	        },
	        768:{
	            items: 3
	        },
	        992:{
	            items: 4
	        }
	    }
	});

	
	// Sliding Footer BG
	var bg_pos = 0;
	setInterval(function () {
		$('.sliding-footer, .sliding-header').css('background-position', bg_pos + 'px 0');
		bg_pos = bg_pos - 1
	}, 50);

	// Fade In Animals
	$(window).scroll(function(){

		if ($(window).scrollTop() >= 200) {
	        $('.rabbit').animate({"margin-left": '-765px'}, 1000);
	    }

	    if ($(window).scrollTop() >= 400) {
	        $('.panda').animate({"margin-left": '500px'}, 1000);
	    }

	    if ($(window).scrollTop() >= 700) {
	        $('.dog').animate({"margin-left": '-790px'}, 1000);
	    }

	    if ($(window).scrollTop() >= 1200) {
	        $('.squirrel').fadeIn('slow');
	    }

	});

});

