const searchLine = document.querySelector('#elastic');

searchLine.oninput = () => {
	let val = searchLine.value.trim();
	let items = document.querySelectorAll('#search-items li');
	if (val != '') {
	    items.forEach(function(item) {
	        if (item.innerText.search(val) == -1) {
	            item.classList.add('hide');
	            item.querySelector('a div.col-11').innerHTML = item.querySelector('a div.col-11').innerText;
	        } else {
	            item.classList.remove('hide');
	            let str = item.querySelector('a div.col-11').innerText;
	            item.querySelector('a div.col-11').innerHTML = insertSpan(str, item.innerText.search(val), val.length);
	        }
	    })
	} else {
	    items.forEach(function(item) {
	        item.classList.remove('hide');
	        item.querySelector('a div.col-11').innerHTML = item.querySelector('a div.col-11').innerText;
	})
	}
}

function insertSpan(string, pos, len) {
    return string.slice(0, pos) + '<span style="background: #fac83e;">' + string.slice(pos, pos+len) + '</span>' + string.slice(pos+len);
}