async function buscaCliente() {
    const doc_cpf = document.getElementById('cpf').value;
    if (!doc_cpf){
        alert('Digita o cpf');
        return;
    }
    //devemos tratar erros 
    const response =await fetch (`http://127.0.0.1:5000/consulta?doc=${doc_cpf}`)

    const dados = await response.json() //pega cada valor individualmente, se voce pode pra devolver como json
    console.log('dados')
    document.getElementById('nome').textContent = dados.nome || "não";
    document.getElementById('nasc').textContent = dados.data_nascimento;
    document.getElementById('email').textContent = dados.email;
} 
async function cadastrarCliente() {
    // pegar os valores inseridos no html
    const cpf =  document.getElementById('cadcpf').value;
    const nome = document.getElementById('cadnome').value;
    const data_nascimento = document.getElementById('cadnascimento').value;
    const email =document.getElementById('cademail').value;

    // criar a estrutura que definimos pro json
    const payload = {
        cpf,
        dados: {
            nome,
            data_nascimento,
            email
        }
    };

    // fazer a requisicao no backend
    const response = await fetch('http://127.0.0.1:5000/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
        const retorno = await response.json();
        if(retorno){
            alert("CPF duplicado")
        }else{
            alert("Cadastro efetuado com sucesso")
        }
    }
    