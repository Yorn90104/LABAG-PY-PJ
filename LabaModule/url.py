import subprocess

def commit_score(name, score):
    """上傳資料至試算表"""
    if name != "" :
        url = f"https://docs.google.com/forms/d/18dVGtPExBUc0p1VbsmMxCyujQoldI6GKQWZQGJQ-yzY/formResponse?entry.582969025={name}&entry.995493130={score}"
        subprocess.Popen(['curl', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)