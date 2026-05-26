async function convertPDF() {

    const fileInput = document.getElementById("pdfFile");

    const status = document.getElementById("status");

    const file = fileInput.files[0];

    if (!file) {

        alert("Please select a PDF file.");

        return;

    }

    const formData = new FormData();

    formData.append("file", file);

    try {

        status.innerText = "Processing PDF...";

        const response = await fetch(
            "http://127.0.0.1:8000/convert",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {

            throw new Error("Conversion failed");

        }

        const blob = await response.blob();

        const url = window.URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = url;

        a.download = "converted.docx";

        document.body.appendChild(a);

        a.click();

        a.remove();

        status.innerText =
            "Conversion Completed Successfully!";

    }

    catch (error) {

        console.error(error);

        status.innerText = "Conversion Failed.";

    }

}


/* =========================
   CHATBOT FUNCTION
========================= */

async function askQuestion() {

    const questionInput = document.getElementById(
        "questionInput"
    );

    const answerBox = document.getElementById(
        "answerBox"
    );

    const question = questionInput.value;

    if (!question) {

        alert("Please enter a question.");

        return;

    }

    try {

        answerBox.innerText =
            "AI is thinking...";

        const response = await fetch(
            "http://127.0.0.1:8000/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );

        if (!response.ok) {

            throw new Error("Chat request failed");

        }

        const data = await response.json();

        answerBox.innerText = data.answer;

    }

    catch (error) {

        console.error(error);

        answerBox.innerText =
            "Failed to get AI response.";

    }

}
