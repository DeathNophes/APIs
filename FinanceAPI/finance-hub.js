const startButton = document.querySelector('.start-button');
const inputField = document.querySelector('.api-field');
const inputSpanText = document.querySelector('#inputSpan');
const apiFieldContainer = document.querySelector('.api-field-container');
const overlay = document.querySelector('#overlay');
const postStartContainer = document.querySelector('.post-start-container');
const result = document.querySelector('#result');

const stockRadioButton = document.querySelector('#stock');
const currencyRadioButton = document.querySelector('#currency');
const assetSearchField = document.querySelector('#asset-search-field');
const searchAssetButton = document.querySelector('.search-button');

let apiKey = '';

// Listen for input changes to the API field
inputField.addEventListener('input', () => {
    apiKey = inputField.value;
});

async function checkApiKey () {
    const url = `https://api.twelvedata.com/quote?symbol=AAPL&apikey=${apiKey}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.symbol) {
            apiFieldContainer.style.display = 'none';
            overlay.style.display = 'block';
            postStartContainer.style.display = 'block';

        } else if (data.code === 401) {
            inputSpanText.textContent = '*Please enter a valid API key from twelvedata.com'
            inputSpanText.style.color = 'red'
        }
    } 
    catch {
        inputSpanText.textContent = '*Please enter a valid API key from twelvedata.com'
        inputSpanText.style.color = 'red'
    }
}

async function searchAsset () {
    const symbol = assetSearchField.value;

    try {
        const response = await fetch(`https://api.twelvedata.com/time_series?symbol=${symbol}&interval=1min&apikey=${apiKey}`)
        const data = await response.json()
        const closePrice = data.values[0].close
        
        buildResult(closePrice, symbol)
    }
    catch {
        console.log('Error')
    }
}

// Button functionality
function brieflyDisableBtn () {
    const button = this;
    const originalColor = button.style.backgroundColor;

    // We change the background color
    button.style.backgroundColor = 'grey';

    // Set the background color back to normal after 100ms
    setTimeout(() => {
        button.style.backgroundColor = originalColor;
    }, 100)
}

function toggleStartButtonState() {
    if (inputField.value.trim() === '') {
        startButton.disabled = true;
        startButton.style.backgroundColor = 'grey';
    } else {
        startButton.disabled = false;
        startButton.style.backgroundColor = 'yellowgreen';
    }
}

function toggleSearchButtonState () {
    if (assetSearchField.value.trim() === '') {
        searchAssetButton.disabled = true;
        searchAssetButton.style.backgroundColor = 'grey';
    } else {
        searchAssetButton.disabled = false;
        searchAssetButton.style.backgroundColor = 'yellowgreen';
    }
}

function showResultDiv () {
    result.style.display = block
}

// Building the result
function buildResult (closePrice, assetSymbol) {
    result.innerHTML = '';

    const symbolP = document.createElement('p');
    symbolP.textContent = `Asset Symbol: `;

    const spanSymbol = document.createElement('span');
    spanSymbol.textContent = `${assetSymbol}`;
    spanSymbol.classList.add('highlight');
    symbolP.appendChild(spanSymbol);

    const priceP = document.createElement('p');
    priceP.textContent = `Last closing price: `;

    const spanPrice = document.createElement('span');
    spanPrice.textContent = `${closePrice}`;
    spanPrice.classList.add('highlight');
    priceP.appendChild(spanPrice)

    result.append(symbolP, priceP)
}

startButton.addEventListener('click', brieflyDisableBtn);
inputField.addEventListener('input', toggleStartButtonState);
startButton.addEventListener('click', checkApiKey);

searchAssetButton.addEventListener('click', searchAsset);
searchAssetButton.addEventListener('click', showResultDiv);
searchAssetButton.addEventListener('click', brieflyDisableBtn)
assetSearchField.addEventListener('input', toggleSearchButtonState)

toggleStartButtonState();
toggleSearchButtonState();