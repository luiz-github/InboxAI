interface Request {
    emailBody: string;
}

export async function sugestEmailResponse(request: Request) {
    try {
        const res = await fetch(import.meta.env.VITE_BASE_URL + '/api/generateEmailResponse', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ prompt: request.emailBody }),
        });
        const data = await res.json();
        return data.data;
    } catch (err) {
        console.error(err);
        return null;
    }
}

export async function sendFile(file: File) {
    try {
        const formData = new FormData();
        formData.append("file", file);

        const res = await fetch(
            import.meta.env.VITE_BASE_URL + "/api/processFileToPrompt",
            {
                method: "POST",
                body: formData
            }
        );

        if (!res.ok) {
            throw new Error(`Erro no servidor: ${res.status}`);
        }

        const data = await res.json();
        return data.data;
    } catch (err) {
        console.error("Erro ao enviar arquivo:", err);
        return null;
    }
}
