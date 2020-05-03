

//---------------------
// WINDOW LOAD FUCNTION
//---------------------

jQuery(window).load(function() {

	prettyPhoto();

	initIsotopeGrid();
	
	preload();

});	


//-----------------------
// WINDOW RESIZE FUCNTION
//-----------------------

function resizeend() {

	if (new Date() - rtime < delta) {

		setTimeout(resizeend, delta);

	} else {

		timeout = false;

		initIsotopeGrid();

		colEqheight();

	} 

}


//----------------------
// WINDOW READY FUCNTION
//----------------------

$(document).ready(function() {
	
	
	// Init Fuctions
	
	owlSlider();
	
	progressBar();
	
	bgImage();
	
	parallaxBg();
	
	fullscreen();
	

	
	colEqheight();
	

	
	dataAnimations();
	
	
		
	// Counter
	$(".count-number").appear(function(){
		$('.count-number').each(function(){
			datacount = $(this).attr('data-count');
			$(this).find('.counter').delay(6000).countTo({
				from: 10,
				to: datacount,
				speed: 3000,
				refreshInterval: 50,
			});
		});
	});
	
	

    $('.smoth-scroll').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });
	
	
	
	// Scroll top top
	var offset = 300,
		offset_opacity = 1200,
		scroll_top_duration = 700,
		$back_to_top = $('.cd-top');

	$(window).scroll(function(){
		( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
		if( $(this).scrollTop() > offset_opacity ) { 
			$back_to_top.addClass('cd-fade-out');
		}
	});

	$back_to_top.on('click', function(event){
		event.preventDefault();
		$('body,html').animate({
			scrollTop: 0 ,
		 	}, scroll_top_duration
		);
	});
var fancyboxIframe = jQuery('.fancybox-iframe');
		if(fancyboxIframe.length) {
		fancyboxIframe.fancybox({
			type: "iframe",
			// other API options
		});
     }
	// Tooltip
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	})
	
	// Popover
	$(function () {
	  $('[data-toggle="popover"]').popover()
	})
		
	// Form Focus 
	$("input").focus(function(){
	
		$(this).parent().addClass("input-focus");
	
	}).blur(function(){
		
		$(this).parent().removeClass("input-focus");
	})
	

});



// Pre Loader
function preload(){
	$(".loader-inner").delay(100).fadeOut();
	$("#pageloader").delay(100).fadeOut("slow")
}


// Progress 
function progressBar() {		

	if ($('.progress-bar').length) {

		$('.progress-bar').each(function() {

			$(this).appear(function(){

			 var datavl = $(this).attr('data-percentage');

			 $(this).animate({ "width" : datavl + "%"}, '1200');

			 $(this).find('span').fadeIn(4000);

			 $(this).css('background', $(this).attr('data-bg'));

			})

		});

		$('.progress').each(function() {

			var dathgt = $(this).attr('data-height');

			$(this).css({'line-height': dathgt + "px", 'height': dathgt});

		});

	}

} 


// Pretty Photo
function prettyPhoto() {

	"use strict";
	
	if( $("a[rel^='prettyPhoto'], a[data-rel^='prettyPhoto']").length != 0 ) { 
	
	 $("a[rel^='prettyPhoto'], a[data-rel^='prettyPhoto']").prettyPhoto({hook: 'data-rel', social_tools: false, deeplinking: false});
	
	}

}

// Background Image
function bgImage(){		

	var pageSection = $("section,.bg-img,.img-bg");

	pageSection.each(function(indx){

		if ($(this).attr("data-background")){

			$(this).css("background-image", "url(" + $(this).data("background") + ")");

		}

	});

}


// Fullscreen
function fullscreen() {
	"use strict";
	if ($(window).width() > 1025) {
		$('.full-screen, .full-screen .item').css({ 'height': $(window).height() });
			$(window).on('resize', function() {
			$('.full-screen, .full-screen .item').css({ 'height': $(window).height() });
		});
	}
}


// Owl Slider
 function owlSlider() {

	(function($) {

		"use strict";

		if ($('.owl-carousel').length) {		    

			  $(".owl-carousel").each(function (index) {

				var autoplay = $(this).data('autoplay');

				var timeout = $(this).data('delay');

				var slidemargin = $(this).data('margin');

				var slidepadding = $(this).data('stagepadding');

				var items = $(this).data('items');

				var animationin = $(this).data('animatein');

				var animationout = $(this).data('animateout');

				var itemheight = $(this).data('autoheight');

				var itemwidth = $(this).data('autowidth');

				var itemmerge = $(this).data('merge');

				var navigation = $(this).data('nav');

				var pagination = $(this).data('dots');

				var infinateloop = $(this).data('loop');

				var itemsdesktop = $(this).data('desktop');

				var itemsdesktopsmall = $(this).data('desktopsmall');

				var itemstablet = $(this).data('tablet');

				var itemsmobile = $(this).data('mobile');

				$(this).on('initialized.owl.carousel changed.owl.carousel',function(property){

					var current = property.item.index;

					$(property.target).find(".owl-item").eq(current).find(".animated").each(function(){

						var elem = $(this);

						var animation = elem.data('animate');

						if ( elem.hasClass('visible') ) {

							elem.removeClass( animation + ' visible');

						}

						if ( !elem.hasClass('visible') ) {

							var animationDelay = elem.data('animation-delay');

							if ( animationDelay ) {			

								setTimeout(function(){

								 elem.addClass( animation + " visible" );

								}, animationDelay);				

							} else {

								elem.addClass( animation + " visible" );

							}

						}

					});					

				}).owlCarousel({ 

					autoplay: autoplay,

					autoplayTimeout:timeout,

					items : items,

					margin:slidemargin,

					autoHeight:itemheight,

					animateIn: animationin,

					animateOut: animationout,

					autoWidth:itemwidth,

					stagePadding:slidepadding,

					merge:itemmerge,

					nav:navigation,

					dots:pagination,

					loop:infinateloop,

					responsive:{

						479:{

							items:itemsmobile,

						},

						768:{

							items:itemstablet,

						},

						980:{

							items:itemsdesktopsmall,

						},

						1199:{

							items:itemsdesktop,

						}

					}

				});

			});

		}  

	})(jQuery);

}


// Parallax
function parallaxBg(){		
	if ($(window).width() > 1025) {
		if($('.parallax-bg').length != 0 && !navigator.userAgent.match(/iPad|iPhone|Android/i)){	
	
				$.stellar({
	
					horizontalScrolling: true,
	
					verticalOffset: 0,
	
					horizontalOffset: 0,
	
					responsive: true,
	
					scrollProperty: 'scroll',
	
					parallaxElements: false,
	
			  });
	
			}
		}	

}


// Animation 
function dataAnimations() {
  $('[data-animation]').each(function() {
		var element = $(this);
		element.addClass('animated');
		element.appear(function() {
			var delay = ( element.data('delay') ? element.data('delay') : 1 );
			if( delay > 1 ) element.css('animation-delay', delay + 'ms');				
			element.addClass( element.data('animation') );
			setTimeout(function() {
				element.addClass('visible');
			}, delay);
		});
  });
}

// Column Equal Height
function equalHeight(group) {

	var tallest = 0;

	group.each(function() {

		var thisHeight = $(this).outerHeight();

		if(thisHeight > tallest) {

			tallest = thisHeight;

		}

	});

	group.css("height", tallest);

}

function colEqheight() {

	equalHeight($(".row > .col-eq-height"));

} 



// Isotope Grid
function initIsotopeGrid() {

  $('.isotope-grid').each(function(){  

	   var $port_container = $(this);  

		$containerProxy = $port_container;

		var filter_selector = $port_container.parent().find('.isotope-filters a.active').data('filter');  

		var gutterSize = $port_container.data('gutter');  

		var columns = $port_container.data('columns');

		 

		if ($(window).width() > 1025) {

			$port_container.imagesLoaded(function(){

				if( columns == 2 ) {

					var masonryGutter = gutterSize / columns;					

				} else if( columns == 3 ) {

					var colValue = gutterSize / 2;

					var masonryGutter = colValue + ( colValue / 3 );					

				} else if( columns == 4 ) {

					var colValue = gutterSize / 2;

					var masonryGutter = colValue + ( colValue / 2 );					

				}

				

				// calculate columnWidth

				var colWidth = Math.floor( $containerProxy.width() / columns );

				var masonryWidth = Math.floor( colWidth - masonryGutter );

				

				$port_container.find('.item').css('width', masonryWidth);

				$port_container.find('.item').css('margin-bottom', gutterSize);

		

				$port_container.isotope({

					resizable: false,

					filter: filter_selector,

					animationEngine: "css",

					masonry: {

						columnWidth: masonryWidth,

						gutter: gutterSize

					},

				});

				

				jQuery( window ).bind( 'load resize', function() {

					var colWidth = Math.floor( $containerProxy.width() / columns );

					var masonryWidth = Math.floor( colWidth - masonryGutter );

					$port_container.find('.item').css('width', masonryWidth);

					

					$port_container.isotope({

						masonry: {

							columnWidth: masonryWidth,

							gutter: gutterSize

						},

					});

				});

			});					

		}

		if ($(window).width() > 992 && $(window).width() < 1024) {

			$port_container.imagesLoaded(function(){

				if( columns == 4 ) {

					columns = 3;

				}

				

				if( columns == 2 ) {

					var masonryGutter = gutterSize / columns;					

				} else if( columns == 3 || columns == 4 ) {

					var colValue = gutterSize / 2;

					var masonryGutter = colValue + ( colValue / 3 );					

				}

				

				// calculate columnWidth

				var colWidth = Math.floor( $containerProxy.width() / columns );

				var masonryWidth = Math.floor( colWidth - masonryGutter );

				

				$port_container.find('.item').css('width', masonryWidth);

				$port_container.find('.item').css('margin-bottom', gutterSize);

		

				$port_container.isotope({

					resizable: false,

					filter: filter_selector,

					animationEngine: "css",

					masonry: {

						columnWidth: masonryWidth,

						gutter: gutterSize

					},

				});

				

				jQuery( window ).bind( 'load resize', function() {

					var colWidth = Math.floor( $containerProxy.width() / columns );

					var masonryWidth = Math.floor( colWidth - masonryGutter );

					$port_container.find('.item').css('width', masonryWidth);

					

					$port_container.isotope({

						masonry: {

							columnWidth: masonryWidth,

							gutter: gutterSize

						},

					});

				});

			});	

		}

		if ($(window).width() > 768 && $(window).width() < 991) {

			$port_container.imagesLoaded(function(){

				if( columns == 3 || columns == 4 ) {

					columns = 2;

				}

				

				if( columns == 2 ) {

					var masonryGutter = gutterSize / columns;					

				}

				

				// calculate columnWidth

				var colWidth = Math.floor( $containerProxy.width() / columns );

				var masonryWidth = Math.floor( colWidth - masonryGutter );

				

				$port_container.find('.item').css('width', masonryWidth);

				$port_container.find('.item').css('margin-bottom', gutterSize);

		

				$port_container.isotope({

					resizable: false,

					filter: filter_selector,

					animationEngine: "css",

					masonry: {

						columnWidth: masonryWidth,

						gutter: gutterSize

					},

				});

				

				jQuery( window ).bind( 'load resize', function() {

					var colWidth = Math.floor( $containerProxy.width() / columns );

					var masonryWidth = Math.floor( colWidth - masonryGutter );

					$port_container.find('.item').css('width', masonryWidth);

					

					$port_container.isotope({

						masonry: {

							columnWidth: masonryWidth,

							gutter: gutterSize

						},

					});

				});

			});

		}

		if ($(window).width() < 767) {

			$port_container.imagesLoaded(function(){

				var gutterSize = Math.floor( $port_container.closest('.isotope-grid').attr('data-gutter') );

				$port_container.find('.item').css('width', '100%');

				$port_container.find('.item').css('margin-bottom', gutterSize);

				

				var selector = $port_container.parent().find('.isotope-filters a.active').data('filter');

				

				$port_container.isotope({

					resizable: false,

					filter: filter_selector,

				 	animationEngine: "css",

					masonry: {

						columnWidth: '.item',

						gutter: 0

					},

				});


			});

		}



  

		// Filter

		$('.isotope-filters a').click(function(){

		

			$(this).parent().parent().find('a.active').removeClass('active');    

			$(this).addClass('active');

			var selector = $(this).parent().parent().find('a.active').attr('data-filter');  

			$(this).parents().find('.isotope-grid').isotope({ filter: selector, animationEngine : "css" });

		

			return false; 

		});


	});

}






