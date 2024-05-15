document.addEventListener('DOMContentLoaded', function () {
    // element-one: Hozzáad egy "box1style" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
elementOne.onclick=function(){
    elementOne.classList.add("box1style")
}
    // element-two: Dupla kattintásra hozzáad egy 2px-es, fekete keretet
    const elementTwo = document.getElementById('element-two');
elementTwo.ondblclick=function(){
    elementTwo.style.border="2px solid black"
}
    // element-three: Ha rámegy az egér, eltűnik
    const elementThree = document.getElementById('element-three');
elementThree.onmouseover=function(){
    elementThree.style.visibility = "hidden"
}
    // element-four: Kattintásra a szövegszín piros lesz benne
    const elementFour = document.getElementById('element-four');
elementFour.onclick=function(){
    elementFour.style.color="red"
}
    // Input mező: Billentyű lenyomásra az inputmező háttérszíne szürke lesz
    const inputField = document.getElementById('myInput');
    inputField.onkeydown=function(){
        inputField.style.backgroundColor="grey"
    }
});