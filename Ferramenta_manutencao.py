import customtkinter as ctk
import subprocess
import os
import shutil  
from customtkinter import FontManager


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


try:
    FontManager.load_font("Orbitron-Bold.ttf")
    fonte_titulo = ("Orbitron", 24, "bold")
except:
    fonte_titulo = ("Arial", 24, "bold")


class AppManutencao(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("Ferramenta de Reparo - v1.0")
        self.geometry("800x800")


        self.label_titulo = ctk.CTkLabel(self, text="FERRAMENTA DE REPARO", font=fonte_titulo)
        self.label_titulo.pack(pady=20)


        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(pady=10)


        self.btn_ipconfig = ctk.CTkButton(self.frame_botoes, text="Executar IPCONFIG",font=("Arial", 14, "bold"),
                                          command=lambda: self.executar("ipconfig"))
                                         
        self.btn_ipconfig.grid(row=0, column=0, padx=10, pady=10)


        self.btn_system = ctk.CTkButton(self.frame_botoes, text="Executar SYSTEMINFO",font=("Arial", 14, "bold") ,
                                        command=lambda: self.executar("systeminfo"))
        self.btn_system.grid(row=1, column=0, padx=10, pady=10)


        self.btn_remote = ctk.CTkButton(self.frame_botoes, text="ACESSO REMOTO",font=("Arial", 14, "bold"),
                                        command=lambda: self.executar("mstsc"))
        self.btn_remote.grid(row=0, column=1, padx=10, pady=10)


        self.btn_limpeza = ctk.CTkButton(self.frame_botoes, text="LIMPEZA TOTAL (Temp/Lixeira)",font=("Arial", 14, "bold") ,
                                         command=self.realizar_limpeza_completa)
       
        self.btn_limpeza.grid(row=1, column=1, padx=10, pady=10)


        self.btn_teste2 = ctk.CTkButton(self.frame_botoes, text="LIMPEZA MANUAL",font=("Arial", 14, "bold") ,
                                        command=lambda: self.executar("cleanmgr"))
        self.btn_teste2.grid(row=0, column=3, padx=10, pady=10)


        self.btn_teste3 = ctk.CTkButton(self.frame_botoes, text="EM BREVE", state="disabled",font=("Arial", 14, "bold") ,
                                        command=lambda: self.executar(""))
        self.btn_teste3.grid(row=1, column=3, padx=10, pady=10)


        self.btn_sair = ctk.CTkButton(self, text="SAIR",font=("Arial", 14, "bold") , fg_color="red" , hover_color="#ff4d4d",
                                      command=self.destroy)
        self.btn_sair.pack(pady=50)


        self.label_autor = ctk.CTkLabel(self, text="Desenvolvido por Wescley Henrique", font=("Orbitron", 12))
        self.label_autor.pack(pady=5)




    def realizar_limpeza_completa(self):
        print("\n--- INICIANDO LIMPEZA ---")
       
        try:
            cmd = "PowerShell.exe -NoProfile -Command Clear-RecycleBin -Force -ErrorAction SilentlyContinue"
            subprocess.run(cmd, shell=True)
            print("Lixeira processada.")
        except Exception as e:
            print(f"Erro na lixeira: {e}")


        base_users = r"C:\Users"
        try:
            if os.path.exists(base_users):
                usuarios = os.listdir(base_users)
        except Exception as e:
            print(f"Erro ao acessar usuários: {e}")
            for usuario in usuarios:
                caminho_temp = os.path.join(base_users, usuario, "AppData", "Local", "Temp")
               
                if os.path.exists(caminho_temp):
                    print(f"Limpando Temp de: {usuario}")
                for item in os.listdir(caminho_temp):
                    item_path = os.path.join(caminho_temp, item)
                    try:
                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            os.unlink(item_path)
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                    except:
                        pass
       
        print("--- LIMPEZA CONCLUÍDA ---")
        subprocess.Popen("msg * Limpeza Concluída com Sucesso!", shell=True)




    def executar(self, comando):
        try:
            if comando == "": return


            if comando in ["ipconfig", "systeminfo"]:
                subprocess.Popen(f'start cmd /k {comando}', shell=True)
            else:
                subprocess.Popen(comando, shell=True)


        except Exception as e:
            print(f"Erro ao executar o comando {comando}: {e}")




if __name__ == "__main__":
    app = AppManutencao()
    if os.path.exists("icon.ico"):
        app.iconbitmap("icon.ico")
    app.mainloop()