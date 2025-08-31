import os
import subprocess
import sys
import logging
from datetime import datetime

# ログ設定
log_file = "/home/gpotyglj/python/public/backend/uvicorn_debug.log"
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

def application(environ, start_response):
    """Passenger WSGI application"""
    try:
        logging.info(f"=== WSGI Application Called at {datetime.now()} ===")
        logging.info(f"Current working directory: {os.getcwd()}")
        logging.info(f"Python executable: {sys.executable}")
        logging.info(f"Environment variables: UVICORN_RUNNING={os.environ.get('UVICORN_RUNNING')}")
        logging.info(f"PATH: {os.environ.get('PATH', 'Not set')}")
        
        # uvicorn起動チェック
        if not os.environ.get("UVICORN_RUNNING"):
            logging.info("Starting uvicorn process...")
            os.environ["UVICORN_RUNNING"] = "1"
            
            uvicorn_path = "/home/gpotyglj/virtualenv/python/public/backend/3.11/bin/uvicorn"
            
            # uvicornの実行ファイルが存在するかチェック
            if not os.path.exists(uvicorn_path):
                logging.error(f"Uvicorn executable not found at: {uvicorn_path}")
                # 代替パスを試す
                alt_paths = [
                    "/home/gpotyglj/virtualenv/python/public/backend/3.11/bin/python -m uvicorn",
                    "python -m uvicorn"
                ]
                for alt_path in alt_paths:
                    logging.info(f"Trying alternative: {alt_path}")
            else:
                logging.info(f"Uvicorn found at: {uvicorn_path}")
            
            # uvicornプロセス起動
            try:
                cmd = [
                    uvicorn_path,
                    "app.main:app",
                    "--host", "127.0.0.1",
                    "--port", "8000",
                    "--log-level", "debug"
                ]
                logging.info(f"Executing command: {' '.join(cmd)}")
                
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd="/home/gpotyglj/python/public/backend"
                )
                logging.info(f"Uvicorn process started with PID: {process.pid}")
                
                # プロセスが即座に終了していないかチェック
                import time
                time.sleep(1)
                if process.poll() is not None:
                    stdout, stderr = process.communicate()
                    logging.error(f"Uvicorn process exited immediately!")
                    logging.error(f"STDOUT: {stdout.decode()}")
                    logging.error(f"STDERR: {stderr.decode()}")
                else:
                    logging.info("Uvicorn process appears to be running")
                    
            except Exception as e:
                logging.error(f"Failed to start uvicorn: {str(e)}")
                logging.error(f"Exception type: {type(e).__name__}")
        else:
            logging.info("Uvicorn already marked as running")
        
        # レスポンス返却
        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        body = f"Debug info logged to {log_file}. Check logs for details.".encode()
        start_response(status, headers)
        return [body]
        
    except Exception as e:
        logging.error(f"WSGI Application Error: {str(e)}")
        logging.error(f"Exception type: {type(e).__name__}")
        status = "500 Internal Server Error"
        headers = [("Content-Type", "text/plain")]
        body = f"Error: {str(e)}".encode()
        start_response(status, headers)
        return [body]