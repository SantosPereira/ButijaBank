const mysql = require('mysql2');

class Dao {
    constructor(){
        this._connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        database: 'butija_db'
        });
    }

    admin(){
        return new Promise((resolve, reject)=>{
            this._connection.query(
                'SELECT * FROM main',
                function(err, results) {
                    if(err){
                        reject(err)
                    }
                    else{
                        resolve(results)
                    }
                }
              );
        })
    }

}
    /*
    list(){
        return new Promise((resolve, reject)=>{
            this._connection.query(
                'SELECT * FROM alunos',
                function(err, results) {
                    if(err){
                        reject(err)
                    }
                    else{
                        resolve(results)
                    }
                }
              );
        })
    }
    save(aluno){
        return new Promise((resolve, reject)=>{
            this._connection.query(
                'insert into alunos (nome, email, curso) values (?,?,?)', [aluno.nome, aluno.email, aluno.curso],
                function(err, results) {
                    if(err){
                        reject(err)
                    }
                    else{
                        resolve(results)
                    }
                }
              );
        })
    }

    update(aluno){
        return new Promise((resolve, reject)=>{
            this._connection.query(
                'update alunos set nome=?, email=?, curso=? where id=?', [aluno.nome, aluno.email, aluno.curso, aluno.id],
                function(err, results) {
                    if(err){
                        reject(err)
                    }
                    else{
                        resolve(results)
                    }
                }
              );
        })
    }

    findById(id){
        return new Promise((resolve, reject)=>{
            this._connection.query(
                'SELECT * FROM alunos where id=?', [id],
                function(err, results) {
                    if(err){
                        reject(err)
                    }
                    else{
                        resolve(results)
                    }
                }
              );
        })
    }
    delete(id){
        return new Promise((resolve, reject)=>{
            this._connection.query(
                'delete from alunos where id=?', [id],
                function(err, results) {
                    if(err){
                        reject(err)
                    }
                    else{
                        resolve(results)
                    }
                }
              );
        })
    }
}
module.exports = Dao
*/