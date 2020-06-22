from singleton import DBConn, UserConfig
from factory import DBConnFactory
from prototype import UsuarioAdministrador, UsuarioNormal, Usuario, UsuarioSuperAdministrador
from main2 import abc
import requests

conn = DBConn()
conn2 = DBConn()
conn3 = DBConn()

conn.demo = 1

if conn == conn2:
    print('S')
else:
    print('N')

usuario_admin = UsuarioAdministrador('DEMO').clone()
usuario_normal = UsuarioNormal('NEMO').clone()
usuario_sa = UsuarioSuperAdministrador('SA').clone()

print(usuario_admin._permissions)
print(usuario_sa._permissions)
print(usuario_normal._permissions)

dbconn4 = DBConnFactory()
dbconn5 = DBConnFactory()


def listar_usuarios():
    url = 'https://api.usuariosservices.com/api/v2/usuario'
    headers = { "Content-Type": "application/json", "Accept": "application/json"}
    requests.post(url, {'username': 1}, headers=headers)
