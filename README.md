# DASIFORMA

## Preparar o Back

Por favor, crie um ambiente virtual com 

```bash
python -m venv venv      

source venv/bin/activate # ativar no linux ou mac 
.\venv\Scripts\activate  # ativer no windows 
```

Após isso, instale as dependências:
```bash
pip install -r requirements.txt
```

Lembre-se de criar na raiz do projeto backend o arquivo `.env` para guardar seus segredos:
```
STRIPE_SECRET_KEY=sk_tralala...
STRIPE_PUBLIC_KEY=pk_blaha...
PLANILHA_ID=kdopaskdopaskodpkascxm... 
```

Utilize o [`python-dotenv`](https://pypi.org/project/python-dotenv/) para acessar seus segredos.

E pronto, pode codar ;-)
