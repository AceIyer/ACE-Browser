// Final add.js
const input = document.getElementById('urlInput');
const btn = document.getElementById('addBtn');
const list = document.getElementById('siteList');

// add a site to the rules
btn.addEventListener('click', () => {
    const domain = input.value.trim();
    if (!domain) return;

    const ruleId = Math.floor(Date.now() / 1000);

    chrome.declarativeNetRequest.updateDynamicRules({
        addRules: [{
            "id": ruleId,
            "priority": 1,
            "action": { 
                "type": "redirect",
                "redirect": { "extensionPath": "/blocked.html" }
            },
            "condition": { "urlFilter": domain, "resourceTypes": ["main_frame"] }
        }]
    }, () => {
        if (chrome.runtime.lastError) {
            console.error(chrome.runtime.lastError);
        } else {
            renderList();
            input.value = '';
        }
    });
});

//generate the blocked sites
function renderList() {
    chrome.declarativeNetRequest.getDynamicRules((rules) => {
        list.innerHTML = '<h3>Blocked Sites:</h3>';
        
        rules.forEach(rule => {
            const div = document.createElement('div');
            div.className = 'site-item';
            div.style.display = 'flex';
            div.style.justifyContent = 'space-between';
            div.style.marginBottom = '5px';
            
            div.innerHTML = `
                <span>${rule.condition.urlFilter}</span>
                <button class="remove-btn" data-id="${rule.id}">Unblock</button>
            `;
            list.appendChild(div);
        });

        // 3. REMOVE RULE LOGIC (Inside click listeners)
        document.querySelectorAll('.remove-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                const idToRemove = parseInt(e.target.getAttribute('data-id'));
                removeRule(idToRemove);
            });
        });
    });
}

function removeRule(id) {
    chrome.declarativeNetRequest.updateDynamicRules({
        removeRuleIds: [id]
    }, () => {
        renderList();
    });
}

// Initial load
renderList();