// This file is responsible for preventing pop up windows that the user may encounter on websites
const originalOpen = window.open;

window.open = function(url, name, features){
    console.log("Blocked redirect to " + url);

    return null;
};