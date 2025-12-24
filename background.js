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

// opens the index.html when icon is clicked 
// this should allow users to then add their own websites that wish to block 

chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.create({
        url:"Index.html"
    });
});

// This should block all unwated redirects from websites

chrome.tabs.onCreated.addListener((tab) => {
    if(tab.openerTabId){

        setTimeout(() => {
            chrome.tabs.get(tab.id, (currentTab) => {
                const url = currentTab.url || currentTab.pendingUrl || "";

                //This should now not canel a new tab
                //should fix the tab issue
                if (url.startsWith("chrome://") || url.startsWith("edge://") || url === "about: blank"){
                    return;
                }
                // This should cancel out pop-up that were forced
                chrome.tabs.remove(tab.id);
                console.log("Ace site blocker blocked : " + url);
            });
        }, 100);
        
    }
});