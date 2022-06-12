let cart = document.getElementById("basket_id");
let iron_objs = JSON.parse(localStorage.getItem("Iron-Horse_JSON"));
let prise_list = [];
if (iron_objs !== null) {
    document.getElementById("form").style.display = 'block';
    for (index in iron_objs){
        let ul = document.createElement("ul");
        ul.className = "list-group list-group-horizontal";
        ul.id = "ul";

        ul.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item"><img class="img-fluid" src="' + iron_objs[index]['img'] + '"></li>';
        ul.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item">' + iron_objs[index]['name'] + '</li>';
        ul.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item">' + iron_objs[index]['model'] + '<br>' + iron_objs[index]['color'] + '<br><span style="color: #339c3e;">' + iron_objs[index]['type'] + '</span></li>';
        ul.innerHTML += `<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item"><div class="input-group btn-block" style="max-width: 200px;"><input id="count-${index}" type="text" value="` + iron_objs[index]['count'] + `"` + `size="1" class="form-control">
            <button type="submit" data-toggle="tooltip" title="" class="btn btn-success" data-original-title="Обновить" onclick="setCount('count-${index}', ${index})"><i class="fa fa-refresh"></i></button>
            <button type="button" data-toggle="tooltip" title="" class="btn btn-danger" data-original-title="Удалить" onclick="clearElem(${index}, ${iron_objs.length})"><i class="fa fa-times-circle"></i></button></div></li>`;
        ul.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item">' + iron_objs[index]['prise'] + ' ' + iron_objs[index]['money'] + '</li>';
        ul.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item">' + iron_objs[index]['all_prise'] + ' ' + iron_objs[index]['money'] +'</li>';
        prise_list.push(iron_objs[index]['all_prise']);
        cart.append(ul);
    }
    let total_sum = document.createElement("ul");
    total_sum.className = "list-group list-group-horizontal mt-3";
    total_sum.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item">Вся сума:</li>';
    total_sum.innerHTML += '<li class="col-6 col-sm-4 col-md-3 col-xl-2 list-group-item">' + sum(prise_list) + ' грн</li>';
    cart.append(total_sum);

    btn_row = document.createElement("div");
    btn_row.className = "d-flex";
    btn_row.innerHTML += '<button onclick="clearFunc()" class="btn btn-secondary m-2">Очистити кошик</button>';
    btn_row.innerHTML += '<a href="/order" class="btn btn-primary m-2">Продовжити покупки</a>';
    cart.append(btn_row);
}
function sum(list){
    let sum = 0;
    list.forEach((i) => {
        sum += i;
    })
    return sum
}
function setCount(id, index){
    const val = document.getElementById(id).value;
    iron_objs[index]["count"] = val;
    iron_objs[index]['all_prise'] = val * iron_objs[index]['prise'];
    localStorage.setItem("Iron-Horse_JSON", JSON.stringify(iron_objs));
    window.location.reload();
}
function clearElem(index, len){
    if (len == 1) {
        clearFunc();
    } else {
        iron_objs = iron_objs.filter((item) => {
            return item != iron_objs[index];
        });
        localStorage.setItem("Iron-Horse_JSON", JSON.stringify(iron_objs));
        window.location.reload();
    }
}
function clearFunc(){
    localStorage.removeItem("Iron-Horse_JSON");
    window.location.reload();
}
function fillDetailField(){
    let iron_objs = JSON.parse(localStorage.getItem("Iron-Horse_JSON"));
    let cart = document.getElementById("details");

    if (Number(cart.innerHTML) == 0) {
        for (i in iron_objs){
            cart.innerHTML += `Ім´я: ${iron_objs[i]['name']},\n`;
            cart.innerHTML += `Модель: ${iron_objs[i]['model']},\n`;
            cart.innerHTML += `Колір: ${iron_objs[i]['color']},\n`;
            cart.innerHTML += `Тип: ${iron_objs[i]['type']},\n`;
            cart.innerHTML += `Кількість: ${iron_objs[i]['count']},\n`;
            cart.innerHTML += `Ціна одиниці: ${iron_objs[i]['prise']} ${iron_objs[i]['money']},\n\n\n`;
            cart.innerHTML += `Вся ціна: ${iron_objs[i]['all_prise']} ${iron_objs[i]['money']}\n\n\n`;
        }
    }
};
fillDetailField();
