class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self, id, nome, email):
        usuario = Usuario(id, nome, email)
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

    def atualizar_usuario(self, id, novo_nome=None, novo_email=None):
        for usuario in self.usuarios:
            if usuario.id == id:
                if novo_nome:
                    usuario.nome = novo_nome
                if novo_email:
                    usuario.email = novo_email
                break

    def deletar_usuario(self, id):
        self.usuarios = [usuario for usuario in self.usuarios if usuario.id != id]

# Exemplo de uso
sistema = SistemaUsuarios()
sistema.criar_usuario(1, "João", "joao@example.com")
sistema.criar_usuario(2, "Maria", "maria@example.com")
sistema.listar_usuarios()

sistema.atualizar_usuario(1, novo_nome="João Silva")
sistema.listar_usuarios()

sistema.deletar_usuario(2)
sistema.listar_usuarios()

### Explicação:
# Criamos uma aplicação CRUD simples com a classe SistemaUsuarios, onde podemos criar, listar, atualizar e deletar usuários.
# Este exemplo é um passo em direção ao desenvolvimento de sistemas completos com banco de dados e APIs, que é o coração do fullstack.