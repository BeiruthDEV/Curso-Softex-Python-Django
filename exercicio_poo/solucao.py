class Usuario:
    
    def __init__(self, nome: str, email: str):
        self.nome = nome
        
        self.__email = email 

    @property
    def email(self) -> str:
        
        return self.__email

    @email.setter
    def email(self, novo_email: str):
       
        if "@" in novo_email:
            self.__email = novo_email
            print(f"[INFO] Sucesso: Email atualizado para '{novo_email}'")
        else:
            print(f"[ERRO] Falha ao atualizar: O email '{novo_email}' é inválido (falta @).")



class CanalEnvio:
    
    def enviar(self, mensagem: str):
       
        raise NotImplementedError("As subclasses devem implementar o método 'enviar'")



class Email(CanalEnvio):
    
    def enviar(self, mensagem: str):
        
        print(f"Enviando para servidor de email: {mensagem}")


class SMS(CanalEnvio):
   
    def enviar(self, mensagem: str):
        
        print(f"Enviando para operadora telefônica: {mensagem}")



class SistemaAlerta:
    
    def __init__(self, usuario: Usuario, canal: CanalEnvio):
        
        self.usuario = usuario
        self.canal = canal

    def disparar(self, texto: str):
        
        print(f"\n--- Notificando Usuário: {self.usuario.nome} ---")
        
        self.canal.enviar(texto)



if __name__ == "__main__":
    print("=== INICIANDO BATERIA DE TESTES ===")

    
    print("\n[1] Teste de Validação de Dados (Encapsulamento)")
    dev_lead = Usuario("Carlos TechLead", "carlos@startup.com")
    
    
    dev_lead.email = "email_invalido_sem_arroba" 
    
    dev_lead.email = "carlos.novo@startup.com"

    
    print("\n[2] Teste de Integração: Canal Email")
    servico_email = Email()
    
    sistema = SistemaAlerta(dev_lead, servico_email)
    sistema.disparar("ALERTA: Servidor de Produção caiu!")

    
    print("\n[3] Teste de Escalabilidade: Mudando para SMS")
    servico_sms = SMS()
    
    
    sistema_mobile = SistemaAlerta(dev_lead, servico_sms)
    sistema_mobile.disparar("STATUS: Pagamento aprovado.")

    print("\n=== FIM DOS TESTES ===")