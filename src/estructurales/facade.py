from composite import Area, JefeUnidad, Empleado

def crear_organigrama() -> Area:
    goku = JefeUnidad('goku')
    area = Area(goku)
    area.agregar(Empleado('Gohan'))
    area.agregar(Area(Empleado('Piccolo')))
    area.agregar(Area(Empleado('Vegeta')))
    area.agregar(Area(Empleado('Bulma')))
    area.agregar(Area(Empleado('Roshi')))
    return area