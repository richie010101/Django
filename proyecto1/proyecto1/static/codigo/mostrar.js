function sub() {
    
    
    text = document.getElementById("text").value;

    document.getElementById('text2').value = text;
    document.getElementById('imagen').src = text;

    if(text.files && text.files[0])
        alert("Código incrustado en el head" + text.files[0]);
}
