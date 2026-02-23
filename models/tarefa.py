from sqlite3 import Cursor
from models.database import Database
from typing import Self, Any, Optional

class Recomendacao:
    """
    Classe que representa uma recomendação anotada.
    """
    def __init__(self: Self, titulo_recomendacao: Optional[str], quem_recomendacao: Optional[str] = None, tipo_recomendacao: Optional[str] = None, id_recomendacao: Optional[int] = None) -> None:
        self.titulo_recomendacao: Optional[str] = titulo_recomendacao
        self.quem_recomendacao: Optional[str] = quem_recomendacao
        self.tipo_recomendacao: Optional[str] = tipo_recomendacao
        self.id_recomendacao: Optional[int] = id_recomendacao


    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = "SELECT titulo_recomendacao, quem_recomendacao, tipo_recomendacao FROM recomendacoes WHERE id = ?;"
            params:tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)

            [[titulo, quem, tipo]] = resultado

        return cls(id_recomendacao=id, titulo_recomendacao=titulo, quem_recomendacao=quem, tipo_recomendacao=tipo)

    def salvar_recomendacao(self: Self) -> None:
        with Database() as db:
            query: str = "INSERT INTO recomendacoes (titulo_recomendacao, quem_recomendacao, tipo_recomendacao) VALUES (?,?,?);"
            params: tuple = (self.titulo_recomendacao, self.quem_recomendacao, self.tipo_recomendacao)
            db.executar(query, params)

    @classmethod
    def obter_recomendacoes(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_recomendacao, quem_recomendacao, tipo_recomendacao, id FROM recomendacoes;'
            resultados: list[Any] = db.buscar_tudo(query)
            recomendacoes: list[Self] = [cls(titulo, quem, tipo, id) for titulo, quem, tipo, id in resultados]
            return recomendacoes
        
    def excluir_recomendacao(self) -> Cursor:
        with Database() as db:
            query: str = "DELETE FROM recomendacoes WHERE id = ?;"
            params: tuple = (self.id_recomendacao,)
            return db.executar(query, params)
        
    def atualizar_recomendacao(self) -> Cursor:
        with Database() as db:
            query: str = "UPDATE recomendacoes SET titulo_recomendacao = ?, quem_recomendacao = ?, tipo_recomendacao = ? WHERE id = ?;"
            params: tuple = (self.titulo_recomendacao, self.quem_recomendacao, self.tipo_recomendacao, self.id_recomendacao)
            resultado: Cursor = db.executar(query, params)
            return resultado 