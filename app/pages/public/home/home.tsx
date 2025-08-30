import Button from "../../../components/button/button"
import TextArea from "~/components/textArea/textArea"
import {sendFile, sugestEmailResponse} from "./../../../api/inboxIA"
import {useState, useRef} from "react";

export function Home() {
    const [inputValue, setInputValue] = useState('');
    const [emailSugestion, setEmailSugestion] = useState<{ resposta: string } | null>(null);
    const fileInputRef = useRef<HTMLInputElement | null>(null);
    const [loading, setLoading] = useState(false);


    const handleGenerate = () => {
        setLoading(true);
        sugestEmailResponse({ emailBody: inputValue })
            .then(resposta => setEmailSugestion(resposta))
            .then(() => setInputValue(''))
            .catch(err => console.log(err))
            .finally(() => setLoading(false));
    }

    const handleFileClick = (type: "pdf" | "txt") => {
        if (fileInputRef.current) {
            fileInputRef.current.accept = type === "pdf" ? ".pdf" : ".txt";
            fileInputRef.current.click();
        }
    }

    const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
        setLoading(true);
        const file = e.target.files?.[0]
        if (!file) return
        try {
            const data = await sendFile(file)
            setLoading(false);
            if (!data.resposta) {
                setEmailSugestion({ resposta: "Erro ao processar arquivo" })
            }
            setEmailSugestion(data)
        } catch (err: any) {
            console.log(err)
            setEmailSugestion({ resposta: "Erro ao processar arquivo" })
        }
    };

  return (
      <section className="flex flex-col justify-center items-center h-screen space-y-4">
          {loading ? (
              <p className="max-w-2xl p-4 text-white text-center">Carregando...</p>
          ) : emailSugestion?.resposta && (
              <p className="max-w-2xl p-4 text-white whitespace-pre-line">
                  {emailSugestion.resposta}
              </p>
          )}

          <div className="flex flex-col w-full max-w-2xl rounded-2xl border border-gray-700 bg-gray-900 px-4 py-4 space-y-4">
              <div className="flex items-center w-full rounded-xl bg-gray-800 px-3 py-2">
                  <TextArea
                      placeholder="Colar email aqui..."
                      value={inputValue}
                      onChange={e => setInputValue(e.target.value)}
                  />
                  <Button
                      name="Enviar"
                      variant="outline"
                      className="ml-2"
                      onClick={handleGenerate}
                  />
              </div>
              <div className="flex justify-start">
                  <input type="file" className="hidden" onChange={handleFileChange} ref={fileInputRef} />
                  <Button
                      name="pdf"
                      variant="secondary"
                      onClick={() => handleFileClick("pdf")}
                  />
                  <Button
                      name="txt"
                      variant="primary"
                      onClick={() => handleFileClick("txt")}
                  />
              </div>
          </div>
      </section>
  );
}