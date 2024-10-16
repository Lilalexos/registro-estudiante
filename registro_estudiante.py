class estudiante:
    def __init__(self, documento_identidad, tipo, numero_documento, nombres):
        self.documento_identidad = documento_identidad
        self.tipo = tipo
        self.numero_documento = numero_documento
        self.nombres = nombres

class curso:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

class sesion:
    def __init__(self, codigo_curso, hora_inicio, hora_final, fecha):
        self.codigo_curso = codigo_curso
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.fecha = fecha

class asistencia:
    def __init__(self, codigo_sesion, documento_estudiante, estado=2):
        self.codigo_sesion = codigo_sesion
        self.documento_estudiante = documento_estudiante
        self.estado = estado  # 0: no llego, 1: llego, 2: llego tarde

class sistema:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []
        self.sesiones = []
        self.asistencias = []

    def agregar_estudiante(self):
        documento_identidad = input("documento de identidad: ")
        tipo = input("tipo (ej. cc, ti): ")
        numero_documento = input("numero de documento: ")
        nombres = input("nombres del estudiante: ")
        nuevo_estudiante = estudiante(documento_identidad, tipo, numero_documento, nombres)
        self.estudiantes.append(nuevo_estudiante)
        print("estudiante agregado.")

    def agregar_curso(self):
        codigo = input("codigo del curso: ")
        nombre = input("nombre del curso: ")
        nuevo_curso = curso(codigo, nombre)
        self.cursos.append(nuevo_curso)
        print("curso agregado.")

    def agregar_sesion(self):
        codigo_curso = input("codigo del curso: ")
        hora_inicio = input("hora de inicio (hh:mm): ")
        hora_final = input("hora final (hh:mm): ")
        fecha = input("fecha (dd/mm/aaaa): ")
        nueva_sesion = sesion(codigo_curso, hora_inicio, hora_final, fecha)
        self.sesiones.append(nueva_sesion)
        print("sesion agregada.")

    def agregar_asistencia(self):
        codigo_sesion = input("codigo de la sesion: ")
        documento_estudiante = input("documento del estudiante: ")
        estado = input("estado (0: no llego, 1: llego, 2: llego tarde): ")
        estado = int(estado) if estado.isdigit() and int(estado) in [0, 1, 2] else 2
        nueva_asistencia = asistencia(codigo_sesion, documento_estudiante, estado)
        self.asistencias.append(nueva_asistencia)
        print("asistencia registrada.")

    def listar_estudiantes(self):
        print("\nlista de estudiantes:")
        for est in self.estudiantes:
            print(f"id: {est.documento_identidad}, nombres: {est.nombres}")
        print(f"numero total de estudiantes: {len(self.estudiantes)}")

    def listar_cursos(self):
        print("\nlista de cursos:")
        for cur in self.cursos:
            print(f"codigo: {cur.codigo}, nombre: {cur.nombre}")
        print(f"numero total de cursos: {len(self.cursos)}")

    def listar_sesiones(self):
        print("\nlista de sesiones:")
        for ses in self.sesiones:
            print(f"codigo: {ses.codigo_curso}, fecha: {ses.fecha}, hora: {ses.hora_inicio} - {ses.hora_final}")
        print(f"numero total de sesiones: {len(self.sesiones)}")

    def listar_asistencias(self):
        print("\nlista de asistencias:")
        for asis in self.asistencias:
            print(f"codigo sesion: {asis.codigo_sesion}, estudiante id: {asis.documento_estudiante}, estado: {asis.estado}")
        print(f"numero total de asistencias: {len(self.asistencias)}")

    def buscar_estudiante(self):
        documento = input("ingrese el documento de identidad del estudiante: ")
        for est in self.estudiantes:
            if est.documento_identidad == documento:
                print(f"estudiante encontrado: {est.nombres}")
                return
        print("estudiante no encontrado.")

    def buscar_curso(self):
        codigo = input("ingrese el codigo del curso: ")
        for cur in self.cursos:
            if cur.codigo == codigo:
                print(f"curso encontrado: {cur.nombre}")
                return
        print("curso no encontrado.")

    def buscar_sesion(self):
        codigo = input("ingrese el codigo de la sesion: ")
        for ses in self.sesiones:
            if ses.codigo_curso == codigo:
                print(f"sesion encontrada: {ses.fecha} de {ses.hora_inicio} a {ses.hora_final}")
                return
        print("sesion no encontrada.")

    def buscar_asistencia(self):
        codigo_sesion = input("ingrese el codigo de la sesion: ")
        documento_estudiante = input("ingrese el documento del estudiante: ")
        for asis in self.asistencias:
            if asis.codigo_sesion == codigo_sesion and asis.documento_estudiante == documento_estudiante:
                print(f"asistencia: estado: {asis.estado}")
                return
        print("asistencia no encontrada.")

def main():
    sistema_obj = sistema()
    while True:
        print("\nmenu:")
        print("1. agregar estudiante")
        print("2. agregar curso")
        print("3. agregar sesion")
        print("4. agregar asistencia")
        print("5. listar estudiantes")
        print("6. listar cursos")
        print("7. listar sesiones")
        print("8. listar asistencias")
        print("9. buscar estudiante")
        print("10. buscar curso")
        print("11. buscar sesion")
        print("12. buscar asistencia")
        print("13. salir")
        opcion = input("seleccione una opcion: ")

        if opcion == '1':
            sistema_obj.agregar_estudiante()
        elif opcion == '2':
            sistema_obj.agregar_curso()
        elif opcion == '3':
            sistema_obj.agregar_sesion()
        elif opcion == '4':
            sistema_obj.agregar_asistencia()
        elif opcion == '5':
            sistema_obj.listar_estudiantes()
        elif opcion == '6':
            sistema_obj.listar_cursos()
        elif opcion == '7':
            sistema_obj.listar_sesiones()
        elif opcion == '8':
            sistema_obj.listar_asistencias()
        elif opcion == '9':
            sistema_obj.buscar_estudiante()
        elif opcion == '10':
            sistema_obj.buscar_curso()
        elif opcion == '11':
            sistema_obj.buscar_sesion()
        elif opcion == '12':
            sistema_obj.buscar_asistencia()
        elif opcion == '13':
            print("saliendo...")
            break
        else:
            print("opcion no valida. intente de nuevo.")

if __name__ == "__main__":
    main()
