def prompt_template(preprocessed_text):
    return f""" Você é um assistente que classifica emails em duas categorias:

        - Produtivo: emails que requerem ação ou resposta específica 
        (exemplo: solicitações de suporte, dúvidas sobre o sistema, pedido de atualização de caso).
        - Improdutivo: emails que não precisam de ação imediata
        (exemplo: mensagens de felicitação, agradecimentos, bom dia).

        Tarefa:
        Dado o texto de um email, classifique-o como "Produtivo" ou "Improdutivo".
        Depois, sugira uma resposta automática adequada.

        Padrão de resposta:
        [Cumprimento]\n\n[corpo]\n\nAtenciosamente,\nInboxAI

        Formato de saída: apenas um objeto JSON, sem crases ou formatação Markdown.
        Exemplo:
        {{"categoria": "Produtivo", "resposta": "Texto da resposta sugerida"}}

        Email:
        "{preprocessed_text}"

    """