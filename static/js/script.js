document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('templateForm').addEventListener('submit', function(e) {
        e.preventDefault(); // Prevents the default form submission action

        // Collecting form data
        const formData = {
            recipientName: document.getElementById('recipientName').value,
            emailSubject: document.getElementById('emailSubject').value,
            keyPoints: document.getElementById('keyPoints').value,
            tone: document.getElementById('tone').value,
            additionalInstructions: document.getElementById('additionalInstructions').value
        };

        // Sending the data to the Flask server
        fetch('/generate_template', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            // Displaying the generated email template in the textarea
            document.getElementById('editableTemplate').value = data.generatedTemplate;

            // Make the template output visible
            document.getElementById('templateOutput').style.display = 'block';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
