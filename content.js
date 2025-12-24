// This file is responsible for preventing pop up windows that the user may encounter on websites
const originalOpen = window.open;

window.open = function(url, name, features){
    console.log("Blocked redirect to " + url);

    return null;
};

window.addEventListener('beforeunload', (event) => {
    event.preventDefault();
    event.returnValue = '';
});

const meta = document.querySelector('meta[http-equiv="refresh"]');
if (meta) {
    meta.remove();
    console.log("Ace Blocker removed a hidden redirect")
};

// This should help between good and bad redirects
let lastClickTime = 0;
document.addEventListener('click', () => {
    lastClickTime = Date.now();
});

window.open = function(url){
    if(Date.now() - lastClickTime < 500){
        return originalOpen(url);
    }
    else{
        // This was maybe a forced redirect
        console.log("Ace Blocked a forced redirect");
        return null;
    }
};