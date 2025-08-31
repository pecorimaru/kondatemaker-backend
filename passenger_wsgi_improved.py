import os
import subprocess
import sys
import time
import signal
import atexit
from pathlib import Path

# 設定
UVICORN_PATH = "/home/gpotyglj/virtualenv/python/public/backend/3.11/bin/uvicorn"
APP_DIR = "/home/gpotyglj/python/public/backend"
PID_FILE = os.path.join(APP_DIR, "uvicorn.pid")
LOG_FILE = os.path.join(APP_DIR, "uvicorn.log")

def is_process_running(pid):
    """プロセスが実行中かチェック"""
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False

def cleanup_old_process():
    """古いプロセスをクリーンアップ"""
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, 'r') as f:
                old_pid = int(f.read().strip())
            
            if is_process_running(old_pid):
                os.kill(old_pid, signal.SIGTERM)
                time.sleep(2)
                if is_process_running(old_pid):
                    os.kill(old_pid, signal.SIGKILL)
            
            os.remove(PID_FILE)
        except (ValueError, FileNotFoundError, ProcessLookupError):
            pass

def start_uvicorn():
    """uvicornプロセスを起動"""
    cleanup_old_process()
    
    # 環境変数を設定
    env = os.environ.copy()
    env['PYTHONPATH'] = APP_DIR
    
    cmd = [
        UVICORN_PATH,
        "app.main:app",
        "--host", "127.0.0.1",
        "--port", "8000",
        "--log-config", None  # デフォルトログ設定を無効化
    ]
    
    try:
        with open(LOG_FILE, 'a') as log_f:
            process = subprocess.Popen(
                cmd,
                cwd=APP_DIR,
                env=env,
                stdout=log_f,
                stderr=subprocess.STDOUT,
                preexec_fn=os.setsid  # 新しいプロセスグループを作成
            )
        
        # PIDファイルに保存
        with open(PID_FILE, 'w') as f:
            f.write(str(process.pid))
        
        # プロセスが正常に起動したかチェック
        time.sleep(1)
        if process.poll() is None:
            return True
        else:
            return False
            
    except Exception as e:
        with open(LOG_FILE, 'a') as f:
            f.write(f"Failed to start uvicorn: {str(e)}\n")
        return False

def cleanup_on_exit():
    """終了時のクリーンアップ"""
    cleanup_old_process()

# 終了時のクリーンアップを登録
atexit.register(cleanup_on_exit)

# uvicorn起動
if not os.environ.get("UVICORN_STARTED"):
    os.environ["UVICORN_STARTED"] = "1"
    success = start_uvicorn()
    
    with open(LOG_FILE, 'a') as f:
        f.write(f"Uvicorn start attempt: {'SUCCESS' if success else 'FAILED'}\n")

def application(environ, start_response):
    """Passenger WSGI application"""
    # ヘルスチェック
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    
    # uvicornプロセスの状態確認
    uvicorn_status = "Unknown"
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, 'r') as f:
                pid = int(f.read().strip())
            uvicorn_status = "Running" if is_process_running(pid) else "Stopped"
        except:
            uvicorn_status = "Error reading PID"
    else:
        uvicorn_status = "Not started"
    
    body = f"Passenger WSGI is running.\nUvicorn status: {uvicorn_status}\nCheck logs at: {LOG_FILE}".encode()
    start_response(status, headers)
    return [body]