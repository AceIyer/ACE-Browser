// In research I found most extensions need a background.js to manage everything
// This right now is simple , but I'll add one just for justs 

chrome.runtime.onInstalled.addListener(()=>{
    console.log("Ace site blocker is now active. Whoop Whoop!!")
});

//Opens the add.html automatically when Ace is installed
chrome.runtime.onInstalled.addListener((details) => {
    if (details.reason === "install") {
        chrome.tabs.create({
            url: "Index.html"
        });
    }
});