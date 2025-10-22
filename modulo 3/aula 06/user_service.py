from user_model import UserModel
from hasher import hash_senha, verificar_senha
import re

class UserService:

    def __init__(self):
        self.user_model = UserModel()

    def _safe_user_data(self, user) -> dict | None:
        if not user:
            return None

        return {
            "id": user["id"],
            "email": user["email"],
            "nome_completo": user["nome_completo"],
            "perfil_acesso": user["perfil_acesso"],
            "data_criacao": user["data_criacao"],
            "data_atualizacao": user["data_atualizacao"],
        }


    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        if current_user_profile == "Diretoria":
            return True

        if target_user_id is None:
            return False

        if action == "edit_self":
            return current_user_id == target_user_id

        return False

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        if not senha or len(senha) < 8:
            return False, "A senha deve conter no mínimo 8 caracteres."

        if (
            not email
            or len(email) < 10
            or "@" not in email
            or not email.endswith(".com")
        ):
            return False, "E-mail inválido. Deve conter '@' e terminar com '.com'."

        if not nome_completo or not nome_completo.replace(" ", "").isalpha():
            return False, "O nome deve conter apenas letras e não pode estar vazio."

        senha_hash = hash_senha(senha)

        return self.user_model.create_user(
            senha_hash=senha_hash,
            email=email,
            nome_completo=nome_completo,
            perfil_acesso=perfil,
        )
    
    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        
        if not email or not senha:
            return None, "E-mail e senha são obrigatórios."

        user = self.user_model.find_user_by_email(email)
        if not user:
            return None, "Usuário não encontrado."

        if not verificar_senha(senha, user["senha_hash"]):
            return None, "Senha incorreta."

        return self._safe_user_data(user), "Login bem-sucedido!"

    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        if not self._is_authorized(
            current_user_id, current_user_profile, target_user_id, "edit_self"
        ):
            return False, "Acesso negado."

        updates = {}
        if new_data.get("senha"):
            if len(new_data["senha"]) < 8:
                return False, "A nova senha deve ter no mínimo 8 caracteres."
            updates["senha_hash"] = hash_senha(new_data["senha"])

        if new_data.get("email"):
            email = new_data["email"]
            if len(email) < 10 or "@" not in email or not email.endswith(".com"):
                return False, "E-mail inválido."
            updates["email"] = email

        if new_data.get("nome_completo"):
            nome = new_data["nome_completo"]
            if not nome.replace(" ", "").isalpha():
                return False, "O nome deve conter apenas letras."
            updates["nome_completo"] = nome

        if not updates:
            return False, "Nenhum dado válido para atualizar."

        
        return self.user_model.update_user_by_id(target_user_id, updates)

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        if current_user_profile != "Diretoria":
            return False, "Acesso negado. Apenas a Diretoria pode deletar usuários."

        return self.user_model.delete_user_by_id(user_id)


    def get_user_by_id(self, user_id: int) -> dict | None:
        
        user = self.user_model.find_user_by_id(user_id)
        return self._safe_user_data(user)


    def get_all_users(self) -> list[dict | None]:
        
        users = self.user_model.get_all_users()
        return [self._safe_user_data(u) for u in users if u]