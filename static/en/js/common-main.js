$(document).ajaxStart(function() { $('body').addClass("loading");    });
$(document).ajaxComplete(function() { $('body').removeClass("loading");    });

$(".anchor").click(function () {
	var isSafari = /safari/.test(navigator.userAgent.toLowerCase());
	var elementClick = $(this).attr("href");
	var destination = $(elementClick).offset().top;
	if (isSafari) {
 		$('body').animate({ scrollTop: destination }, 600);
	} 
    else {
     	$('html').animate({ scrollTop: destination }, 600);
    }
    return false; 
});
var repeatClick = true,
	flag = true,
	init = false,
	blockSlider = $('#products-slider'),
	imgParallax = $('#scene-wrapper'),
	imgOverlay = $('#bg-overlay'),
	counter,
	slider = '#my-carousel',
	slideItem = slider + ' .carousel-inner .item',
	textContent = $('.main-info');


// interacting of aside


$('.choose-category').on('click', function(){
	var $this = $(this),
		category = $this.data('target'),
		currentLi = $this.parent(),
		indexOfLi = $this.parent().index(),
		urlToJson = 'js/list.json?v=2',
		listIndicators = $(slider + ' .carousel-indicators'),
		listSlides = $(slider + ' .carousel-inner'),
		arrIndicators = [],
		newSlidesCount = 0,
		arrSlides = [];
	// for mobile version
	$('.aside-wrapper').removeClass('active');
	if (repeatClick !== indexOfLi || init === true) {
		flag = true;
		init = false;
		repeatClick = indexOfLi;
		imgParallax.addClass('opacity');
		imgOverlay.addClass('active');
		if (blockSlider.is(':visible'))	blockSlider.hide();
		$('#categories').find('li.active').removeClass('active');
		currentLi.toggleClass('active');
		// ajax requests
		$.ajax({
			url: urlToJson,
			dataType: 'json',
			type: 'GET',
			cache: false,
			success: function(data) {
				$.each(data, function(id, value){
					counter = value.length;
					for (var i = 1; i < counter; i++){
						$(slideItem + ':nth-of-type('+ (i+1) + ')').remove();
						$('.carousel-indicators li:nth-child(' + (i+1) + ')').remove();
					}
					if (id == category) {
						for (var i = 0; i < counter; i++){
							var child = $(slideItem).first();
							if (i === 0) {
								$(slideItem).removeClass('active');
								$(slideItem).first().addClass('active');
								if ($("#ie").hasClass("ie9"))
									$(slideItem).first().css('left', '0');
								$('.carousel-indicators li').removeClass('active');	
								$('.carousel-indicators li').first().addClass('active');
								child.find('a').attr('href', value[i].url);
								child.find('a img').removeAttr().attr('src', value[i].src);
								child.find('a img').attr('alt', value[i].name);
								child.find('.carousel-caption').empty().append(value[i].caption);	
							} 
							else {
								newSlidesCount++;
								arrIndicators.push('<li data-target="#my-carousel" data-slide-to="' + i + '"></li>');
								arrSlides.push('<div class="item"><a href="' + value[i].url + '"><img src="' + value[i].src + '" alt="' + value[i].name + '"></a><div class="carousel-caption">' + value[i].caption + '</div></div>');
							}
						} // for
					} // if
				}); // $.each
				for (var i = 0; i < newSlidesCount; i++){
					listIndicators.append(arrIndicators[i]);
					listSlides.append(arrSlides[i]);
				}
			}, // success
			complete: function() {
				textContent.hide();
				blockSlider.fadeIn('slow');
				var isSafari = /safari/.test(navigator.userAgent.toLowerCase());
				var elementClick = $('.choose-category').attr("href");
				var destination = $(elementClick).offset().top;
				if (isSafari) {
			 	 $('body').animate({ scrollTop: destination }, 600);
					   } 
			    else {
			     	$('html').animate({ scrollTop: destination }, 600);
			    }
			}
		}); // ajax
	} // main if
	else if (flag) {
		blockSlider.hide();
		textContent.fadeIn();
		for (var i = 1; i < counter; i++){
			$(slideItem + ':nth-child('+ (i+1) + ')').remove();
			$('.carousel-indicators li:nth-child(' + (i+1) + ')').remove();
		}
		flag = false;
		init = true;
		imgParallax.removeClass('opacity');
		imgOverlay.removeClass('active');
		currentLi.removeClass('active');
		currentLi = true;
	}
	return false;
});

$("#backup").on('click', function(){
	blockSlider.hide();
	textContent.fadeIn('slow');
	for (var i = 1; i < counter; i++){
		$(slideItem + ':nth-child('+ (i+1) + ')').remove();
		$('.carousel-indicators li:nth-child(' + (i+1) + ')').remove();
	}
	imgOverlay.removeClass('active');
	imgParallax.removeClass('opacity');
	$('#categories li').removeClass('active');
});

$('#show-button').on('click', function(){
	$('.aside-wrapper').toggleClass('active');
});
$('.hide-button').on('click', function(){
	$(this).parent().removeClass('active');
	if ($(this).parent().parent().find('.nav-toggle').hasClass('open'))
		$('.nav-toggle').removeClass('open');
});
$('.nav-toggle').on('click', function(){
	$(this).toggleClass('open');
	$('#nav').toggleClass('active');
});
$('.mobile-hide').on('click', function(){
	// for mobile version
	$('#nav').removeClass('active');
	$('.nav-toggle').removeClass('open');
});
