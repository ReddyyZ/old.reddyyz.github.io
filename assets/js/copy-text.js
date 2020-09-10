function copy_to_clip(document_class){
    var x = document.getElementsByClassName(document_class);
    copyText.select();
    copyText.setSelectionRange(0, 99999);

    document.execCommand("copy");
    return true;
}