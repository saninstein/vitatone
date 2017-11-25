ymaps.ready(function () {
	    var myMap = new ymaps.Map('map', {
	            center: [50.421100 , 30.528535],
	            zoom: 15,
	            controls: []
	        }, {
	            searchControlProvider: 'yandex#search'
	        }),
	        myPlacemark = new ymaps.Placemark(myMap.getCenter(), {
	            hintContent: 'Офiс Vitatone',
	            balloonContent: 'Україна, Київ, вулиця Патріса Лумумби, 3'
	        }, 
	        {
	            // Опции.
	            // Необходимо указать данный тип макета.
	            iconLayout: 'default#image',
	            // Своё изображение иконки метки.
	            iconImageHref: '/static/img/logo.png',
	            // Размеры метки.
	            iconImageSize: [60, 35],
	            iconImageOffset: [-23, -23]
	        });
	    myMap.geoObjects.add(myPlacemark);
	    myMap.setCenter([50.413715 , 30.512803], 14, {});
});