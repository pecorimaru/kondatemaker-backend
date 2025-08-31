import sys
import os

# アプリケーションのパスを追加
sys.path.insert(0, '/home/gpotyglj/python/public/backend')

try:
    # FastAPIアプリをインポート
    from app.main import app as fastapi_app
    
    # ASGI to WSGI adapter を使用
    from asgiref.wsgi import WsgiToAsgi
    
    # FastAPIアプリをWSGIアプリケーションに変換
    application = WsgiToAsgi(fastapi_app)
    
except ImportError as e:
    # asgirefがない場合の代替手段
    print(f"Import error: {e}")
    
    def application(environ, start_response):
        """Fallback WSGI application"""
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        body = f'Import Error: {str(e)}\nPlease install asgiref: pip install asgiref'
        start_response(status, headers)
        return [body.encode()]

except Exception as e:
    print(f"General error: {e}")
    
    def application(environ, start_response):
        """Error WSGI application"""
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        body = f'Application Error: {str(e)}'
        start_response(status, headers)
        return [body.encode()]