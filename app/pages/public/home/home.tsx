import Button from "../../../components/button/button"

export function Home() {
  return (
    <section>
      <Button 
        name="PDF upload"
        variant="secondary"
        onClick={() => alert('botão clicado')}
      />
    </section>
  );
}