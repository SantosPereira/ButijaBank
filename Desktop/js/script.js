function roda(){
    let {PythonShell} = require('python-shell');

    PythonShell.run('C:/Git/SistemaBancoButija/GUI.py', null, function (err) {
        if (err) throw err;
        console.log('finished');
    });
}



const Dao = require('C:/Git/SistemaBancoButija/Desktop/API/dao')
const dao = new Dao

dao.admin().then((results) => {
        tela_dados = $("#dados").attr("hidden", false)
    }).catch((err) => {
        console.log('OCORREU UM ERRO')
        console.log(err)
    })

function get_cpf(){
    var tela_dados = $("#tela_dados").attr("hidden", false)
    var tela = $("#tela").remove()
    tela = $("#tela").append(tela_dados)

    

    
    //agora chamar o código python
    roda()
}

function get(){
    var loading = $(".loading").attr("hidden", false)
    var acesso = $("#acesso").remove()
    acesso = $("#acesso").append(loading)
    setInterval(get_cpf,3000)
    // chamar animação css
}

