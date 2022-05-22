const alertPlaceholder = document.querySelector('#liveAlertPlaceholder');

const description_btn = document.querySelector('#description-tab');
const char_btn = document.querySelector('#char-tab');
char_btn.style.color = '#2e7d41';

const increase_btn = document.querySelector('#increase');
const decrease_btn = document.querySelector('#decrease');
const input = document.querySelector('#inputQuantity');

const submit_btn = document.querySelector('#submit');

let cartList = JSON.parse(localStorage.getItem("Iron-Horse_JSON"));
if (cartList == null || cartList == ""){
    cartList = [];
}

function alert(icon, message, type) {
    if (alertPlaceholder.hasChildNodes()) {
        alertPlaceholder.innerHTML = '';
    }

    const wrapper = document.createElement('div');

    wrapper.innerHTML = `<div class="alert alert-${type} alert-dismissible" role="alert">
        ${icon}
        ${message}
        <a href="/basket" class="alert-link">Корзина</a>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`;

    alertPlaceholder.append(wrapper);
}

description_btn.onclick = () => {
    char_btn.style.color = '#2e7d41';
    description_btn.style.color = '#000';
}
char_btn.onclick = () => {
    description_btn.style.color = '#2e7d41';
    char_btn.style.color = '#000';
}

increase_btn.onclick = () => {
    console.log(input.value, input.max);
    if (input.value < Number(input.max)){
        input.value++;
    } else {
        document.querySelector('#tip').style.display = 'block';
    }
}

decrease_btn.onclick = () => {
    if (input.value > 1){
        document.querySelector('#tip').style.display = 'none';
        input.value--;
    }
}

input.addEventListener('change', () => {
    if (input.value < 1) {
        input.value = 1
    } else if (input.value >= Number(input.max)) {
        input.value = input.max;
        document.querySelector('#tip').style.display = 'block';
    }
})

submit_btn.onclick = () => {
    const cart = {
        img: document.querySelector('#productImg').src,
        name: document.querySelector('#productTitle').innerHTML,
        model: "Iron-Horse",
        type: "Спец предложение",
        money: "грн",
        color: document.querySelector('#color').innerHTML,
        count: document.querySelector('#inputQuantity').value,
        prise: document.querySelector('#prise').innerHTML,
        all_prise: document.querySelector('#inputQuantity').value * document.querySelector('#prise').innerHTML
    };
    cartList.push(cart);
    localStorage.setItem("Iron-Horse_JSON", JSON.stringify(cartList));
    window.location.href = '#';
    alert('<svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:"><use xlink:href="#check-circle-fill"/></svg>', 'Товар успешно добавлен!', 'success');
}