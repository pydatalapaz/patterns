from adapter import ApiClient, ApiRestClient, SoapClient, WCFClient, WCFClientAdapter
from bridge import Foco, HomeSwitch, Computador
from decorator import Pudge, CinturonFuerza, CapaMago
from composite import Empleado, JefeUnidad, Area
from facade import crear_organigrama
from flyweight import ImagenFactory

def version_printer(api: ApiClient):
    print(api.version())

rest_client = ApiRestClient()
soap_client = SoapClient()
wcf_client = WCFClientAdapter(WCFClient())

version_printer(rest_client)
version_printer(soap_client)
version_printer(wcf_client)

sw = HomeSwitch(Computador())
sw.encender()
sw.apagar()

pudge = CapaMago(CinturonFuerza(Pudge()))
print(pudge.fuerza())
print(pudge.inteligencia())

area = crear_organigrama()
area.notificar()

factory = ImagenFactory()
factory_dos = ImagenFactory()
factory.get_imagen('a').mostrar(1, 1)
factory.get_imagen('b').mostrar(2, 2)
factory.get_imagen('c').mostrar(2, 2)

assert factory.get_imagen('a') == factory_dos.get_imagen('a')
# Proxy
# Flyweight

