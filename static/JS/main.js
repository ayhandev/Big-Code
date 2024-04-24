var editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
    lineNumbers: true,
    theme: 'dracula',
    autoCloseBrackets: true,
    matchBrackets: true,
    extraKeys: {"Enter": "autoComplete"}, // Auto-complete on Enter key press
    hintOptions: {hint: CodeMirror.hint.anyword, html: true} // Enable hinting for any word and HTML tags
});

function setLanguage(language) {
    document.getElementById('language-selection').textContent = 'Selected Language: ' + language;
    editor.setOption('mode', language.toLowerCase());
}

// Show language suggestion
document.getElementById('language-search').addEventListener('input', function() {
    var searchValue = this.value.toLowerCase();
    var suggestionBox = document.getElementById('language-suggestion');
    suggestionBox.innerHTML = '';

    languages.forEach(function(language) {
        if (language.toLowerCase().includes(searchValue)) {
            var suggestionItem = document.createElement('div');
            suggestionItem.classList.add('language-suggestion-item');
            suggestionItem.textContent = language;
            suggestionItem.addEventListener('click', function() {
                setLanguage(language);
                suggestionBox.style.display = 'none';
            });
            suggestionBox.appendChild(suggestionItem);
        }
    });

    if (suggestionBox.childElementCount > 0) {
        suggestionBox.style.display = 'block';
    } else {
        suggestionBox.style.display = 'none';
    }
});

// Hide suggestion box on clicking outside
window.addEventListener('click', function(event) {
    var suggestionBox = document.getElementById('language-suggestion');
    if (!event.target.matches('#language-search') && !event.target.closest('#language-suggestion')) {
        suggestionBox.style.display = 'none';
    }
});

// Set language
function setLanguage(language) {
    // Hide language suggestion box
    var suggestionBox = document.getElementById('language-suggestion');
    suggestionBox.style.display = 'none';

    // If the selected language is HTML, insert HTML structure
    if (language.toLowerCase() === 'html') {
        var htmlStructure = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Title</title>
</head>
<body>

</body>
</html>`;
        editor.setValue(htmlStructure);
    } else {
        // Clear editor content for other languages
        editor.setValue('');
    }

    // Set mode and update selected language display
    editor.setOption('mode', language.toLowerCase());
    document.getElementById('language-selection').textContent = 'Selected Language: ' + language;

    // If the selected language is not HTML, set Python as default
    if (language.toLowerCase() !== 'html') {
        document.getElementById('language-search').value = '';
    }
}

// Initial language selection
setLanguage('HTML');

// Languages array
var languages = ['Python', 'HTML'];
    
// Run button click event
document.getElementById('run-button').addEventListener('click', function() {
    runCode();
});

// Function to run code
function runCode() {
    var code = editor.getValue();
    var language = document.getElementById('language-selection').textContent.split(' ')[2]; // Get the selected language
    if (language.toLowerCase() === 'html') {
        // Open the result in a new tab
        var newTab = window.open();
        newTab.document.write(code);
    } else {
        // Execute Python code
        fetch('/run_code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: 'code=' + encodeURIComponent(code) + '&language=' + encodeURIComponent(language)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('terminal').innerText = data.output;
        });
    }
}
