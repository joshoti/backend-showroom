Element.prototype.parents = function(selector) {
    var elements = [];
    var elem = this;
    var ishaveselector = selector !== undefined;

    while ((elem = elem.parentElement) !== null) {
        if (elem.nodeType !== Node.ELEMENT_NODE) {
            continue;
        }

        if (!ishaveselector || elem.matches(selector)) {
            elements.push(elem);
        }
    }

    return elements;
};

function setActiveCarouselItem(card) {
    var target = card.querySelector('.carousel-item'),
        firstIndicator = card.querySelector('.carousel-indicators > li')
    target.classList.add('active');
    if (firstIndicator) firstIndicator.classList.add('active');
} 
function initTestimonialsCarousel(card) {
    var target = card,
        carouselID = target.getAttribute('id') + '-carousel',
        bs5 = target.getAttribute('data-bs-version') === '5';
    target.querySelectorAll('.carousel').forEach(el => el.setAttribute('id', carouselID));
    if (target.querySelector('.carousel-controls')) target.querySelectorAll('.carousel-controls').forEach(el => {
        el.querySelectorAll('a').forEach(el => {
            el.setAttribute('href', '#' + carouselID);
            bs5 ? el.setAttribute('data-bs-target', '#' + carouselID)
            : el.setAttribute('data-target', '#' + carouselID);
        }); 
    })
    target.querySelectorAll('.carousel-indicators > li').forEach(el => {
        bs5 ? el.setAttribute('data-bs-target', '#' + carouselID)
        : el.setAttribute('data-target', '#' + carouselID);
    });
    setActiveCarouselItem(target);
}


function initClientCarousel(card) {
    var target = card,
        countElems = target.querySelectorAll('.carousel-item').length,
        visibleSlides = target.querySelector('.carousel-inner').getAttribute('data-visible');
    if (countElems < visibleSlides) {
        visibleSlides = countElems;
    }
    target.querySelectorAll('.carousel-inner').forEach(el => el.setAttribute('class', 'carousel-inner slides' + visibleSlides));
    target.querySelectorAll('.clonedCol').forEach(el => el.remove());

    target.querySelectorAll('.carousel-item .col-md-12').forEach(function (el) {
        if (visibleSlides < 2) {
            el.setAttribute('class', 'col-md-12');
        } else if (visibleSlides == '5') {
            el.setAttribute('class', 'col-md-12 col-lg-15');
        } else {
            el.setAttribute('class', 'col-md-12 col-lg-' + 12 / visibleSlides);
        }
    });

    // css fix for carousel mess in bs5
    target.querySelectorAll('.carousel-item .row').forEach(el => {
        el.setAttribute('style', '-webkit-flex-grow: 1; flex-grow: 1; margin: 0;')
    });

    target.querySelectorAll('.carousel-item').forEach(function (el) {
        var itemToClone = el;
        for (var i = 1; i < visibleSlides; i++) {
            itemToClone = itemToClone.nextElementSibling;
            if (!itemToClone) {
                itemToClone = el.parentNode.children[0] === el ? el.nextElementSibling : el.parentNode.children[0];
            }
            var index = getIndex(itemToClone);
            var clonedItem = itemToClone.querySelector('.col-md-12').cloneNode(true);
            clonedItem.classList.add('cloneditem-' + i);
            clonedItem.classList.add('clonedCol');
            clonedItem.setAttribute('data-cloned-index', index);
            el.children[0].appendChild(clonedItem);
        }
    });
}

function getIndex(el) {
    if (!el) return -1;
    var i = 0;
    do {
      i++;
    } while (el = el.previousElementSibling);
    return i;
}


function updateClientCarousel(card){
    var target = $(card),
        countElems = target.find('.carousel-item').length,
        visibleSlides = target.find('.carousel-inner').attr('data-visible');
    if (countElems < visibleSlides){
        visibleSlides = countElems;
    }
    target.find('.clonedCol').remove();
    target.find('.carousel-item').each(function() {
        var itemToClone = $(this);
        for (var i = 1; i < visibleSlides; i++) {
            itemToClone = itemToClone.next();
            if (!itemToClone.length) {
                itemToClone = $(this).siblings(':first');
            }
            var index = itemToClone.index();
            itemToClone.find('.col-md-12:first').clone().addClass('cloneditem-' + i).addClass('clonedCol').attr('data-cloned-index', index).appendTo($(this).children().eq(0));
        }
    });
}



function clickHandler(e){
    e.stopPropagation();
    e.preventDefault();

    var target = e.target;
    var curItem;
    var curIndex;

    if (target.closest('.clonedCol').length) {
        curItem = target.closest('.clonedCol');
        curIndex = curItem.getAttribute('data-cloned-index');
    } else {
        curItem = target.closest('.carousel-item');
        curIndex = getIndex(curItem);
    }
    var item = target.closest('.carousel-inner').querySelectorAll('.carousel-item')[curIndex].querySelector('img');
 
    if (target.parents('.clonedCol').length > 0) {
        item.dispatchEvent(new CustomEvent('click'));
    }
}

// Mobirise initialization
var $,
    isJQuery = typeof jQuery == 'function';
if (isJQuery) $ = jQuery;
var isBuilder = document.querySelector('html').classList.contains('is-builder');

if (isBuilder) {
    $(document).on('add.cards', function(event) {
        if (!$(event.target).hasClass('clients')) {
            return;
        }
        initTestimonialsCarousel(event.target);
        initClientCarousel(event.target);
        if (event.type === 'add') {       
            $(event.target).on('slide.bs.carousel', function() {
                updateClientCarousel(event.target);
            });
        }
        $(event.target).find('.carousel-item [mbr-media]').on('click', function(e) {
            clickHandler(e);
        });
        $(event.target).on('slide.bs.carousel', function() {
            $(event.target).find('.carousel-item .clonedCol [mbr-media]').off('click').on('click', function(e) {
                        clickHandler(e);
                    });
        });
    }).on('changeParameter.cards', function(event, paramName,value) {
        if (!$(event.target).hasClass('clients')) {
            return;
        }
        if (paramName=='slidesCount'){
            if ($(event.target).find('.carousel-item.active').length==0) {
                setActiveCarouselItem(event.target);
            }                
        }
        initClientCarousel(event.target);
        updateClientCarousel(event.target);
        $(event.target).find('.carousel-item [mbr-media]').on('click', function(e) {
            clickHandler(e);
        });
        $(event.target).on('slide.bs.carousel', function() {
            $(event.target).find('.carousel-item .clonedCol [mbr-media]').off('click').on('click', function(e) {
                        clickHandler(e);
                    });
        });
    }).on('changeContent.cards', function(event, type) {
        if (!$(event.target).hasClass('clients')) {
            return;
        }
        updateClientCarousel(event.target);
        try{
            $(event.target).closest('.carousel').carousel('next');
        } catch(err) {}
    });
} else {
    if(typeof window.initClientPlugin === 'undefined'){
        window.initClientPlugin = true;
        document.body.querySelectorAll('.clients').forEach(function(el) {
            if(!el.getAttribute('data-isinit')){
                initTestimonialsCarousel(el);
                initClientCarousel(el);
            }  
        });  
    }
}