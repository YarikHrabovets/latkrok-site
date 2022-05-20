let list = {'jet-print': '/logo', 'аренда': '/order', 'корзина': '/basket', 'про нас': '/about'};
function GoTo(){
	let val = document.getElementById('search').value.toLowerCase();
	if (val in list){
		window.close();
		window.open(list[val]);
	};
};