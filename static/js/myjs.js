function setUserTheme() {
    var color = localStorage.getItem('color')
    console.log(color)
    if (color != '') {
        // 1:optimistic  2:pessimistic 3.neutral
        if (color == 'red') {
            document.getElementById("mycss").setAttribute("href", "/static/css/home_red.css")
        } else if (color == 'blue') {
            document.getElementById("mycss").setAttribute("href", "/static/css/home_blue.css")
        }
    }
}